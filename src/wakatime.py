import requests
import os
from datetime import datetime


class WakaTimeClient:
    def __init__(self, api_key=None, range="last_7_days"):
        self.API_KEY = api_key or os.getenv("WAKATIME_API_KEY")
        self.STATS_RANGE = range

        if not self.API_KEY:
            raise ValueError("WAKATIME API KEY not found!")

        self._data = self._fetch_stats()

        self.start_date = datetime.strptime(self._data["start"], "%Y-%m-%dT%H:%M:%SZ")
        self.end_date = datetime.strptime(self._data["end"], "%Y-%m-%dT%H:%M:%SZ")
        self.total_time_spent = self._data[
            "human_readable_total_including_other_language"
        ]

    def _fetch_stats(self):
        response = requests.get(
            f"https://wakatime.com/api/v1/users/current/stats/{self.STATS_RANGE}?api_key={self.API_KEY}"
        )
        response.raise_for_status()
        return response.json()["data"]

    def languages(self, limit=5):
        return [
            (lang["name"], lang["percent"], lang["text"])
            for lang in self._data.get("languages", [])[:limit]
        ]
