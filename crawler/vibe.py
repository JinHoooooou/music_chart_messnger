from crawler.music_chart_crawler import MusicChartCrawler
from constant.url import VIBE_ALBUM_DETAIL_URI, VIBE_CHART_URI, VIBE_CHART_API


class VibeChartCrawler(MusicChartCrawler):
    def __init__(self):
        super().__init__(
            chart_url=VIBE_CHART_URI,
            platform_name="바이브",
            crawl_url=VIBE_CHART_API,
            parser_features="lxml-xml",
        )

    def _extract_top3(self):
        return self.parser.select("track")[:3]

    def _get_title(self, track):
        return track.select("trackTitle")[0].text

    def _get_artist(self, track):
        return track.select("artistName")[0].text

    def _get_album_image_url(self, track):
        return track.select("imageUrl")[0].text

    def _get_album_detail_url(self, track):
        album_id = track.select("albumId")[0].text
        return f"{VIBE_ALBUM_DETAIL_URI}{album_id}"
