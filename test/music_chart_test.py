from unittest import TestCase
from unittest.mock import patch

from chart.flo import Flo
from chart.genie import Genie
from chart.melon import Melon
from chart.vibe import Vibe
from test.mock import mock_top3
from constant.url import MELON_CHART_URI, GENIE_CHART_URI, FLO_CHART_URI, VIBE_CHART_URI


class CrawlerTest(TestCase):
    @patch(
        "chart.music_chart.MusicChart.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_melon_chart(self, mock_music):
        # Given: MelonChart의 top3를 모킹

        # When: MelonChart가 주어진다.
        melon_chart = Melon()

        # Then: platform_name은 "멜론"이다.
        self.assertEqual("멜론", melon_chart.platform_name)
        # And: chart_url은 MELON_CHART_URI와 같다.
        self.assertEqual(MELON_CHART_URI, melon_chart.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(melon_chart.top3, mock_top3)

    @patch(
        "chart.music_chart.MusicChart.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_genie_chart_crawler(self, mock_music):
        # Given: GenieChart의 top3를 모킹

        # When: GenieChart 주어진다.
        genie_chart = Genie()

        # Then: platform_name은 "지니"이다.
        self.assertEqual("지니", genie_chart.platform_name)
        # And: chart_url은 GENIE_CHART_URI와 같다.
        self.assertEqual(GENIE_CHART_URI, genie_chart.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(genie_chart.top3, mock_top3)

    @patch(
        "chart.music_chart.MusicChart.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_flo_chart_crawler(self, mock_music):
        # Given: FloChart의 top3를 모킹

        # When: FloChart가 주어진다.
        flo_chart = Flo()

        # Then: platform_name은 "플로"이다.
        self.assertEqual("플로", flo_chart.platform_name)
        # And: chart_url은 FLO_CHART_URI와 같다.
        self.assertEqual(FLO_CHART_URI, flo_chart.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(flo_chart.top3, mock_top3)

    @patch(
        "chart.music_chart.MusicChart.get_top3_music_info",
        return_value=mock_top3,
    )
    def test_vibe_chart_crawler(self, mock_music):
        # Given: VibeChart의 top3를 모킹

        # When: VibeChart가 주어진다.
        vibe_chart = Vibe()

        # Then: platform_name은 "바이브"이다.
        self.assertEqual("바이브", vibe_chart.platform_name)
        # And: chart_url은 VIBE_CHART_URI와 같다.
        self.assertEqual(VIBE_CHART_URI, vibe_chart.chart_url)
        # And: top3는 Music객체 3개이고 각 title, artist, album_cover_url, album_detail_url을 가지고 있어야한다.
        self.assertEqual(vibe_chart.top3, mock_top3)
