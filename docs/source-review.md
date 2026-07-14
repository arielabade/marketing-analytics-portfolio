# Source Review

Audited repositories with marketing signal:

- `valid`: product roadmap mentions landing pages, tracking, UTMs, Meta Ads, Google Ads, CAC and conversion comparability.
- `curatorship`: contains growth/marketing/AI curation workflows, but also scraped research outputs and usage-control material, so raw workspace outputs were not migrated.
- `portfolio`: contained an older portfolio description with SQL, analytics and LLM positioning; it was not copied because it also contained personal profile data.
- `growth`, `metrics`, `adsrecipes`: empty at audit time.

Decision: create a clean marketing analytics shell with executable KPI helpers and synthetic validation data, then use future sanitized campaign exports as cases.
