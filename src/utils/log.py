import logging

LOGGER_FORMAT_STRING = (
    '%(asctime)s [%(levelname)-5s] [%(filename)s]-[%(lineno)-3d] %(message)s'
)
logging.basicConfig(
    level=logging.INFO, format=LOGGER_FORMAT_STRING,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(__file__)
