import os
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

SCALE_MB_TO_B = 1024 * 1024


def get_parser():
    parser = ArgumentParser(description="Find files in your system.")
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        help="Path to start searching, defaults to current directory",
        default=os.getcwd(),
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        nargs="?",
        help="Filename to search",
    )
    parser.add_argument(
        "--min-modified-time",
        type=str,
        help="The minimum value for the modification time of the file",
    )
    parser.add_argument(
        "--max-modified-time",
        type=str,
        help="The maximum value for the modification time of the file",
    )
    parser.add_argument(
        "--max-size",
        type=int,
        help="The maximum filesize in MB",
    )
    parser.add_argument(
        "--min-size",
        type=int,
        help="The minimum filesize in MB",
    )
    parser.add_argument(
        "--depth",
        type=int,
        help="The depth limit for the search. If not provided, no limit will be applied",
    )
    return parser


@dataclass
class Config:
    path: str = None
    name: str = None
    mtime_max: int = None
    mtime_min: int = None
    max_size: int = None
    min_size: int = None
    depth: int = None

    @staticmethod
    def _strdate_to_unix_time(date: Optional[str]) -> Optional[str]:
        if date is None:
            return date
        try:
            date_object = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print(
                f"Failed to parse date {date}. Make sure it has format DD-MM-YYYY\n"
                f"Ignoring date {date}"
            )
            return None
        else:
            return date_object.timestamp()

    @staticmethod
    def _update_size_to_bytes(size: Optional[int]) -> Optional[int]:
        return size * SCALE_MB_TO_B if size is not None else None

    @classmethod
    def build_config_from_arguments(cls, arguments: Namespace):
        print(arguments)
        return cls(
            path=arguments.path,
            name=arguments.name,
            mtime_max=cls._strdate_to_unix_time(arguments.max_modified_time),
            mtime_min=cls._strdate_to_unix_time(arguments.min_modified_time),
            max_size=cls._update_size_to_bytes(arguments.max_size),
            min_size=cls._update_size_to_bytes(arguments.min_size),
            depth=arguments.depth,
        )
