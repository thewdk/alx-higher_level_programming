#!/usr/bin/python3
"""
initialize the process
"""
from sys import argv
import requests


def alx_header():
    """
    A Script that fetches url and gets X-Request-Id.
    """
    reqFor = requests.get(argv[1])
    print(reqFor.headers.get('X-Request-Id'))


if __name__ == '__main__':
    alx_header()
