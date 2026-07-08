# obx-guide

Static site for **guide.obx.deals** — a town-by-town OBX area guide.
Part of the `obx.deals` network (see `tiddnet/rental-intel` ADR 0215,
which supersedes ADR 0053's stale Streamlit-based design).

Plain static HTML, no build step, hosted on GitHub Pages. Custom domain
via `CNAME` file + Route53 CNAME record (`terraform/main.tf` in
`rental-intel`).

## Structure

- `index.html` — landing page, towns grouped by region
- One folder per town (`corolla/`, `duck/`, ... `ocracoke/`) — profile
  page: tagline, character, best-for/not-ideal-for, real access facts,
  real data (rental count, distance, size range, rate range)

## Data

Per-town stats (rental count, distance from Nags Head, bedroom range,
rate range) are pulled from `rental_intel.db`/`search.db` at generation
time — real, not invented. Distance is straight-line (haversine), not a
routed drive time, and labeled as such. Copy (tagline/character/best-for)
drafted by Claude Fable, grounded in the same real data — no invented
statistics or named businesses.

## Updating

Hand-maintained (not auto-regenerated) — see ADR 0215 for what's
deferred (the 20-question FAQ set, in-search community cards). Edit
HTML directly, commit, push; GitHub Pages redeploys automatically.
