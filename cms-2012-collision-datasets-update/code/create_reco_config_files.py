#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create RECO configuration files.

Walks through ./inputs/config-cache and creates RECO configuration files
in ./inputs/reco-config-files by selecting only appropriate RECO processes.
"""

import re
import os
import shutil


def get_content(afile):
    "Return full content of the configuration file."
    return open("./inputs/config-store/" + afile, "r").read()


def get_python_filename(afile):
    "Return python_filename from configuration file."
    content = get_content(afile)
    python_filename = ""
    m = re.search(r"--python (.*)\.py", content)
    if m:
        python_filename = str(m.groups(1)[0])
    return os.path.basename(python_filename)


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = "UNKNOWN"
    m = re.search(r"process = cms.Process\(\s?['\"]([A-Z]+)['\"]\s?\)", content)
    if m:
        process = str(m.groups(1)[0])
    return process


def main():
    """Do the main job."""
    if not os.path.exists("./inputs/reco-config-files"):
        os.mkdir("./inputs/reco-config-files")
    for root, dirs, files in os.walk("./inputs/config-store"):
        for afile in files:
            process = get_process(afile)
            if process == "RECO":
                python_filename = get_python_filename(afile)
                if python_filename.startswith("reco"):
                    shutil.copyfile(
                        f"./inputs/config-store/{afile}",
                        f"./inputs/reco-config-files/{python_filename}.py",
                    )


if __name__ == "__main__":
    main()
