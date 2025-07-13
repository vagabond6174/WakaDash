from src.wakatime import WakaTimeClient
from datetime import datetime, timedelta
from src.graph import plot_language_usage,plot_day_wise_summary_no_projects


waka = WakaTimeClient()

# Language stats
stats = waka.fetch_stats()

plot_language_usage(
    (datetime.strptime(stats["start"], "%Y-%m-%dT%H:%M:%SZ") + timedelta(days = 1)).strftime("%d %B %Y"),
    datetime.strptime(stats["end"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y"),
    stats['human_readable_total_including_other_language'],
    waka.languages(stats)
)

# Day wise data
day_wise_stats = waka.fetch_day_wise_summary()
plot_day_wise_summary_no_projects(day_wise_stats)
