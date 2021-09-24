import argparse
import os
import re
from dataclasses import dataclass
from typing import Generator, Optional

from pyfind.config import Config

FULL_PATTERN = re.compile(r"\w+")


@dataclass
class FileInfo:
    name: str
    size: float
    mtime: str


def get_file_info_object(path: str) -> FileInfo:
    stat = os.stat(path)
    filename = path.split("/")[-1]
    size_in_bytes = stat.st_size
    mtime = stat.st_mtime
    return FileInfo(filename, size_in_bytes, mtime)


def _condition_name(filename: str, config_pattern: Optional[str]) -> bool:
    """
    Check if the given pattern (word or regular expression) matches the word.

    Args:
        filename_pattern (str): The pattern to match against the word.
        word (str): The word to check if it matches the pattern.

    Returns:
        bool: True if the pattern matches the word, False otherwise.
    """
    if config_pattern is None:
        return True

    # If the pattern is an exact word
    if FULL_PATTERN.fullmatch(config_pattern):
        return config_pattern == filename

    # If the pattern is a regular expression
    match = re.match(config_pattern, filename)
    return bool(match)


def _condition_multiple(
    file_attribute: int, config_max: Optional[int], config_min: Optional[int]
) -> bool:
    return (config_max is None or config_max >= file_attribute) and (
        config_min is None or config_min <= file_attribute
    )


def file_meets_conditions(file_info: FileInfo, config: Config) -> bool:
    return (
        _condition_name(file_info.name, config.name)
        and _condition_multiple(file_info.mtime, config.mtime_max, config.mtime_min)
        and _condition_multiple(file_info.size, config.max_size, config.min_size)
    )


def get_filepaths_recursively_os(path: str, depth: int) -> Generator[str, None, None]:
    """
    Recursively retrieves files under the given path up to a specified depth.

    Args:
        path (str): The starting path from which to retrieve files.
        depth (int): The maximum depth of recursion to retrieve files. If set to 0,
                     only the files directly under the given path will be returned.

    Yields:
        str: The path of each file found.
    """
    if depth != 0:
        for element in os.scandir(path):
            if os.path.isfile(element):
                yield element.path
            elif os.path.isdir(element):
                yield from get_filepaths_recursively_os(
                    os.path.join(path, element.name), depth - 1
                )


def start_searching(config: argparse.Namespace) -> None:
    """
    Start searching for files based on the provided configuration.

    Args:
        config (argparse.Namespace): Configuration object containing search parameters.

    Returns:
        None
    """
    path = config.path
    depth = config.depth + 1 if config.depth is not None else -1

    results = []
    for filepath in get_filepaths_recursively_os(path, depth):
        file_info = get_file_info_object(filepath)
        if file_meets_conditions(file_info, config):
            results.append(filepath)
            print(filepath)
    return results
