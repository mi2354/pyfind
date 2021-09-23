from pyfind.filter_files import (
    FileInfo,
    _condition_multiple,
    _condition_name,
    file_meets_conditions,
)
from pyfind.main import Config


def test_condition_name():
    filename = "file1.txt"

    assert _condition_name(filename, "file1*")  # Regex works
    assert not _condition_name(filename, "file1")  # wrong regex, should not match only substring
    assert _condition_name(filename, "file1.txt")  # Full name should match
    assert not _condition_name(filename, "File1.txt")  # Case sensitive


def test_condition_multiple():
    assert _condition_multiple(1, 3, 0)


def test_file_meets_conditions():
    file_info = FileInfo("file1.txt", 5500, 1632462450)
    c = Config(None)
    c.name = "file1*"
    c.max_size = 6000
    c.min_size = 5000
    assert file_meets_conditions(file_info, c)
