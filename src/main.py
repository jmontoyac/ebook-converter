import sys
import logging
from utils.argparser import *
from core.read_files.read_input_file import *


SUCCESSFUL_RUN = 0
FAILED_RUN = 1
LOGGER_FORMAT_STRING = (
    '%(asctime)s [%(levelname)-5s] [%(filename)s]-[%(lineno)-3d] %(message)s'
)
logging.basicConfig(
    level=logging.INFO, format=LOGGER_FORMAT_STRING, datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(__file__)


def main(arguments) -> bool:
    result = True
    try:
        args = vars(parse_arguments(arguments))
        print(f'Args: {args}')
        
        # Open pdf file
        #read_file(args['input_file'])
        get_images(args['input_file'])
        
    except argparse.ArgumentError as error:
        print(f'Error: {error}')
        result = False
    return result


if __name__ == '__main__':
    sys.exit(SUCCESSFUL_RUN if main(sys.argv[1:]) else FAILED_RUN)