from datetime import datetime, timedelta
import pytz
import logging
from enum import Enum


def get_logger(module_name: str, loggin_level=logging.INFO):
    logger = logging.getLogger(module_name)
    logger.setLevel(loggin_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(loggin_level)
    formatter = logging.Formatter(
        '%(module)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


class ClimbingArea(Enum):
    BOULDERING = 12
    INDOOR_LENGTH = 13
    OUTDOOR_LENGTH = 14

    @classmethod
    def get_by_name(cls, name: str):
        for key in cls:
            if key.name.lower() in name.lower().replace("-","_"):
                return key.value
        raise ValueError()

    @classmethod
    def names(cls):
        return list(val.name.lower().replace("_","-") for val in cls)

    @classmethod
    def values(cls):
        return list(val.value for val in cls)    