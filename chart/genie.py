import re

from chart.music_chart import MusicChart
from constant.url import GENIE_CHART_URI, GENIE_ALBUM_DETAIL_URI


class Genie(MusicChart):
    def __init__(self):
        super().__init__(
            chart_url=GENIE_CHART_URI, platform_name="지니", crawl_url=GENIE_CHART_URI
        )

    def _extract_top3(self):
        return self.parser.select("tr.list")[:3]

    def _get_title(self, track):
        return track.select("a.title")[0].text.strip()

    def _get_artist(self, track):
        return track.select("a.artist")[0].text.strip()

    def _get_album_image_url(self, track):
        return f"https://{track.select('a.cover img')[0]['src'][2:-19]}"

    def _get_album_detail_url(self, track):
        album_id = re.sub("\\D", "", track.select("a.cover")[0]["onclick"])
        return f"{GENIE_ALBUM_DETAIL_URI}{album_id}"
