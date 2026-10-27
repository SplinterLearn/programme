#!/usr/bin/env bash
# Stage a merge conflict in a scratch git repo, for the B3 skip test.
#
#   bash stage_conflict.sh [DIR]          create DIR (default: ./conflict-practice)
#                                         and leave a merge conflict to resolve
#   bash stage_conflict.sh --check [DIR]  check the resolution
#
# The scratch repo is local only: no remote, nothing is pushed. Teammates'
# commits use made-up example.com identities; the merge commit is yours.
set -euo pipefail

FILE="trip-plan.md"
AGREED="Leave at: 09:30"

check() {
  local dir="$1" ok=1
  cd "$dir" 2>/dev/null || { echo "FAIL: $dir doesn't exist"; exit 1; }
  if [ -f .git/MERGE_HEAD ]; then
    echo "FAIL: the merge isn't finished yet (commit it after resolving)"; ok=0
  fi
  if grep -nE '^(<<<<<<<|=======|>>>>>>>)' "$FILE" >/dev/null; then
    echo "FAIL: conflict markers are still in $FILE:"; grep -nE '^(<<<<<<<|=======|>>>>>>>)' "$FILE"; ok=0
  fi
  if ! grep -qx "$AGREED" "$FILE"; then
    echo "FAIL: the leave time isn't the one the team agreed on (see NOTES.md)"; ok=0
  fi
  if [ "$(grep -c '^Leave at:' "$FILE")" != "1" ]; then
    echo "FAIL: there should be exactly one 'Leave at:' line"; ok=0
  fi
  grep -qx "Bring: water, sandwiches, rain jacket" "$FILE" || { echo "FAIL: the packing change from main was lost"; ok=0; }
  grep -qx "Meet at: the north gate" "$FILE" || { echo "FAIL: the meeting-point change from teammate-branch was lost"; ok=0; }
  if ! git log -1 --pretty=%P | grep -q ' '; then
    echo "FAIL: the last commit isn't a merge commit"; ok=0
  fi
  if [ "$ok" = 1 ]; then
    echo "PASS: conflict resolved as agreed, both teammates' other changes kept, merge committed."
    echo "Merge commit: $(git log -1 --pretty='%h %s')"
  else
    exit 1
  fi
}

if [ "${1:-}" = "--check" ]; then
  check "${2:-conflict-practice}"
  exit 0
fi

DIR="${1:-conflict-practice}"
if [ -e "$DIR" ]; then
  echo "$DIR already exists. Pick a new folder name or delete it first." >&2
  exit 1
fi

mkdir -p "$DIR"
cd "$DIR"
git init -q -b main
as_alex() { git -c user.name="Teammate Alex" -c user.email="alex@example.com" "$@"; }
as_kim() { git -c user.name="Teammate Kim" -c user.email="kim@example.com" "$@"; }

cat > "$FILE" <<'EOF'
# Club hiking trip

Meet at: the car park

Route: the lake loop (about 8 km)

Leave at: 10:00

Back by: 17:00

Bring: water, sandwiches
EOF
cat > NOTES.md <<'EOF'
# Team decisions

- 2026-05-02: The bus timetable changed. We agreed to **leave at 09:30**.
- 2026-05-03: Kim is updating the meeting point; Alex is updating the packing list.
EOF
as_alex add -A
as_alex commit -q -m "Start the trip plan"

git switch -q -c teammate-branch
sed -i.bak -e 's/^Meet at: .*/Meet at: the north gate/' -e 's/^Leave at: .*/Leave at: 09:30/' "$FILE" && rm -f "$FILE.bak"
as_kim commit -q -am "Move meeting point to the north gate; leave at 09:30"

git switch -q main
sed -i.bak -e 's/^Bring: .*/Bring: water, sandwiches, rain jacket/' -e 's/^Leave at: .*/Leave at: 10:15/' "$FILE" && rm -f "$FILE.bak"
as_alex commit -q -am "Add rain jacket; push leave time to 10:15"

set +e
git merge teammate-branch >/dev/null 2>&1
set -e

echo "A merge conflict is waiting in $(pwd)"
echo
git status --short
echo
echo "Next:"
echo "  1. cd $DIR and open $FILE. Read NOTES.md: what did the team agree?"
echo "  2. Edit $FILE: keep the right lines, remove every <<<<<<<, ======= and >>>>>>> line."
echo "  3. git add $FILE && git commit   (this finishes the merge)"
echo "  4. bash $0 --check $DIR"
