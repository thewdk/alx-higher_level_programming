#!/usr/bin/python3
"""
initialize the process
"""
import requests


def data_status():
    """A Python script that fetches the Status"""

    data_request = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(data_request.text), data_request.text))


if __name__ == '__main__':
    data_status()
