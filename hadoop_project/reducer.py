#!/usr/bin/python3
"""
Imports
"""
import sys


top_salaries = []

for line in sys.stdin:
    line = line.strip()

    id, company_comp = line.split("\t")

    company, comp = company_comp.split(",")

    comp = float(comp)

    top_salaries.append((comp, id, company))

    top_salaries = sorted(top_salaries, reverse=True)[:10]

for salary in top_salaries:
    comp, id, company = salary
    print(f"{id}, {company}\t{comp}")
