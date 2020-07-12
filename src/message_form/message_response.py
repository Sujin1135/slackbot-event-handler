from enum import Enum

from src.message_form.get_message_form import get_message_form


class MessageResponse(Enum):
    WELCOME = get_message_form('welcome')
