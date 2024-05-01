#!/usr/bin/python3
"""Sends a POST request with a given letter.
"""
import sys
import requests


if __name__ == "__main__":
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    pload = {"q": let}

    r = requests.post("http://0.0.0.0:5000/search_user", data=pload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
