#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

import glob
import os
import json

TEMPLATE_TOC = """\
      <tr><td>{runs}</td><td><a href="https://github.com/cms-sw/cmssw/tree/{cmssw}">{cmssw}</a></td><td><a href="files/{filename}">{title}</a></td></tr>"""

def main():
    """Do the main job."""

    # find lines in input file starting with "CMSSW"
    lines = open('./inputs/summary.txt', 'r').readlines()
    filtered_lines = [a for a in lines if a.startswith("CMSSW")]#[:2] <-- Uncomment this to limit line count for testing purposes

    # for every configuration line:
    for line in filtered_lines:
        cmssw, title, runs = line.split(None, 2)
        
        runs = runs.strip()
        runs = runs.replace('(run ', '')
        runs = runs.replace('(runs ', '')
        runs = runs.replace(')', '')
        filename = title.strip("/").replace("/", "_") + ".py"
        print(TEMPLATE_TOC.format(
            filename = filename,
            cmssw = cmssw,
            title = title,
            runs = runs,
        ))

if __name__ == '__main__':
    main()
