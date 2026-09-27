import logging
logging.basicConfig(level=logging.INFO)
try:
    1/0
except ZeroDivisionError:
    logging.exception("calculation failed")
