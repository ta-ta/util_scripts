import argparse
import logging
import os
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    XXX をトリガーに呼ばれる
    """
    main()


def main():
    """
    main()
    """
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-e', '--env', help='', default='')
    args = parser.parse_args()
    env = args.env

    if env == '':
        parser.print_help()
        sys.exit()

    main()
