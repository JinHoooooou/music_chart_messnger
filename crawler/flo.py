import json

from crawler.music_chart_crawler import MusicChartCrawler
from constant.url import FLO_ALBUM_DETAIL_URI, FLO_CHART_URI, FLO_CHART_API


class FloChartCrawler(MusicChartCrawler):
    def __init__(self):
        super().__init__(
            chart_url=FLO_CHART_URI, platform_name="플로", crawl_url=FLO_CHART_API
        )

    def _decode(self, encrypted_id):
        decode = ""
        for digit in encrypted_id:
            if digit == "0":
                decode += "d"
            elif digit == "1":
                decode += "a"
            elif digit == "2":
                decode += "n"
            elif digit == "3":
                decode += "i"
            elif digit == "4":
                decode += "e"
            elif digit == "5":
                decode += "l"
            elif digit == "6":
                decode += "z"
            elif digit == "7":
                decode += "o"
            elif digit == "8":
                decode += "h"
            elif digit == "9":
                decode += "y"
        return decode

    def _extract_top3(self):
        return json.loads(self.parser.select("p")[0].text)["data"]["trackList"][:3]

    def _get_title(self, track):
        return track["name"]

    def _get_artist(self, track):
        return track["representationArtist"]["name"]

    def _get_album_image_url(self, track):
        return track["album"]["imgList"][1]["url"]

    def _get_album_detail_url(self, track):
        album_id = self._decode(str(track["album"]["id"]))

        return f"{FLO_ALBUM_DETAIL_URI}{album_id}/albumtrack"
