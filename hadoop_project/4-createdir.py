#!/usr/bin/python2
"""
Imports
"""
from snakebite.client import Client


def createdir(l):
    """
    Create DIR
    """
    client = Client("localhost", 9000)

    for dir in l:
        client.mkdir([dir], create_parent=True)

if __name__ == "__main__":
    directories = ["/Betty", "/Betty/Holberton"]
    createdir(directories)
