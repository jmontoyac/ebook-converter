'''
'''
import sys
from utils.argparser import parse_arguments
from utils.argparser import argparse
from utils.log import logger
from core.read_files.read_input_file import get_images, read_file


SUCCESSFUL_RUN = 0
FAILED_RUN = 1


def main(arguments) -> bool:
    '''
    Main function to process pdf file
    Args:
        arguments: Command line arguments
    Return:
        result (bool): Execution result
    '''
    result = True
    try:
        args = vars(parse_arguments(arguments))
        print(f'Args: {args}')

        # Open pdf file
        read_file(args['input_file'])
        get_images(args['input_file'])

    except argparse.ArgumentError as error:
        print(f'Error: {error}')
        logger.error('Error: %s', error)
        result = False
    return result


if __name__ == '__main__':
    sys.exit(SUCCESSFUL_RUN if main(sys.argv[1:]) else FAILED_RUN)