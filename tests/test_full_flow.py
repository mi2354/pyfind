import os

from pyfind.filter_files import FileInfo, start_searching
from pyfind.main import Config

SCRIPT_PATH = os.path.abspath(__file__)
FOLDER_PATH = os.path.dirname(SCRIPT_PATH)


def test_file_meets_conditions():
    c = Config(FOLDER_PATH, "file1.*")
    result = start_searching(c)
    assert len(result) == 1
    assert result[0].split("/")[-1] == "file1.txt"


def test_not_enough_depth():
    c = Config(FOLDER_PATH, "depth_file*", depth=1)
    result = start_searching(c)
    assert result == []
