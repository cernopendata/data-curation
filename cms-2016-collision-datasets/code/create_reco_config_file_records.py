#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create RECO CMS Configuration Files records.
"""

import hashlib
import json
import re
import os
import shutil


NOTE = (
    "This file describes the exact setup for the CMS software executable which "
    "was used in a data-processing step. It is provided only <i>for information "
    "purposes</i>. Although all the components required to <i>analyse</i> the public "
    "primary datasets - such as corresponding input data, condition data, software "
    "version - are provided on this portal, it is not necessarily possible to "
    "<i>reproduce</i> all the described data-processing steps."
)


RECID_START = 30400
YEAR_CREATED = "2016"
YEAR_PUBLISHED = "2024"
COLLISION_ENERGY = "13Tev"
COLLISION_TYPE = "pp"


def get_content(afile):
    "Return full content of the configuration file."
    return open("./inputs/config-store/" + afile, "r").read()


def get_run_period(afile):
    "Return run period for configuration file."
    file_name = get_python_filename(afile)
    if "2016G" in file_name:
        return "Run2016G"
    if "2016H" in file_name:
        return "Run2016H"
    return "FIXME"


def get_abstract(afile):
    "Return abstract for configuration file."
    process = get_process(afile)
    annotation = get_annotation(afile)
    abstract = "The configuration file used in " + process + " data processing step"
    if "nevts" in annotation:
        return abstract + "."
    else:
        return abstract + " for " + annotation + "."


def get_title(afile):
    "Return suitable title of configuration file."
    process = get_process(afile)
    filename = get_python_filename(afile)
    if filename.endswith('.py'):
        filename = filename[:-3]
    return "Configuration file for " + process + " step " + filename


def get_python_filename(afile):
    "Return python_filename from configuration file."
    content = get_content(afile)
    python_filename = ""
    m = re.search(r"--python_filename[= ](.*\.py)", content)
    if m:
        python_filename = m.groups(1)[0]
        python_filename = os.path.basename(python_filename)

        pattern = r"-000\d+_0_cfg\.py$" # remove not needed trailing numbers from file name
        python_filename = re.sub(pattern, ".py", python_filename)
    return python_filename


def get_annotation(afile):
    "Return annotation from configuration file."
    content = get_content(afile)
    annotation = ""
    m = re.search(r"annotation = cms.untracked.string\('(.*)'\)", content)
    if m:
        annotation = m.groups(1)[0]
    return annotation


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = "UNKNOWN"
    m = re.search(r"process = cms\.Process\('([^']*)'", content)
    if m:
        process = m.group(1)
    return process


def get_size(afile):
    """Return the size of the configuration file."""
    file_path = "./inputs/config-store/" + afile
    return os.path.getsize(file_path)


def get_checksum(afile):
    """Return the SHA1 checksum of the configuration file."""
    file_path = "./inputs/config-store/" + afile
    return hashlib.sha1(open(file_path, "rb").read()).hexdigest()


def main():
    """Do the main job."""

    recid = RECID_START
    fdesc = open("./outputs/reco_config_files_link_info.py", "w")
    fdesc.write("LINK_INFO = {\n")

    records = []
    files_seen = []
    for root, dirs, files in os.walk("./inputs/config-store/"):

        for afile in files:

            # Skip non-RECO files
            afile_python_filename = get_python_filename(afile)

            if not afile_python_filename.startswith("ReReco") and not afile_python_filename.startswith("recoskim"):
                continue
            
            if afile_python_filename in files_seen:
                continue
            
            files_seen.append(afile_python_filename)

            # Create nice reco_*.py files for copying them over to EOSPUBLIC
            shutil.copyfile(
                "./inputs/config-store/" + afile, "./outputs/" + afile_python_filename
            )

            rec = {}

            rec["abstract"] = {}
            rec["abstract"]["description"] = get_abstract(afile)

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

            rec["experiment"] = [
                "CMS"
            ]

            rec["files"] = [
                {
                    "checksum": "adler32:" + get_checksum(afile),
                    "size": get_size(afile),
                    "uri": "root://eospublic.cern.ch//eos/opendata/cms/configuration-files/2016/"
                    + afile_python_filename,
                }
            ]

            rec["note"] = {}
            rec["note"]["description"] = NOTE

            rec["publisher"] = "CERN Open Data Portal"

            rec["recid"] = str(recid)

            rec["run_period"] = [
                get_run_period(afile),
            ]

            rec["title"] = get_title(afile)

            rec["type"] = {}
            rec["type"]["primary"] = "Supplementaries"
            rec["type"]["secondary"] = [
                "Configuration",
            ]

            records.append(rec)

            fdesc.write(
                "  '%s': %d,\n" % (afile_python_filename.split(".", 1)[0], recid)
            )
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
