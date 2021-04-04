from datetime import datetime, timedelta
import pytz
import logging


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