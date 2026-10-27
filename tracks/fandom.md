---
id: fandom
title: Fandom & anime data
summary: Anime and fandom data and community tools — watchlists, character databases, fan-site APIs and simple analytics.
example_projects:
  - "Watchlist planner: how long until I finish a series, then a whole sorted watchlist (Block 2 project)"
  - "Episode counts and ratings pulled live from a public anime API"
  - "A character database you can search and filter, stored in SQLite"
  - "Seasonal stats: which genres or studios a community watches most, with a chart"
  - "A small web page or bot that recommends what to watch next from your list"
extra_resources:
  - title: Jikan — unofficial MyAnimeList API (no key needed)
    url: https://jikan.moe/
    notes: "Used from M2.5. See the module for rate limits; cache responses and be polite."
    verified_on: 2026-10-27
  - title: AniList API docs (GraphQL)
    url: https://docs.anilist.co/
    notes: "Alternative API for later blocks; GraphQL is more advanced than REST."
    verified_on: 2026-10-27
status: ready-for-pilot
---
# Track: fandom

**For** students who live in anime, manga, games or any fandom and want to build tools for themselves and their community.

## Through the year

| When | What it looks like |
|---|---|
| Block 2 | **Watchlist planner** (`b2-watchlist/`): days to finish a series → day-by-day schedule → the whole watchlist sorted → survives bad input → real episode counts from Jikan |
| Block 4 | write your own tests for the planner; fix seeded bugs |
| Block 5 | store your list in SQLite; a small web page for it; deploy it |
| Block 6 | have a coding agent add a feature (e.g. "recommend next") from your spec, and review its diff |
| Block 7 | track project: e.g. a seasonal stats dashboard or a community tool |

## Good habits this track teaches
- APIs have **rate limits**: cache, wait, and never hammer a free service.
- Data from fan sites can be incomplete (e.g. episode counts for airing shows): handle missing values.
- Respect communities: no scraping of private data, and credit the sources.
