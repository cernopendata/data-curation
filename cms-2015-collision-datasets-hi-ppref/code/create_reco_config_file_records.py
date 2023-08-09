#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS 2015 HI ppref RECO configuration files records.
"""

import hashlib
import json
import re
import os
import shutil

RECID_START = 24700
year_created = "2015"
year_published = "2023"
collision_energy = "5.02TeV"
collision_type = "pp"
run_period = "Run2015E"

NOTE = (
    "This file describes the exact setup for the CMS software executable which "
    "was used in a data-processing step. It is provided only <i>for information "
    "purposes</i>. Although all the components required to <i>analyse</i> the public "
    "primary datasets - such as corresponding input data, condition data, software "
    "version - are provided on this portal, it is not necessarily possible to "
    "<i>reproduce</i> all the described data-processing steps."
)


def main():
    """Do the main job."""

    recid = RECID_START
    fdesc = open("./outputs/reco_config_files_link_info.py", "w")
    fdesc.write("LINK_INFO = {\n")

    records = []

    for line in open("./inputs/reco-config-files-listing.txt", "r").readlines():
        line = line.strip()
        match = re.search(r"^path=(.*) size=(.*) checksum=(.*)", line)
        if match:
            path, size, checksum = match.groups()

            filename = path.rsplit("/", 1)[-1]
            filename_without_ext = filename.rsplit(".", 1)[0]

            rec = {}

            rec["abstract"] = {}
            rec["abstract"][
                "description"
            ] = "The configuration file used in the prompt RECO data processing step immediately after data taking."

            rec["accelerator"] = "CERN-LHC"

            rec["collaboration"] = {}
            rec["collaboration"]["name"] = "CMS collaboration"

            rec["collections"] = [
                "CMS-Configuration-Files",
            ]

            rec["collision_information"] = {}
            rec["collision_information"]["energy"] = collision_energy
            rec["collision_information"]["type"] = collision_type

            rec["date_created"] = [
                year_created,
            ]
            rec["date_published"] = year_published

            rec["distribution"] = {}
            rec["distribution"]["formats"] = [
                "py",
            ]
            rec["distribution"]["number_files"] = 1
            rec["distribution"]["size"] = int(size)

            rec["experiment"] = "CMS"

            rec["files"] = [
                {
                    "checksum": "adler32:" + checksum,
                    "size": int(size),
                    "uri": path,
                }
            ]

            rec["note"] = {}
            rec["note"]["description"] = NOTE

            rec["publisher"] = "CERN Open Data Portal"

            rec["recid"] = str(recid)

            rec["run_period"] = [
                run_period,
            ]

            rec["title"] = f"Configuration file for RECO step {filename_without_ext}"

            rec["type"] = {}
            rec["type"]["primary"] = "Supplementaries"
            rec["type"]["secondary"] = [
                "Configuration",
            ]

            records.append(rec)

            fdesc.write("  '%s': %d,\n" % (filename.split(".", 1)[0], recid))
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
