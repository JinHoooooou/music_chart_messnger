import json
import os

import requests

KAKAO_AUTH_HOST = "https://kauth.kakao.com"
TOKEN_URI = "/oauth/token"

KAKAO_API_HOST = "https://kapi.kakao.com"
MESSAGE_TO_ME_URI = "/v2/api/talk/memo/default/send"
ACCESS_TOKEN_INFO_URI = "/v1/user/access_token_info"


class KakaoTalk:
    def __init__(self):
        self.refresh_token = None
        self.client_id = None
        self._get_env_variable()

    def _get_env_variable(self):
        dir_path = os.path.dirname(__file__)
        filename = "env.json"

        with open(os.path.join(dir_path, filename), "r", encoding="utf-8") as file:
            env = json.load(file)
            self.refresh_token = env["refresh_token"]
            self.client_id = env["client_id"]

    def _refresh_refresh_token(self, refresh_token):
        dir_path = os.path.dirname(__file__)
        filename = "env.json"

        with open(os.path.join(dir_path, filename), "wr", encoding="utf-8") as file:
            env = json.load(file)
            env["refresh_token"] = refresh_token

            json.dump(env, file)

    def build_music_top3_list_message(self, chart):
        list_template = {
            "object_type": "list",
            "header_title": f"{chart.platform_name} 차트",
            "header_link": {
                "web_url": chart.chart_url,
                "mobile_web_url": chart.chart_url,
            },
            "contents": [
                {
                    "title": music.title,
                    "description": music.artist,
                    "image_url": music.album_cover_url,
                    "image_width": 640,
                    "image_height": 640,
                    "link": {
                        "web_url": music.album_detail_url,
                        "mobile_web_url": music.album_detail_url,
                    },
                }
                for music in chart.top3
            ],
            "button_title": "차트로 이동",
        }

        return list_template

    def _get_access_token(self):
        url = KAKAO_AUTH_HOST + TOKEN_URI
        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": self.refresh_token
        }

        response = requests.post(url, headers=headers, data=data)

        response_body = json.loads(response.content.decode("utf-8"))
        access_token = response_body["access_token"]

        if "refresh_token" in response_body:
            self._refresh_refresh_token(response_body["refresh_token"])

        return access_token

    def send_message_to_me(self, platform):
        url = KAKAO_API_HOST + MESSAGE_TO_ME_URI

        access_token = self._get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        template = self.build_music_top3_list_message(platform)
        data = {"template_object": json.dumps(template, ensure_ascii=False)}

        response = requests.post(url, data=data, headers=headers)

        return response
