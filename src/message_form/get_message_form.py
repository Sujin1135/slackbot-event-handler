import json
import os


def get_message_form(key: str):
    current_path = os.path.dirname(__file__)
    rel_path = "./json/{}.json".format(key)
    abs_file_path = os.path.join(current_path, rel_path)

    with open(abs_file_path, 'r') as json_file:
        json_data = json.load(json_file)

        return json_data