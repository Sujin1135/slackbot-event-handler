from enum import Enum


def get_response_by_text(text: str):
    for attr in MessageResponse:
        command = attr.name.lower()
        if command == text:
            return attr.value

    # TODO: It has to change return value, because null type is incorrect to return
    return None


class MessageResponse(Enum):
    # TODO: It'll return current weather by inputted city
    WEATHER = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to Slack! :wave: We're so glad you're here. :blush:\n\n"
                "*Get started by completing the steps below:*"
            ),
        }
    }
