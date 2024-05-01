#!/usr/bin/python3
"""
initialize the process
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def task_post_email():
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('utf-8')
    reqFor = Request(url, data)
    with urlopen(reqFor) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    task_post_email()
