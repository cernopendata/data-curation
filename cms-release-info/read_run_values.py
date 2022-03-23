#!/usr/bin/env python

import subprocess
import sys
from helpers import *


"""
Read run range information from an input file.
"""

input = sys.argv[1]
if "Run" in input:
    run_period = input
else:
    year = input


def main():
    "Do the job."

    print (*read_run_range(run_period), sep =', ')

if __name__ == "__main__":
    main()