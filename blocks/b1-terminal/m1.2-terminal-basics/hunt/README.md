# B1 terminal scavenger hunt

Use **only the terminal** for this: no clicking in the file explorer, no editor, no AI. The explain-back will ask how you did each step.

Start here:

```bash
cd b1-hunt
ls
```

## Your tasks

Do them in any order. Check yourself at any time with `pytest b1-hunt` from the repo root (or just `pytest` inside `b1-hunt/`).

1. **Build a camp.** Create these folders inside `b1-hunt/`:
   ```
   camp/
   ├── tents/
   └── supplies/
       ├── food/
       └── tools/
   ```
   *Hint:* `mkdir`. Can you make `supplies/food` in one command? (Check `mkdir --help` for `-p`.)
2. **Move the map.** Move `start/map.txt` into `camp/`, so it's `camp/map.txt` and no longer in `start/`.
3. **Copy the rules.** Copy `start/rules.txt` to `camp/tents/rules.txt`. The original must stay in `start/`.
4. **Rename the compass.** Move `start/compass-draft.txt` to `camp/supplies/tools/compass.txt` (moving and renaming are the same command).
5. **Delete the junk.** Remove `start/junk.tmp`. There's no recycle bin in the terminal, so check the name before you press Enter.
6. **Pack food.** Create `camp/supplies/food/list.txt` containing exactly three lines, `apples`, `bread`, `water`, in that order.
   *New trick:* `echo "apples" > list.txt` writes a line to a file (replacing what was there); `>>` adds a line to the end.
7. **Search the haystack.** Create `answers.txt` in `b1-hunt/` with these four lines, filling in the values:
   ```
   lantern: <path of the hidden file in haystack/, starting with haystack/>
   acorn: <path of the file in haystack/ that contains the words "golden acorn">
   txt_count: <how many .txt files there are in haystack/, including subfolders>
   camp_path: <the absolute path of your camp/ folder>
   ```
   *Hints:* hidden files start with a dot (`ls -a`, or `find`); `grep -r` searches inside files; `find haystack -name "*.txt"` lists files by name; `pwd` prints where you are. You can write the answers with `echo "..." >> answers.txt`.

When `pytest` shows all green, commit and open a PR (see your repo README). That's the B1 exit artefact.

**Don't** change `test_hunt.py` or the files in `haystack/`.
