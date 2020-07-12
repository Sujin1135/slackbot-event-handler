import os

from slack import WebClient


class Sender(object):
    def __init__(self, channel: str):
        token = os.environ['SLACK_API_TOKEN']
        self.web_client = WebClient(token=token)
        self.channel = channel

    def open_user(self, user_id: str):
        self.web_client.im_open(user=user_id)

    def send_message(self, *message: dict):
        message_request = self._make_message(*message)
        self.web_client.chat_postMessage(**message_request)

    def _make_message(self, *message: dict):
        return {
            "ts": "",
            "channel": self.channel,
            "username": "my bot",
            "icon_emoji": ":robot_face:",
            "blocks": [*message]
        }
