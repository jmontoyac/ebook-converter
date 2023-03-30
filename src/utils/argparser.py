import argparse

def parse_arguments(arguments):
    parser = argparse.ArgumentParser(description=
                                     'ebook file format converter'
                                     )
    parser.add_argument(
        '--input_file',
        '-i',
        type=str,
        required=True,
        #choices='source_file.pdf',
        help='Source file, i.e. file.pdf'
    )
    parser.add_argument(
        '--output_file',
        '-o',
        type=str,
        required=True,
        #choices='destination_file.epub',
        help='Destination file, i.e. file.epub'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        default=False,
        action='store_true',
        help='Enables debug-level logging'
    )
    args = parser.parse_args(arguments)
    return args