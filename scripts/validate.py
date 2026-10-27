#!/usr/bin/env python3
"""Validate all programme content against schema/ plus the structural rules.

Usage:  python scripts/validate.py [--quiet]

Exit code 0 = no errors (warnings are allowed), 1 = errors.

Everything that can be a JSON Schema rule lives in schema/. This script adds
the cross-file rules a schema can't express (see docs/content-format.md,
"Validation rules"). The bot reimplements these checks; keep them few and
documented.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
SCHEMA_BASE = "https://github.com/splinterlearn/programme/schema/"

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PLACEHOLDER = re.compile(r"\{\{\s*([a-z][a-z0-9_]*)\s*\}\}")
TRACK_HEADING = re.compile(r"^## Track: ([a-z][a-z0-9-]*)\s*$", re.MULTILINE)


# --------------------------------------------------------------------------
# YAML loading: JSON-compatible and unambiguous across YAML 1.1 / 1.2 parsers
# --------------------------------------------------------------------------

class StrictLoader(yaml.SafeLoader):
    """SafeLoader that only treats true/false as booleans and keeps dates as strings.

    Unquoted yes/no/on/off are recorded so they can be reported: YAML 1.1
    parsers read them as booleans, YAML 1.2 parsers as strings.
    """


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers
          if tag not in ("tag:yaml.org,2002:bool", "tag:yaml.org,2002:timestamp")]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
StrictLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
    list("tTfF"),
)
AMBIGUOUS = re.compile(r"^(?:yes|Yes|YES|no|No|NO|on|On|ON|off|Off|OFF)$")


def _construct_str(loader: StrictLoader, node: yaml.ScalarNode) -> str:
    if node.style is None and AMBIGUOUS.match(node.value):
        loader.ambiguous.append((node.value, node.start_mark.line + 1))
    return loader.construct_scalar(node)


StrictLoader.add_constructor("tag:yaml.org,2002:str", _construct_str)


def load_yaml(text: str) -> tuple[object, list[tuple[str, int]]]:
    loader = StrictLoader(text)
    loader.ambiguous = []
    try:
        return loader.get_single_data(), loader.ambiguous
    finally:
        loader.dispose()


def split_frontmatter(text: str) -> tuple[str | None, str, int]:
    """Return (frontmatter, body, body_start_line). Frontmatter is None if absent."""
    if not text.startswith("---\n"):
        return None, text, 1
    end = text.find("\n---\n", 4)
    if end == -1:
        if text.endswith("\n---"):
            end = len(text) - 4
        else:
            return None, text, 1
    fm = text[4:end + 1]
    body = text[end + 5:]
    return fm, body, fm.count("\n") + 3


def non_string_keys(data: object, path: str = "") -> list[str]:
    bad = []
    if isinstance(data, dict):
        for k, v in data.items():
            if not isinstance(k, str):
                bad.append(f"{path}/{k!r}")
            bad.extend(non_string_keys(v, f"{path}/{k}"))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            bad.extend(non_string_keys(v, f"{path}/{i}"))
    return bad


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, where: Path | str, msg: str) -> None:
        self.errors.append(f"{rel(where)}: {msg}")

    def warn(self, where: Path | str, msg: str) -> None:
        self.warnings.append(f"{rel(where)}: {msg}")

    def problem(self, strict: bool, where: Path | str, msg: str) -> None:
        """Error when strict (ready content), warning otherwise (drafts)."""
        (self.error if strict else self.warn)(where, msg)


def rel(p: Path | str) -> str:
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


# --------------------------------------------------------------------------
# Schemas
# --------------------------------------------------------------------------

class Schemas:
    def __init__(self, report: Report):
        self.report = report
        resources = []
        self.raw: dict[str, dict] = {}
        for path in sorted(SCHEMA_DIR.rglob("*.schema.json")):
            try:
                doc = json.loads(path.read_text())
                Draft202012Validator.check_schema(doc)
            except Exception as exc:  # noqa: BLE001 - report any schema problem
                report.error(path, f"invalid schema: {exc}")
                continue
            if not doc.get("$id", "").startswith(SCHEMA_BASE):
                report.error(path, f"$id must start with {SCHEMA_BASE}")
                continue
            name = str(path.relative_to(SCHEMA_DIR))
            if doc["$id"] != SCHEMA_BASE + name:
                report.error(path, f"$id must be {SCHEMA_BASE + name}")
            self.raw[name] = doc
            resources.append((doc["$id"], Resource.from_contents(doc)))
        self.registry = Registry().with_resources(resources)

    def check(self, name: str, data: object, where: Path) -> bool:
        doc = self.raw.get(name)
        if doc is None:
            self.report.error(where, f"schema {name} not found")
            return False
        validator = Draft202012Validator(doc, registry=self.registry)
        errs = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
        for e in errs:
            loc = "/".join(str(p) for p in e.absolute_path) or "(root)"
            self.report.error(where, f"[{name}] {loc}: {e.message}")
        return not errs


# --------------------------------------------------------------------------
# Loading content files
# --------------------------------------------------------------------------

def load_data_file(path: Path, report: Report, frontmatter: bool) -> tuple[object, str] | None:
    """Load YAML (or the frontmatter of a Markdown file). Returns (data, body)."""
    if not path.is_file():
        report.error(path, "file missing")
        return None
    text = path.read_text(encoding="utf-8")
    body = ""
    if frontmatter:
        fm, body, _ = split_frontmatter(text)
        if fm is None:
            report.error(path, "missing YAML frontmatter (--- ... ---)")
            return None
        text = fm
    try:
        data, ambiguous = load_yaml(text)
    except yaml.YAMLError as exc:
        report.error(path, f"YAML error: {exc}")
        return None
    for value, line in ambiguous:
        report.error(path, f"line {line}: unquoted {value!r} is a boolean in YAML 1.1 and a string in 1.2; quote it")
    for key in non_string_keys(data):
        report.error(path, f"non-string key at {key} (quote it, e.g. \"0\":)")
    return data, body


def test_names(test_dir: Path) -> set[str]:
    names: set[str] = set()
    for f in sorted(test_dir.rglob("test_*.py")):
        tree = ast.parse(f.read_text(encoding="utf-8"), filename=str(f))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                names.add(node.name)
    return names


# --------------------------------------------------------------------------
# Validator
# --------------------------------------------------------------------------

class Validator:
    def __init__(self) -> None:
        self.r = Report()
        self.s = Schemas(self.r)
        self.track_ids: set[str] = set()
        self.rubrics: dict[str, dict] = {}
        self.levels: list[dict] = []
        self.blocks: dict[str, dict] = {}
        self.modules: dict[str, dict] = {}
        self.fingerprints: dict[str, str] = {}

    # ---- top level -------------------------------------------------------

    def run(self) -> Report:
        self.check_version()
        self.check_tracks()
        self.check_tutor()
        self.check_blocks()
        self.check_licence_ladder()
        self.check_todos()
        return self.r

    def check_version(self) -> None:
        path = SCHEMA_DIR / "VERSION"
        if not path.is_file():
            self.r.error(path, "missing")
            return
        if not SEMVER.match(path.read_text().strip()):
            self.r.error(path, "must be a semver string like 1.0.0")

    def check_tracks(self) -> None:
        for path in sorted((ROOT / "tracks").glob("*.md")):
            if path.name == "README.md":
                continue
            loaded = load_data_file(path, self.r, frontmatter=True)
            if not loaded:
                continue
            data, _ = loaded
            if self.s.check("track.schema.json", data, path):
                if data["id"] != path.stem:
                    self.r.error(path, f"id {data['id']!r} must match the file name")
                self.track_ids.add(data["id"])
        if not self.track_ids:
            self.r.error("tracks/", "no tracks found")

    # ---- tutor/ ----------------------------------------------------------

    def check_tutor(self) -> None:
        tutor = ROOT / "tutor"
        loaded = load_data_file(tutor / "licence-levels.yaml", self.r, frontmatter=False)
        if loaded and self.s.check("licence-levels.schema.json", loaded[0], tutor / "licence-levels.yaml"):
            self.levels = loaded[0]["levels"]
            ids = [lvl["id"] for lvl in self.levels]
            if ids != ["L0", "L1", "L2", "L3"]:
                self.r.error(tutor / "licence-levels.yaml", f"levels must be L0, L1, L2, L3 in order (got {ids})")

        for path in sorted((tutor / "rubrics").glob("*.yaml")):
            loaded = load_data_file(path, self.r, frontmatter=False)
            if not loaded or not self.s.check("rubric.schema.json", loaded[0], path):
                continue
            rubric = loaded[0]
            if rubric["id"] != path.stem:
                self.r.error(path, "id must match the file name")
            crit = [c["id"] for c in rubric["criteria"]]
            if len(crit) != len(set(crit)):
                self.r.error(path, "duplicate criterion ids")
            if rubric["pass_threshold"] > 2 * len(crit):
                self.r.error(path, "pass_threshold is higher than the maximum score")
            self.rubrics[rubric["id"]] = rubric

        begging = tutor / "test-cases" / "begging.yaml"
        loaded = load_data_file(begging, self.r, frontmatter=False)
        if loaded and self.s.check("begging-tests.schema.json", loaded[0], begging):
            ids = [c["id"] for c in loaded[0]["cases"]]
            if len(ids) != len(set(ids)):
                self.r.error(begging, "duplicate case ids")

        readme = tutor / "README.md"
        readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        if not readme_text:
            self.r.error(readme, "missing")
        documented = set(PLACEHOLDER.findall(readme_text))
        for path in sorted(tutor.glob("*.md")):
            if path.name == "README.md":
                continue
            loaded = load_data_file(path, self.r, frontmatter=True)
            if not loaded or not self.s.check("prompt.schema.json", loaded[0], path):
                continue
            meta, body = loaded
            if meta["id"] != path.stem:
                self.r.error(path, "id must match the file name")
            used = set(PLACEHOLDER.findall(body))
            declared = set(meta["placeholders"])
            for name in sorted(used - declared):
                self.r.error(path, f"placeholder {{{{{name}}}}} is used but not declared in frontmatter")
            for name in sorted(declared - used):
                self.r.warn(path, f"placeholder {name!r} is declared but not used")
            for name in sorted(used - documented):
                self.r.error(path, f"placeholder {{{{{name}}}}} is not documented in tutor/README.md")
            if meta["output_schema"] and not (ROOT / meta["output_schema"]).is_file():
                self.r.error(path, f"output_schema {meta['output_schema']} does not exist")

    # ---- blocks ----------------------------------------------------------

    def check_blocks(self) -> None:
        blocks_dir = ROOT / "blocks"
        if not blocks_dir.is_dir():
            self.r.error(blocks_dir, "missing")
            return
        dirs = sorted(d for d in blocks_dir.iterdir() if d.is_dir())
        prev_weeks = None
        for bdir in dirs:
            m = re.match(r"^(b[0-9])-[a-z0-9-]+$", bdir.name)
            if not m:
                self.r.error(bdir, "block folders are named <id>-<slug>, e.g. b2-fundamentals")
                continue
            loaded = load_data_file(bdir / "block.md", self.r, frontmatter=True)
            if not loaded or not self.s.check("block.schema.json", loaded[0], bdir / "block.md"):
                continue
            block = loaded[0]
            if block["id"] != m.group(1):
                self.r.error(bdir / "block.md", f"id {block['id']!r} must match the folder prefix {m.group(1)!r}")
            if block["weeks"][0] > block["weeks"][1]:
                self.r.error(bdir / "block.md", "weeks must be [first, last]")
            if prev_weeks and block["weeks"][0] <= prev_weeks[1]:
                self.r.error(bdir / "block.md", f"weeks overlap the previous block {prev_weeks}")
            prev_weeks = block["weeks"]
            self.blocks[block["id"]] = block
            self.check_block(bdir, block)

    def check_block(self, bdir: Path, block: dict) -> None:
        bid = block["id"]
        where = bdir / "block.md"
        project = block["project"]
        if project:
            for track in project["folders"]:
                if track not in self.track_ids:
                    self.r.error(where, f"project.folders: unknown track {track!r}")
            if not project["id"].startswith(bid + "-"):
                self.r.error(where, f"project.id must start with {bid}-")

        entries = block["modules"]
        ids = [e["id"] for e in entries]
        if len(ids) != len(set(ids)):
            self.r.error(where, "duplicate module ids")
        for e in entries:
            if not e["id"].startswith("m" + bid[1:] + "."):
                self.r.error(where, f"module {e['id']} does not belong to block {bid}")
        numbers = [int(i.split(".")[1]) for i in ids]
        if numbers != sorted(numbers):
            self.r.error(where, "modules must be listed in order")

        folders: dict[str, Path] = {}
        for d in sorted(p for p in bdir.iterdir() if p.is_dir()):
            mm = re.match(r"^(m[0-9]\.[0-9]+)-[a-z0-9-]+$", d.name)
            if not mm:
                self.r.error(d, "unexpected folder in a block (module folders are <id>-<slug>)")
                continue
            folders[mm.group(1)] = d

        for e in entries:
            if e["status"] == "stub":
                if e["id"] in folders:
                    self.r.error(where, f"{e['id']} is a stub but has a folder; set its status or remove the folder")
            elif e["id"] not in folders:
                self.r.error(where, f"{e['id']} has status {e['status']} but no folder")
        for mid in folders:
            if mid not in ids:
                self.r.error(folders[mid], f"folder for {mid} is not listed in block.md modules")

        statuses = {e["id"]: e["status"] for e in entries}
        for mid, mdir in folders.items():
            module = self.check_module(mdir, block)
            if module and mid in statuses and module["status"] != statuses[mid]:
                self.r.error(where, f"{mid}: status {statuses[mid]!r} here but {module['status']!r} in module.md")

        if block["status"] == "ready" and any(e["status"] != "ready" for e in entries):
            self.r.error(where, "a ready block must have only ready modules")

        skip_path = bdir / "skip-test.md"
        if block["skip_test"] is None:
            if skip_path.exists():
                self.r.error(where, "skip_test is null but skip-test.md exists")
        else:
            self.check_skip_test(bdir, block)

    # ---- modules ---------------------------------------------------------

    def check_module(self, mdir: Path, block: dict) -> dict | None:
        where = mdir / "module.md"
        loaded = load_data_file(where, self.r, frontmatter=True)
        if not loaded or not self.s.check("module.schema.json", loaded[0], where):
            return None
        mod = loaded[0]
        mid = mod["id"]
        strict = mod["status"] == "ready"
        self.modules[mid] = mod

        if not mdir.name.startswith(mid + "-"):
            self.r.error(where, f"id {mid!r} must match the folder prefix")
        if mod["block"] != block["id"]:
            self.r.error(where, f"block {mod['block']!r} but the folder is in {block['id']!r}")
        if mod["licence_level"] != block["licence_level"]:
            self.r.error(where, f"licence_level {mod['licence_level']} differs from the block's {block['licence_level']}")
        bw, mw = block["weeks"], mod["weeks"]
        if not (bw[0] <= mw[0] <= mw[1] <= bw[1]):
            self.r.error(where, f"weeks {mw} must lie within the block's weeks {bw}")

        ns = [s["n"] for s in mod["sessions"]]
        if ns != list(range(1, len(ns) + 1)):
            self.r.error(where, "sessions must be numbered 1, 2, 3, ...")
        if len(ns) != mod["est_sessions"]:
            self.r.error(where, f"est_sessions is {mod['est_sessions']} but {len(ns)} sessions are listed")

        comp_ids = [c["id"] for c in mod["competencies"]]
        self._ids_unique_prefixed(where, comp_ids, f"{mid}.c", "competency")
        check_ids = [c["id"] for c in mod["checks"]]
        self._ids_unique_prefixed(where, check_ids, f"{mid}.k", "check")

        for fp in mod["cs50_fingerprints"]:
            other = self.fingerprints.get(fp["filename"])
            if other and other != mid:
                self.r.error(where, f"CS50 fingerprint {fp['filename']} is also in {other}")
            self.fingerprints[fp["filename"]] = mid

        # explain-back bank
        questions: dict[str, dict] = {}
        eb_path = mdir / "explain-back.yaml"
        if mod["explain_back"]:
            if eb_path.is_file():
                questions = self.check_bank(eb_path, mid, set(comp_ids), strict)
            else:
                self.r.problem(strict, where, "explain_back is true but explain-back.yaml is missing")
        elif eb_path.exists():
            self.r.error(where, "explain_back is false but explain-back.yaml exists")

        # remix
        remix = mod["remix"]
        tested: list[str | None] = [None]
        tests_by_track: dict[str | None, set[str]] = {}
        rubric = None
        if remix:
            tested = list(remix["tracks"]) or [None]
            rubric = self.check_remix(mdir, mod, block, strict)
            for t in remix["tracks"]:
                tdir = mdir / "tracks" / t / "tests"
                tests_by_track[t] = test_names(tdir) if tdir.is_dir() else set()
        else:
            files = [p for p in mdir.rglob("test_*.py")]
            names: set[str] = set()
            for f in files:
                names |= test_names(f.parent)
            tests_by_track[None] = names
            if (mdir / "remix.md").exists():
                self.r.error(where, "remix is null but remix.md exists")

        self.check_coverage(where, mod, questions, tests_by_track, tested, rubric, set(check_ids), strict)
        if remix:
            for ref in remix["edge_case"]["covered_by"]:
                self._resolve_ref(where, ref, questions, tests_by_track, rubric, set(check_ids), strict, "edge_case.covered_by")
            missing = set(remix["tracks"]) - set(remix["edge_case"]["per_track"])
            if missing:
                self.r.problem(strict, where, f"edge_case.per_track has no entry for {sorted(missing)}")
        self.check_student_files(mdir, mod, block, strict)
        return mod

    def _ids_unique_prefixed(self, where: Path, ids: list[str], prefix: str, kind: str) -> None:
        if len(ids) != len(set(ids)):
            self.r.error(where, f"duplicate {kind} ids")
        for i in ids:
            if not i.startswith(prefix):
                self.r.error(where, f"{kind} id {i!r} must start with {prefix!r}")

    def check_bank(self, path: Path, scope: str, comp_ids: set[str], strict: bool) -> dict[str, dict]:
        loaded = load_data_file(path, self.r, frontmatter=False)
        if not loaded or not self.s.check("explain-back.schema.json", loaded[0], path):
            return {}
        bank = loaded[0]
        if bank["scope"] != scope:
            self.r.error(path, f"scope must be {scope!r}")
        qids = [q["id"] for q in bank["questions"]]
        self._ids_unique_prefixed(path, qids, f"{scope}.q", "question")
        for q in bank["questions"]:
            for c in q["competencies"]:
                if c not in comp_ids:
                    self.r.error(path, f"{q['id']}: unknown competency {c}")
            if q["tracks"] != "all":
                for t in q["tracks"]:
                    if t not in self.track_ids:
                        self.r.error(path, f"{q['id']}: unknown track {t}")
            if q["type"] != "micro-task" and any(k in q for k in ("code", "expected_fix", "ai_off")):
                if q.get("ai_off") is True or "expected_fix" in q:
                    self.r.error(path, f"{q['id']}: ai_off/expected_fix are only for micro-task questions")
        return {q["id"]: q for q in bank["questions"]}

    def check_remix(self, mdir: Path, mod: dict, block: dict, strict: bool) -> dict | None:
        where = mdir / "module.md"
        remix = mod["remix"]
        project = block["project"]
        if not project:
            self.r.error(where, "module has a remix but the block has no project")
        elif remix["project_id"] != project["id"]:
            self.r.error(where, f"remix.project_id {remix['project_id']!r} must be the block project {project['id']!r}")

        overlap = set(remix["tracks"]) & set(remix["brief_only_tracks"])
        if overlap:
            self.r.error(where, f"tracks and brief_only_tracks overlap: {sorted(overlap)}")
        for t in remix["tracks"] + remix["brief_only_tracks"]:
            if t not in self.track_ids:
                self.r.error(where, f"remix: unknown track {t!r} (no tracks/{t}.md)")

        for t in remix["tracks"]:
            tdir = mdir / "tracks" / t
            tests = tdir / "tests"
            if not (tests.is_dir() and any(tests.glob("test_*.py"))):
                self.r.problem(strict, where, f"track {t}: missing tracks/{t}/tests/test_*.py  TODO(next-task)?")
            cp = tdir / "checkpoint"
            if not (cp.is_dir() and any(cp.glob("*.py"))):
                self.r.problem(strict, where, f"track {t}: missing tracks/{t}/checkpoint/")

        rpath = mdir / "remix.md"
        loaded = load_data_file(rpath, self.r, frontmatter=True)
        if loaded and self.s.check("remix.schema.json", loaded[0], rpath):
            meta, body = loaded
            if meta["module"] != mod["id"] or meta["step"] != remix["step"]:
                self.r.error(rpath, "module/step must match module.md")
            headings = TRACK_HEADING.findall(body)
            for t in remix["tracks"] + remix["brief_only_tracks"]:
                if t not in headings:
                    self.r.error(rpath, f"missing section '## Track: {t}'")
            for h in headings:
                if h not in remix["tracks"] + remix["brief_only_tracks"]:
                    self.r.error(rpath, f"section for track {h!r} not listed in module.md remix")

        rubric = self.rubrics.get(remix["rubric"])
        if rubric is None:
            self.r.error(where, f"rubric {remix['rubric']!r} not found in tutor/rubrics/")
        return rubric

    def check_coverage(self, where, mod, questions, tests_by_track, tested, rubric, checks, strict) -> None:
        cov = mod["coverage"]
        comp_ids = [c["id"] for c in mod["competencies"]]
        for cid in comp_ids:
            if cid not in cov:
                self.r.error(where, f"coverage: competency {cid} is not covered by any gate item")
        for cid in cov:
            if cid not in comp_ids:
                self.r.error(where, f"coverage: unknown competency {cid}")

        for cid, refs in cov.items():
            for ref in refs:
                self._resolve_ref(where, ref, questions, tests_by_track, rubric, checks, strict, f"coverage.{cid}")
                kind, _, val = ref.partition(":")
                if kind == "eb" and val in questions and cid not in questions[val]["competencies"]:
                    self.r.problem(strict, where, f"coverage.{cid}: {val} does not list {cid} in its competencies")

            # Per tested track: at least one item that exists and applies to that track.
            for track in tested:
                if not any(self._applies(ref, track, questions, tests_by_track, rubric, checks) for ref in refs):
                    label = f"track {track}" if track else "this module"
                    self.r.problem(strict, where, f"coverage: {cid} has no existing gate item for {label}")

    def _applies(self, ref, track, questions, tests_by_track, rubric, checks) -> bool:
        kind, _, val = ref.partition(":")
        if kind == "test":
            return val in tests_by_track.get(track, set())
        if kind == "eb":
            q = questions.get(val)
            return bool(q) and (q["tracks"] == "all" or track is None or track in q["tracks"])
        if kind == "rubric":
            return bool(rubric) and any(c["id"] == val for c in rubric["criteria"])
        if kind == "check":
            return val in checks
        return False

    def _resolve_ref(self, where, ref, questions, tests_by_track, rubric, checks, strict, ctx) -> None:
        kind, _, val = ref.partition(":")
        if kind == "test":
            for track, names in tests_by_track.items():
                if val not in names:
                    label = f"tracks/{track}/tests" if track else "the module's test files"
                    self.r.problem(strict, where, f"{ctx}: test {val!r} not found in {label}")
            if not tests_by_track:
                self.r.problem(strict, where, f"{ctx}: test {val!r} but the module has no tests")
        elif kind == "eb":
            if val not in questions:
                self.r.problem(strict, where, f"{ctx}: question {val!r} not found in explain-back.yaml")
        elif kind == "rubric":
            if not rubric:
                self.r.error(where, f"{ctx}: {ref} but the module has no rubric (no remix, or the rubric file is missing)")
            elif not any(c["id"] == val for c in rubric["criteria"]):
                self.r.error(where, f"{ctx}: rubric criterion {val!r} not in {rubric['id']}")
        elif kind == "check":
            if val not in checks:
                self.r.error(where, f"{ctx}: check {val!r} not defined in checks")
        elif kind == "task":
            self.r.error(where, f"{ctx}: task: references are only valid in skip tests")

    def check_student_files(self, mdir: Path, mod: dict, block: dict, strict: bool) -> None:
        where = mdir / "module.md"
        remix = mod["remix"]
        tracks = remix["tracks"] if remix else []
        for sf in mod["student_files"]:
            src, dst = sf["from"], sf["to"]
            if "{project_dir}" in src:
                self.r.error(where, f"student_files: {{project_dir}} belongs in 'to', not 'from' ({src})")
            if ("{track}" in src or "{project_dir}" in dst) and not remix:
                self.r.error(where, f"student_files: {src} -> {dst} uses placeholders but the module has no remix")
                continue
            if src.endswith("/") != dst.endswith("/"):
                self.r.error(where, f"student_files: {src} -> {dst}: folders end with / on both sides")
            expanded = [src.replace("{track}", t) for t in tracks] if "{track}" in src else [src]
            for s in expanded:
                target = mdir / s
                ok = target.is_dir() if s.endswith("/") else target.is_file()
                if not ok:
                    self.r.problem(strict, where, f"student_files: {s} does not exist")

    # ---- skip tests ------------------------------------------------------

    def check_skip_test(self, bdir: Path, block: dict) -> None:
        path = bdir / "skip-test.md"
        loaded = load_data_file(path, self.r, frontmatter=True)
        if not loaded or not self.s.check("skip-test.schema.json", loaded[0], path):
            return
        st = loaded[0]
        bid = block["id"]
        strict = st["status"] == "ready"
        if st["id"] != f"{bid}-skip" or st["block"] != bid:
            self.r.error(path, f"id must be {bid}-skip and block {bid}")
        if st["kind"] == "module-gates":
            listed = [e["id"] for e in block["modules"]]
            if st["modules"] != listed:
                self.r.error(path, f"modules must be all of the block's modules in order: {listed}")
            for mid in st["modules"]:
                mod = self.modules.get(mid)
                if mod is None:
                    self.r.problem(strict, path, f"{mid} has no module.md yet")
                elif mod["status"] != "ready":
                    self.r.warn(path, f"{mid} is {mod['status']}; the bot serves only ready modules' gates")
            return

        scope = f"{bid}.skip"
        comp_ids = [c["id"] for c in st["competencies"]]
        self._ids_unique_prefixed(path, comp_ids, f"{scope}.c", "competency")
        task_ids = [t["id"] for t in st["tasks"]]
        self._ids_unique_prefixed(path, task_ids, f"{scope}.t", "task")
        bank_path = bdir / st["explain_back"]["file"]
        questions = self.check_bank(bank_path, scope, set(comp_ids), strict) if bank_path.is_file() else {}
        if not bank_path.is_file():
            self.r.error(path, f"explain_back.file {st['explain_back']['file']} not found")
        micro = sum(1 for q in questions.values() if q["type"] == "micro-task")
        if questions and st["explain_back"]["sample"] > len(questions) - micro:
            self.r.error(path, "explain_back.sample is larger than the number of non-micro-task questions")
        if questions and st["explain_back"]["micro_tasks"] > micro:
            self.r.error(path, "explain_back.micro_tasks is larger than the number of micro-tasks in the bank")
        for cid in comp_ids:
            if cid not in st["coverage"]:
                self.r.error(path, f"coverage: competency {cid} is not covered")
        for cid, refs in st["coverage"].items():
            if cid not in comp_ids:
                self.r.error(path, f"coverage: unknown competency {cid}")
            for ref in refs:
                kind, _, val = ref.partition(":")
                if kind == "task" and val not in task_ids:
                    self.r.error(path, f"coverage.{cid}: task {val} not defined")
                elif kind == "eb" and val not in questions:
                    self.r.error(path, f"coverage.{cid}: question {val} not in the bank")
                elif kind not in ("task", "eb"):
                    self.r.error(path, f"coverage.{cid}: skip tests use task: and eb: references only")

    # ---- cross-file ------------------------------------------------------

    def check_licence_ladder(self) -> None:
        where = ROOT / "tutor" / "licence-levels.yaml"
        unlocks = {lvl["unlock"].get("block"): lvl["id"] for lvl in self.levels if lvl["unlock"]["on"] == "block_exit"}
        for bid, block in self.blocks.items():
            expected = unlocks.get(bid)
            if block["licence_unlock_on_exit"] != expected:
                self.r.error(ROOT / "blocks", f"{bid}: licence_unlock_on_exit is {block['licence_unlock_on_exit']!r} "
                                              f"but licence-levels.yaml says {expected!r}")
        for bid in unlocks:
            if bid not in self.blocks:
                self.r.error(where, f"unlock refers to unknown block {bid}")
        # Each block's licence is the one in effect after the previous unlocks.
        order = ["L0", "L1", "L2", "L3"]
        current = "L0"
        for bid in sorted(self.blocks):
            block = self.blocks[bid]
            if block["licence_level"] != current:
                self.r.error(ROOT / "blocks", f"{bid}: licence_level should be {current} (after earlier unlocks), "
                                              f"not {block['licence_level']}")
            if block["licence_unlock_on_exit"]:
                if order.index(block["licence_unlock_on_exit"]) != order.index(current) + 1:
                    self.r.error(ROOT / "blocks", f"{bid}: unlock must be the next level after {current}")
                current = block["licence_unlock_on_exit"]

    def check_todos(self) -> None:
        verify = 0
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file() or any(p in path.parts for p in (".git", ".venv", "__pycache__", ".pytest_cache")):
                continue
            if path.suffix not in (".md", ".yaml", ".py", ".sh", ".json", ".yml"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            # Count real markers in content, not mentions in the docs that explain them.
            if path.parts[len(ROOT.parts)] in ("blocks", "tracks", "tutor") or path.name == "ROADMAP.md":
                verify += text.count("TODO(verify)")
            if "TODO(next-task)" in text and "blocks" in path.parts:
                mdir = next((p for p in path.parents if (p / "module.md").is_file()), None)
                if mdir and self.modules.get(mdir.name.split("-")[0], {}).get("status") == "ready":
                    self.r.error(path, "ready modules must not contain TODO(next-task)")
        self.todo_verify = verify


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    v = Validator()
    report = v.run()
    if not quiet:
        for w in report.warnings:
            print(f"warning: {w}")
    for e in report.errors:
        print(f"ERROR: {e}")
    print(
        f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s); "
        f"{len(v.blocks)} blocks, {len(v.modules)} module folders, {len(v.track_ids)} tracks; "
        f"{getattr(v, 'todo_verify', 0)} TODO(verify) marker(s)."
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
