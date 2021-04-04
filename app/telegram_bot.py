from datetime import datetime
import pytz
import requests

import logging

logger = logging.getLogger('telegram_bot')

class TelegramBot(object):
    def __init__(self, bot_token: str):
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, message: str, chat_id: str):
        response = requests.post(
            self.base_url + "/sendMessage", data={'chat_id': chat_id, 'text': message})
        try:
            response.raise_for_status()
            logger.info(f"Message sent to the chat {chat_id}")
        except BaseException as err:
            logger.error(response.status_code, response.text)
            raise err

    def read_messages(chat_id: str):
        response = requests.get(self.base_url + "/getUpdates")
        updates = response.json()
        try:
            response.raise_for_status()
            logger.info(f"Failed to receive updates")
        except BaseException as err:
            logger.error(response.status_code, response.text)
            raise err