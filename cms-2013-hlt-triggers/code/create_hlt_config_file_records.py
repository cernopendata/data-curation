#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS 2013 HLT configuration files records.
"""

import json
import re

RECID_START = 24850
year_created = "2013"
year_published = "2023"
collision_energy_pa = "5.02TeV"
collision_energy_pp = "2.76TeV"
collision_type_pa = "pPb"
collision_type_pp = "pp"
run_period_pa = "HIRun2013"
run_period_pp = "Run2013A"

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
    fdesc = open("./outputs/hlt_config_files_link_info.py", "w")
    fdesc.write("LINK_INFO = {\n")

    records = []

    for line in open("./inputs/hlt-config-files-listing.txt", "r").readlines():
        line = line.strip()
        match = re.search(r"^path=(.*) size=(.*) checksum=(.*)", line)
        if match:
            path, size, checksum = match.groups()

            filename = path.rsplit("/", 1)[-1]
            filename_without_ext = filename.rsplit(".", 1)[0]
            filename_without_ext_with_slashes = "/" + filename_without_ext.replace(
                "_", "/"
            )

            # Disregard "special" ones
            if filename.startswith("cdaq_special"):
                continue

            # Detect collision an drun period information
            if "Run2013PA" in filename:
                collision_energy = collision_energy_pa
                collision_type = collision_type_pa
                run_period = run_period_pa
            elif "Run2013PP" in filename:
                collision_energy = collision_energy_pp
                collision_type = collision_type_pp
                run_period = run_period_pp
            else:
                collision_energy = "FIXME"
                collision_type = "FIXME"
                run_period = "FIXME"

            rec = {}

            rec["abstract"] = {}
            rec["abstract"][
                "description"
            ] = "The configuration file used in data taking and HLT data processing step."

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

            rec[
                "title"
            ] = f"Configuration file for HLT step {filename_without_ext_with_slashes}"

            rec["type"] = {}
            rec["type"]["primary"] = "Supplementaries"
            rec["type"]["secondary"] = [
                "Configuration",
            ]

            records.append(rec)

            fdesc.write("  '%s': %d,\n" % (filename_without_ext_with_slashes, recid))
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
