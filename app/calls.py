import requests
import datetime
import os

URL = os.environ.get("URL")


def check_availability(area, date, start_at):
    """ Check slots availability

    Args:
        area (str): [description]
        date (str): [description]
        start_at (str): [description]
    """
    headers = {
        'content-type': 'application/json',
    }
    params = {"reservation_area_id": area, "date": date, "slim": True}
    r = requests.get(URL, params=params, headers=headers)
    slots = r.json()
    for slot in slots:
        if slot["start_at"].find(f"T{start_at}") == -1:
            continue
        break
    else:
        raise RuntimeError(f"Timeslot {start_at} doesn't exist on {date}")
    return slot["spots"] - slot["spots_booked"]
