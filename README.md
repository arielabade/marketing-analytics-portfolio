# Marketing Analytics Portfolio

Turning campaign behavior into structured performance decisions.

## Why this project exists

This repository is the digital behavior layer of Ariel Lima's portfolio. It organizes available source material around marketing analysis, campaign diagnostics and decision support.

## The decision this project supports

Given campaign or funnel data, identify what changed, what matters and what decision should be taken next.

## Current contents

- `src/marketing_analytics/kpis.py`: reusable KPI helpers for spend, conversions, CPA, ROAS and conversion rate.
- `data/sample_campaign_daily.csv`: synthetic campaign data used only for executable examples.
- `cases/campaign-diagnostics-template.md`: case format following Context -> Question -> Data -> Method -> Finding -> Decision -> Limitation.
- `docs/source-review.md`: what was found in the previous repositories and why only curated content was migrated.

## How to run

```bash
python -m pytest
```

## Part of a larger portfolio

This project is part of a portfolio focused on transforming behavioral signals into measurable decisions.

- Previous layer: `tracking-attribution-lab`
- Next layer: `paid-media-budget-optimizer`
- Portfolio overview: `arielabade`

## Limitations

The audited repositories did not contain a clean publishable campaign dataset. The included data is synthetic and exists only to validate the KPI code and documentation structure.
