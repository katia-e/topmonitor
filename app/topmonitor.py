import click
from calls import get_slot_availability, get_slots_schedule
import telegram_bot
from time import sleep, ctime
import logging
from lib.utils import get_logger
import os
from lib.utils import ClimbingArea
import yaml
import re

chat_id = os.environ.get("TELEGRAM_CHAT_ID")
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
logger = get_logger("topmonitor")


@click.group(invoke_without_command=True)
@click.option('--area',
              default="outdoor",
              help=f'Climbing area: {ClimbingArea.names()}')
@click.option('--date',
              default='today',
              help='Date: yyyy-mm-dd or today/tomorrow, default: today')
@click.option(
    '--slots',
    default=[],
    help=
    'List of slots to monitor, format: hh:mm, default: all time slots will be monitored'
)
@click.option('--pooling-interval',
              default=60,
              help='Time interval between calls, default 60s')
@click.pass_context
def monitor(ctx, date: str, area: str, slots: list, pooling_interval: int):
    """Monitor top logger for free slots"""
    if not ctx.invoked_subcommand:
        if slots:
            slots = re.split(r",|;|\.| ", slots)
        nr_available_slots = {}
        tel_bot = telegram_bot.TelegramBot(bot_token)
        tel_bot.send_message(
            f"Topminitor is running. Request {area} {date} {slots if slots else 'all slots'} ",
            chat_id=chat_id)
        while True:
            updated_nr_available_slots = get_slot_availability(
                area, date, slots)
            for slot in updated_nr_available_slots.keys():
                if nr_available_slots.get(
                        slot, 0) != updated_nr_available_slots[slot]:
                    if updated_nr_available_slots[slot] == 0:
                        ps = "No luck yet:("
                    else:
                        ps = "This is your chance!!"
                    message: str = f"{updated_nr_available_slots[slot]} available slots for {date} at {slot}\n{ps}"
                    logger.info(message)
                    tel_bot.send_message(f"{message}", chat_id=chat_id)
            nr_available_slots = updated_nr_available_slots
            sleep(pooling_interval)


@monitor.command()
@click.option('--date',
              default='123',
              help='date: yyyy-mm-dd or today/tomorrow')
@click.option('--area',
              default="outdoor",
              help=f'Climbing area: {ClimbingArea.names()}')
def list_slots(date: str, area: str):
    print(yaml.dump(get_slots_schedule(date, area)))


if __name__ == '__main__':
    monitor()
