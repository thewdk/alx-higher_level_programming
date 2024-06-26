#!/usr/bin/python3
"""
Fetches resources.
"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        code = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(code)))
        print("\t- content: {}".format(code))
        print("\t- utf8 content: {}".format(code.decode("utf-8")))
