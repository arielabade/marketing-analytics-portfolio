from marketing_analytics.kpis import CampaignMetrics, summarize_campaigns


def test_summarize_campaigns():
    rows = [
        CampaignMetrics("A", spend=100, revenue=300, conversions=5, clicks=100),
        CampaignMetrics("B", spend=50, revenue=60, conversions=1, clicks=50),
    ]
    summary = summarize_campaigns(rows)
    assert summary["spend"] == 150
    assert summary["cpa"] == 25
    assert summary["roas"] == 2.4
