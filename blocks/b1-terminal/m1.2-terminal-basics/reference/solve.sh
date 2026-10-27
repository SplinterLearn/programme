#!/usr/bin/env bash
# Reference solution for the B1 hunt. Used only by scripts/check_checkpoints.py
# to prove the hunt checker is passable. It is NOT copied into student repos.
# Run from inside a copy of hunt/ (named b1-hunt/).
set -euo pipefail

mkdir -p camp/tents camp/supplies/food camp/supplies/tools
mv start/map.txt camp/
cp start/rules.txt camp/tents/rules.txt
mv start/compass-draft.txt camp/supplies/tools/compass.txt
rm start/junk.tmp

echo "apples" > camp/supplies/food/list.txt
echo "bread" >> camp/supplies/food/list.txt
echo "water" >> camp/supplies/food/list.txt

{
  echo "lantern: $(find haystack -name '.*' -type f)"
  echo "acorn: $(grep -rl 'golden acorn' haystack)"
  echo "txt_count: $(find haystack -name '*.txt' | wc -l)"
  echo "camp_path: $(cd camp && pwd)"
} > answers.txt
