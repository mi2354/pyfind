# Pyfind

## Description

This is a pure Python implementation of the `find` utility that you all have in the linux terminal. This version includes the following features:
- Regex search
- Search based on file weight: more than X mb or less than Y mb
- Search based on last modification of the file: older than X or newer than Y

## Installation
Git clone the repository and just pip install it!

## Usage
Search for any file larger than 1GB in the downloads folder:
```bash
pyfind Downloads/ --min-size=1000
```
