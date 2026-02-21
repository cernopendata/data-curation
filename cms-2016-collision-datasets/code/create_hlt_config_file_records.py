#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create HLT CMS Configuration Files records.
"""

import json
import os
import re
import zlib


NOTE = (
    "This file describes the exact setup for the CMS software executable which "
    "was used in a data-processing step. It is provided only <i>for information "
    "purposes</i>. Although all the components required to <i>analyse</i> the public "
    "primary datasets - such as corresponding input data, condition data, software "
    "version - are provided on this portal, it is not necessarily possible to "
    "<i>reproduce</i> all the described data-processing steps."
)


RECID_START = 29000
YEAR_CREATED = "2016"
YEAR_PUBLISHED = "2024"
COLLISION_TYPE = "pp"
COLLISION_ENERGY = "13TeV"


def get_run_period(afile):
    """Return run period for configuration file.

    The knowledge is based on run numbers.
    """
    if "Run2016G" in afile:
        return "Run2016G"
    elif "Run2016H" in afile:
        return "Run2016H"
    else:
        return "Run2016"


def get_content(afile):
    "Return full content of the configuration file."
    return open("./inputs/hlt-config-files/" + afile, "r").read()


def get_title(afile):
    "Return suitable title of configuration file."
    process = get_process(afile)
    tablename = get_tablename(afile)
    return "Configuration file for " + process + " step " + tablename


def get_tablename(afile):
    "Return tableName for configuration file."
    content = get_content(afile)
    tablename = ""
    m = re.search(r"tableName = cms.string\(\s?'(.*)'\s?\)", content)
    if m:
        tablename = m.groups(1)[0]
    return tablename


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = "UNKNOWN"
    m = re.search(r"process = cms.Process\( \"([A-Z]+)\" \)", content)
    if m:
        process = m.groups(1)[0]
    return process


def get_run_numbers_and_software(tablename):
    "Return run numbers and software for given configuration."
    for line in open("./inputs/hlt-trigger-information.txt", "r").readlines():
        cmssw, title, runs = line.split(" ", 2)
        runs = runs.strip()
        runs = runs.replace("(run ", "")
        runs = runs.replace("(runs ", "")
        runs = runs.replace(")", "")
        if title == tablename:
            return (runs, cmssw)
    return None


def create_rich_description(afile):
    "Return suitable description text for the configuration file."
    out = ""
    process = get_process(afile)
    tablename = get_tablename(afile)
    more_info = get_run_numbers_and_software(tablename)
    if more_info:
        out += " "
    out += (
        "The configuration file used in data taking and %(process)s data processing step."
        % {"process": process}
    )
    if more_info:
        run_number = more_info[0]
        cmssw = more_info[1]
        out += (
            '<p>Run number %(run_number)s, software version <a href="https://github.com/cms-sw/cmssw-cvs/tree/%(cmssw)s">%(cmssw)s</a>.</p>'
            % {"run_number": run_number, "cmssw": cmssw.replace("_ONLINE", "")}
        )
        out += ""
    return out


def get_size(afile):
    """Return the size of the configuration file."""
    file_path = "./inputs/hlt-config-files/" + afile
    return os.path.getsize(file_path)


def get_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    file_path = "./inputs/hlt-config-files/" + afile
    return hex(zlib.adler32(open(file_path, "rb").read(), 1) & 0xFFFFFFFF)[2:]


def main():
    """Do the main job."""

    recid = RECID_START
    fdesc = open("./outputs/hlt_config_files_link_info.py", "w")
    fdesc.write("LINK_INFO = {\n")

    records = []

    for root, dirs, files in os.walk("./inputs/hlt-config-files"):
        for afile in files:

            rec = {}

            rec["abstract"] = {}
            rec["abstract"]["description"] = create_rich_description(afile)

            rec["accelerator"] = "CERN-LHC"

            rec["collaboration"] = {}
            rec["collaboration"]["name"] = "CMS Collaboration"
            rec["collaboration"]["recid"] = ""

            rec["collections"] = [
                "CMS-Configuration-Files",
            ]

            rec["collision_information"] = {}
            rec["collision_information"]["energy"] = COLLISION_ENERGY
            rec["collision_information"]["type"] = COLLISION_TYPE

            rec["date_created"] = [
                YEAR_CREATED,
            ]
            rec["date_published"] = YEAR_PUBLISHED

            rec["distribution"] = {}
            rec["distribution"]["formats"] = [
                "py",
            ]
            rec["distribution"]["number_files"] = 1
            rec["distribution"]["size"] = get_size(afile)

            rec["experiment"] = "CMS"

            rec["files"] = [
                {
                    "checksum": "adler32:%s" % get_checksum(afile),
                    "size": get_size(afile),
                    "uri": "root://eospublic.cern.ch//eos/opendata/cms/configuration-files/2016/"
                    + afile,
                }
            ]

            rec["note"] = {}
            rec["note"]["description"] = NOTE

            rec["publisher"] = "CERN Open Data Portal"

            rec["recid"] = str(recid)

            rec["run_period"] = [
                get_run_period(os.path.splitext(os.path.basename(afile))[0]),
            ]

            rec["title"] = get_title(afile)

            rec["type"] = {}
            rec["type"]["primary"] = "Supplementaries"
            rec["type"]["secondary"] = [
                "Configuration",
            ]

            records.append(rec)

            fdesc.write("  '%s': %d,\n" % (get_tablename(afile), recid))
            recid += 1

    fdesc.write("}\n")
    fdesc.close()

    print(
        json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    )


if __name__ == "__main__":
    main()
