import click
from calls import check_availability
import telegram_bot
from time import sleep, ctime
import logging
from lib.utils import get_logger
import os

AREA_ID = {"bouldering": 12, "indoor-length": 13, "outdoor-length": 14}
INTERVAL = 60

chat_id = os.environ["TELEGRAM_CHAT_ID"]
bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
logger = get_logger("topmonitor")


@click.command()
@click.option('--area',
              default="indoor-length",
              help=f'Climbing area: {", ".join(AREA_ID.keys())}')
@click.option('--date', default='today', help='date: yyyy-mm-dd')
@click.option('--start-at', default='18:30', help='Starting time hh:mm')
def monitor(area, date, start_at):
    """Monitor top logger for free slots"""
    nr_available_slots = -1
    tel_bot = telegram_bot.TelegramBot(bot_token)
    while True:
        updated_nr_available_slots = check_availability(
            AREA_ID[area], date, start_at)
        if nr_available_slots != updated_nr_available_slots:
            if updated_nr_available_slots == 0:
                ps = "No luck yet:("
            else:
                ps = "This is your chance!!"
            message: str = f"{updated_nr_available_slots} available slots for {date} at {start_at}\n{ps}"
            logger.info(message)
            tel_bot.send_message(f"{message}", chat_id=chat_id)
            nr_available_slots = updated_nr_available_slots
        sleep(INTERVAL)


if __name__ == '__main__':
    monitor()