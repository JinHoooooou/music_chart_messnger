from unittest import TestCase
from unittest.mock import patch

from crawler.flo import FloChartCrawler
from crawler.genie import GenieChartCrawler
from crawler.melon import MelonChartCrawler
from crawler.vibe import VibeChartCrawler
from test.mock import mock_top3
from constant.url import MELON_CHART_URI, GENIE_CHART_URI, FLO_CHART_URI, VIBE_CHART_URI


class CrawlerTest(TestCase):
    @patch(
        "crawler.music_chart_crawler.MusicChartCrawler.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_melon_chart_crawler(self, mock_music):
        # Given: MelonChartCrawler의 top3를 모킹

        # When: MelonChartCrawler가 주어진다.
        melon_chart_crawler = MelonChartCrawler()

        # Then: platform_name은 "멜론"이다.
        self.assertEqual("멜론", melon_chart_crawler.platform_name)
        # And: chart_url은 MELON_CHART_URI와 같다.
        self.assertEqual(MELON_CHART_URI, melon_chart_crawler.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(melon_chart_crawler.top3, mock_top3)

    @patch(
        "crawler.music_chart_crawler.MusicChartCrawler.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_genie_chart_crawler(self, mock_music):
        # Given: GenieChartCrawler의 top3를 모킹

        # When: GenieChartCrawler가 주어진다.
        genie_chart_crawler = GenieChartCrawler()

        # Then: platform_name은 "지니"이다.
        self.assertEqual("지니", genie_chart_crawler.platform_name)
        # And: chart_url은 GENIE_CHART_URI와 같다.
        self.assertEqual(GENIE_CHART_URI, genie_chart_crawler.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(genie_chart_crawler.top3, mock_top3)

    @patch(
        "crawler.music_chart_crawler.MusicChartCrawler.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_flo_chart_crawler(self, mock_music):
        # Given: FloChartCrawler의 top3를 모킹

        # When: FloChartCrawler가 주어진다.
        flo_chart_crawler = FloChartCrawler()

        # Then: platform_name은 "플로"이다.
        self.assertEqual("플로", flo_chart_crawler.platform_name)
        # And: chart_url은 FLO_CHART_URI와 같다.
        self.assertEqual(FLO_CHART_URI, flo_chart_crawler.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(flo_chart_crawler.top3, mock_top3)

    @patch(
        "crawler.music_chart_crawler.MusicChartCrawler.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_vibe_chart_crawler(self, mock_music):
        # Given: VibeChartCrawler의 top3를 모킹

        # When: VibeChartCrawler가 주어진다.
        vibe_chart_crawler = VibeChartCrawler()

        # Then: platform_name은 "바이브"이다.
        self.assertEqual("바이브", vibe_chart_crawler.platform_name)
        # And: chart_url은 VIBE_CHART_URI와 같다.
        self.assertEqual(VIBE_CHART_URI, vibe_chart_crawler.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(vibe_chart_crawler.top3, mock_top3)
