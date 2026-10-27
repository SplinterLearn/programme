---
id: context
purpose: "Per-turn context appended after the system prompt, in cache-friendly order: module (layer 2), student profile (layer 3), session and conversation (layer 4). The student's message (layer 5) follows as the user turn."
model_tier: cheap
cache_layer: 2
placeholders: [module, remix, track, cs50_summaries, student_profile, mode, session, conversation_summary, recent_turns]
output_schema: null
---
<!-- layer 2: changes per module; cached -->
# Current module

{{module}}

## The student's remix (track: {{track}})

{{remix}}

## CS50 problem sets in this block (for recognising them; one-line summaries in our own words)

{{cs50_summaries}}

<!-- layer 3: changes rarely; small -->
# Student profile

{{student_profile}}

<!-- layer 4: changes every turn -->
# This session

Mode: **{{mode}}**

{{session}}

## Conversation so far

Summary of earlier turns:
{{conversation_summary}}

Recent turns:
{{recent_turns}}
