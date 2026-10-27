---
module: m2.5
step: 5
---
# M2.5 remix: step 5, real data from an API (draft)

Split fetching (network) from logic (pure functions), so the logic can be tested without the internet. TODO(next-task): final spec and tests with mocked responses.

## Track: finance

**Brief.** The thing you want costs money in another currency. Use today's exchange rate.

**Spec sketch** (`savings.py`):
- `rate_from_json(data, currency) -> float`: reads the rate out of a Frankfurter-style JSON response (a dict). Planned test `test_reads_json`, with a saved example response.
- `fetch_rate(base, target) -> float | None`: calls the API with `requests`; returns `None` if the request fails. Planned test `test_handles_failure`, with the network mocked.
- `main()` converts the price, then runs the M2.1–M2.4 planner.

## Track: fandom

**Brief.** Stop typing episode counts: get them from the anime database.

**Spec sketch** (`watchlist.py`):
- `episodes_from_json(data) -> int | None`: reads `data["episodes"]` from a Jikan `/anime/{id}` response; `None` if missing (airing shows can have no count). Planned test `test_reads_json`.
- `fetch_anime(anime_id) -> dict | None`: calls `https://api.jikan.moe/v4/anime/{id}`; returns `None` on failure or rate limit. Planned test `test_handles_failure`.
- `main()` asks for an anime id and episodes watched, then plans the rest.
