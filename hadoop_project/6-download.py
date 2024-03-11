#!/usr/bin/python2
"""
Imports
"""
from snakebite.client import Client
import os


def download(l):
    """
    Download Dir
    """
    client = Client("localhost", 9000)

    try:
        for dir in l:
            client.copyToLocal([dir], '/tmp')
    except Exception:
        pass

if __name__ == "__main__":
    directories = ["/Betty", "/Betty/Holberton"]
    download(directories)
