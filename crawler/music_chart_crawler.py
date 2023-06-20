from abc import ABCMeta, abstractmethod

import requests
from bs4 import BeautifulSoup

from constant import USER_AGENT
from music.music import Music


class MusicChartCrawler(metaclass=ABCMeta):
    def __init__(self, chart_url, platform_name, crawl_url, parser_features="lxml"):
        self.parser = self._parse_chart_page(crawl_url, parser_features)

        self.chart_url = chart_url
        self.platform_name = platform_name
        self.top3 = self.get_top3_music_info()

    def _parse_chart_page(self, crawl_url, parser_features):
        chart_html_page = requests.get(crawl_url, headers=USER_AGENT)
        return BeautifulSoup(chart_html_page.text, parser_features)

    def get_top3_music_info(self):
        result = []

        top3 = self._extract_top3()
        for track in top3:
            title = self._get_title(track)
            artist = self._get_artist(track)
            album_cover_url = self._get_album_image_url(track)
            album_detail_url = self._get_album_detail_url(track)

            result.append(Music(title, artist, album_cover_url, album_detail_url))

        return result

    @abstractmethod
    def _extract_top3(self):
        pass

    @abstractmethod
    def _get_title(self, track):
        pass

    @abstractmethod
    def _get_artist(self, track):
        pass

    @abstractmethod
    def _get_album_image_url(self, track):
        pass

    @abstractmethod
    def _get_album_detail_url(self, track):
        pass
