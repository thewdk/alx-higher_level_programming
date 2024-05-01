#!/usr/bin/python3
"""
initialize process
"""
from sys import argv
from urllib.request import urlopen
from urllib.request import Request
import urllib.error


def task_error_code():
    url = argv[1]
    reqFor = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(reqFor) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == '__main__':
    task_error_code()
