---
id: biology
title: Biology & science data
summary: Biology and science data — DNA strings, small bioinformatics problems in Python, and working with real public datasets.
example_projects:
  - "DNA toolkit: count bases, GC content, reverse complement, translate to protein"
  - "Solve the beginner Rosalind problems in Python, with your own tests"
  - "Plot a public dataset (e.g. species counts or experiment results) and explain what it shows"
  - "A small lab-notes app that stores experiments in SQLite"
extra_resources:
  - title: Rosalind — Python Village (beginner problems)
    url: https://rosalind.info/problems/list-view/?location=python-village
    notes: "Free bioinformatics problems with automatic checking. Python Village is the intro set; the Bioinformatics Stronghold comes after. Good from Block 2 on, especially with CS50P Lecture 7 (regex) as track content."
    verified_on: 2026-10-27
  - title: Biopython
    url: https://biopython.org/
    notes: "Library for later blocks (Block 7), once the basics are done by hand."
    verified_on: 2026-10-27
  - title: NCBI APIs
    url: https://www.ncbi.nlm.nih.gov/home/develop/api/
    notes: "Public biology data APIs for Block 5+. TODO(verify): which endpoints need a key and their rate limits before using them in a module."
    verified_on: 2026-10-27
status: ready-for-pilot
---
# Track: biology

**For** students drawn to living things, medicine, chemistry or any science, who want code to answer questions about real data.

## Through the year

| When | What it looks like |
|---|---|
| Block 2 | remix variants are written later (TODO(next-task)); until then use the **finance** spec with science nouns (e.g. "days until the culture reaches N cells"), or the closest tested track. Rosalind Python Village works as extra practice |
| Block 4 | tests for a DNA toolkit; regular expressions (CS50P Lecture 7) as track content |
| Block 5 | load a CSV dataset, store it in SQLite, chart it, put it on a small web page |
| Block 7 | track project: e.g. a sequence-analysis CLI or a dataset explorer |

## Good habits this track teaches
- Check your results against a known answer (Rosalind does this for you).
- Data has units and errors: write them down.
