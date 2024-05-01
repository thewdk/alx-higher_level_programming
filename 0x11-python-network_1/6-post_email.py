#!/usr/bin/python3
"""
initialize the process
"""
from sys import argv
import requests


def alx_post_email():
    """ Sends a POST request
        to the passed URL with the email as a
        parameter, and finally displays the body of the response.
    """
    mailData = {'email': argv[2]}
    response = requests.post(argv[1], data=mailData)
    print(response.text)


if __name__ == '__main__':
    alx_post_email()
