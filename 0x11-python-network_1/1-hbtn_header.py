#!/usr/bin/python3
"""
Reply header value
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    reqFor = urllib.request.Request(url)

    with urllib.request.urlopen(reqFor) as response:
        requestId = response.headers.get('X-Request-Id')

    print(requestId)
