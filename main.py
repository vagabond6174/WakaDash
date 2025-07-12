from src.wakatime import WakaTimeClient
from src.graph import plot_language_usage


waka = WakaTimeClient()
plot_language_usage(
    waka.start_date.strftime("%d %B %Y"),
    waka.end_date.strftime("%d %B %Y"),
    waka.total_time_spent,
    waka.languages(),
)
