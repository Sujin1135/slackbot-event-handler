from src.message_form.message_response import MessageResponse


def get_response_by_text(text: str):
    for attr in MessageResponse:
        command = attr.name.lower()
        if command == text.lower():
            return attr.value

    # TODO: It has to change return value, because null type is incorrect to return
    return None