#!/usr/bin/python2
"""
Imports
"""
from snakebite.client import Client


def deletedir(l):
    """
    Delete DIR
    """
    client = Client("localhost", 9000)

    try:
        for dir in l:
            client.delete([dir], recurse=True)
    except Exception:
        pass

if __name__ == "__main__":
    directories = ["/Betty", "/Betty/Holberton"]
    deletedir(directories)
