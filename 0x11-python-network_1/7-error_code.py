#!/usr/bin/python3
"""
initilize the process
"""
from sys import argv
import requests


def alx_error_code():
    """Script that fetches to url and get X-Request-Id."""
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == '__main__':
    alx_error_code()
