import os

from pyfind.config import Config, get_parser
from pyfind.filter_files import start_searching


def main():
    parser = get_parser()
    args = parser.parse_args()

    config = Config.build_config_from_arguments(args)

    start_searching(config)


if __name__ == "__main__":
    main()
