# Interest tracks

A track is the student's theme for the year. In months 1–4 it decides the remix variant; from month 5 it becomes dedicated project work (Block 7). See [ADR 0010](../docs/decisions/0010-staged-personalisation.md).

Each `<id>.md` has frontmatter (`schema/track.schema.json`) and a body describing the track's direction through the blocks. `status`: `ready-for-pilot` (prepared for the first students), `draft` (outline), `ready`.

A student can change track at a block boundary. Their block project stays; the next remix uses the new theme.
