import re

from chart.music_chart import MusicChart
from constant.url import MELON_CHART_URI, MELON_ALBUM_DETAIL_URI


class Melon(MusicChart):
    def __init__(self):
        super().__init__(
            chart_url=MELON_CHART_URI, platform_name="멜론", crawl_url=MELON_CHART_URI
        )

    def _extract_top3(self):
        return self.parser.select("tr.lst50")[:3]

    def _get_title(self, track):
        return track.select("div.wrap_song_info a")[0].text

    def _get_artist(self, track):
        return track.select("div.wrap_song_info a")[1].text

    def _get_album_image_url(self, track):
        return track.select("div.wrap img[src]")[0]["src"]

    def _get_album_detail_url(self, track):
        album_id = re.sub("\\D", "", track.select("div.ellipsis.rank03 a")[0]["href"])
        return f"{MELON_ALBUM_DETAIL_URI}{album_id}"
