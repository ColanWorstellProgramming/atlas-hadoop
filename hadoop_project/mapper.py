#!/usr/bin/python3
"""
Imports
"""
import sys


for line in sys.stdin:
    row = line.split(",")

    id = row[0]
    company = row[1]
    comp = row[2]

    print(f"{id}\t{company}, {comp}")
