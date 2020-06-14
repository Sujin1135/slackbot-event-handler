import logging
import os

from flask import Flask

from src.event_handler import init_slack_app

app = Flask(__name__)
app.config['SLACK_SIGNING_SECRET'] = os.environ['SLACK_SIGNING_SECRET']
init_slack_app(app)


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run()


token = os.environ['SLACK_API_TOKEN']
