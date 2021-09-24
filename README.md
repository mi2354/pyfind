# Pyfind

This is a pure Python implementation of the `find` utility that you all have in the linux terminal. This version includes the following features:
- Regex search
- Search based on file weight: more than X mb or less than Y mb
- Search based on last modification of the file: older than X or newer than Y

## Installation
Git clone the repository and just pip install it!

## Usage
Search for any file larger than 1GB in the downloads folder:
```bash
$ pyfind Downloads/ --min-size=1000
```

Check all the possibilities:
```bash
$ pyfind --help
usage: pyfind [-h] [-n [NAME]] [--min-modified-time MIN_MODIFIED_TIME] [--max-modified-time MAX_MODIFIED_TIME] [--max-size MAX_SIZE]
              [--min-size MIN_SIZE] [--depth DEPTH]
              [path]

Find files in your system.

positional arguments:
  path                  Path to start searching, defaults to current directory

options:
  -h, --help            show this help message and exit
  -n [NAME], --name [NAME]
                        Filename to search
  --min-modified-time MIN_MODIFIED_TIME
                        The minimum value for the modification time of the file
  --max-modified-time MAX_MODIFIED_TIME
                        The maximum value for the modification time of the file
  --max-size MAX_SIZE   The maximum filesize in MB
  --min-size MIN_SIZE   The minimum filesize in MB
  --depth DEPTH         The depth limit for the search. If not provided, no limit will be applied
```
