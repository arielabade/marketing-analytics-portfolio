from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CampaignMetrics:
    campaign: str
    spend: float
    revenue: float
    conversions: int
    clicks: int

    @property
    def cpa(self) -> float | None:
        return None if self.conversions == 0 else self.spend / self.conversions

    @property
    def roas(self) -> float | None:
        return None if self.spend == 0 else self.revenue / self.spend

    @property
    def conversion_rate(self) -> float | None:
        return None if self.clicks == 0 else self.conversions / self.clicks


def summarize_campaigns(rows: list[CampaignMetrics]) -> dict[str, float | int | None]:
    spend = sum(row.spend for row in rows)
    revenue = sum(row.revenue for row in rows)
    conversions = sum(row.conversions for row in rows)
    clicks = sum(row.clicks for row in rows)
    return {
        "spend": round(spend, 2),
        "revenue": round(revenue, 2),
        "conversions": conversions,
        "clicks": clicks,
        "cpa": None if conversions == 0 else round(spend / conversions, 2),
        "roas": None if spend == 0 else round(revenue / spend, 2),
        "conversion_rate": None if clicks == 0 else round(conversions / clicks, 4),
    }
