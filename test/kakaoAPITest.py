from unittest import TestCase

from chart.melon import Melon
from kakao.talk import KakaoTalk


class KakaoAPITest(TestCase):
    def test_send_list_message_of_music_chart(self):
        '''
        melon chart message를 보내면 응답으로 200 OK를 보내야한다.
        '''
        kakao_talk = KakaoTalk()

        melon = Melon()

        result = kakao_talk.send_message_to_me(melon)

        self.assertEqual(200, result.status_code)
