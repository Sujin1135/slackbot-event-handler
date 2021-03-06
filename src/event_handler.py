import os

from flask import Flask
from flask_slack import SlackManager

from src.message_form.get_response_by_text import get_response_by_text
from src.message_form.message_response import MessageResponse
from src.sender import Sender

token = os.environ['SLACK_API_TOKEN']
channel = os.environ['CHANNEL']
message_sender = Sender(channel)
slack_manager = SlackManager()


def init_slack_app(app: Flask):
    slack_manager.init_app(app)


@slack_manager.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    print(emoji)


@slack_manager.on("team_join")
def give_welcoming(sender, data, **extra):
    event = data['event']
    user_id = event.get("user", {}).get("id")
    message_sender.open_user(user_id)

    welcome_message = MessageResponse.WELCOME.value
    message_sender.send_message(welcome_message)


@slack_manager.on("message")
def send_message(sender, data, **extra):
    event = data['event']
    text = event.get("text")

    message = get_response_by_text(text)
    if message:
        message_sender.send_message(message)
