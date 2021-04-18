import requests
import datetime
import os
import re
from datetime import datetime, timedelta
import logging
from enum import Enum
from lib.utils import ClimbingArea

logger = logging.getLogger('api-calls')
URL = os.environ.get("URL")


def call(date: str, area: str):
    """Call API to get availability per date and per area

    Args:
        date (str): date today/tomorrow or yyy-mm-dd
        area (str): area name, names of ClimbingArea enum

    Returns:
        [type]: [description]
    """
    date = _format_date(date)
    headers = {
        'content-type': 'application/json',
    }
    params = {
        "reservation_area_id": ClimbingArea.get_by_name(area),
        "date": date,
        "slim": True
    }
    r = requests.get(URL, params=params, headers=headers)
    r.raise_for_status()
    return r.json()


def _format_date(date: str):
    if date == "today":
        return f"{datetime.now():%Y-%m-%d}"
    if date == "tomorrow":
        return f"{datetime.now()+timedelta(days=1):%Y-%m-%d}"
    date = re.search(r"\d{4}-\d{2}-\d{2}", date)
    if not date:
        raise ValueError(
            f"Unexpected date format {date}. Required format yyyy-mm-dd")
    return date.group()


def get_slot_availability(area: int, date: str, time_slots: list):
    """ Check slots availability

    Args:
        area (int): [description]
        date (str): [description]
        time_slots (list): [description]
    """
    slots_data = call(date, area)
    available_time_slots = [
        re.search(r"T(\d\d:\d\d)", s["start_at"]).group(1) for s in slots_data
    ]
    slot_availability = {}

    if not time_slots:
        time_slots = available_time_slots

    for time_slot in set(time_slots):
        for slot in slots_data:
            if slot["start_at"].find(f"T{time_slot}") == -1:
                continue
            break
        else:
            msg = f"""Time slot at {time_slot} doesn't exsist on {date}.
                            Available time slots are {", ".join(available_time_slots)}
                """
            logger.error(msg)
            raise ValueError(msg)
        slot_availability[time_slot] = slot["spots"] - slot["spots_booked"]

    return slot_availability


def get_slots_schedule(date: str, area: str):

    slot_data = call(date, area)
    slots = {}
    for slot in slot_data:
        starts_at = re.search(r"T(\d\d:\d\d)", slot["start_at"]).group(1)
        slots[starts_at] = slot["spots"] - slot["spots_booked"]
    return slots
