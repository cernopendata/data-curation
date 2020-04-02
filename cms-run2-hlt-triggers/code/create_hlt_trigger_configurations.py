#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert CMS Trigger configuration files.
"""

import glob
import os
import subprocess

def main():
    """Do the main job."""

    # find lines in input file starting with "CMSSW"
    lines = open('./inputs/summary.txt', 'r').readlines()
    filtered_lines = [a for a in lines if a.startswith("CMSSW")]#[:2] <-- Uncomment this to set max file count for testing purposes

    # print lines count
    print(
        "Found {line_count} convertable lines in input, converting...".format(
            line_count = str(len(filtered_lines))
        )
    )

    # for every configuration line:
    for line_number, line in enumerate(filtered_lines):
        title = line.split(None, 2)[1]
        
        # print progress
        print(
            "Converting '{title}' ( {line_num} / {line_count} )".format(
                title = title,
                line_num = str(line_number + 1),
                line_count = str(len(filtered_lines))
            )
        )

        # name output file
        filename = title.strip("/").replace("/", "_") + ".py"

        # create conversion command
        command = """python2 ../outputs/CMSSW_10_6_10/src/HLTrigger/Configuration/python/Tools/confdbOfflineConverter.py \\
                    --configName {title} --adg \\
                    > ../outputs/{filename}""".format(
                        title = title,
                        filename = filename
                    )

        # run conversion command in terminal
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.path.dirname(os.path.realpath(__file__)), shell=True)
        output, error = process.communicate()

        # exit on error
        if not process.returncode == 0:
            print("Conversion of some files failed:")
            print(error.decode('utf-8'))
            break

        # print possible output
        if output:
            print(output.decode('utf-8'))

if __name__ == '__main__':
    main()
