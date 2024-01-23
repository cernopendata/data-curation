#!/usr/bin/env python3

"""
Create CMS 2013 trigger information record.
"""

import json
import re

RECID_START = 1702
date_created = "2013"
date_published = "2023"
run_number_pp = "Run2013A"
run_number_pPb = "HIRun2013"

LINK_INFO = {}
exec(open("./outputs/hlt_config_files_link_info.py", "r").read())


def main():
    """Do the main job."""

    rec = {}

    rec["abstract"] = {}

    abstract_description = '\n      The list of trigger configuration files for the CMS 2013 proton-lead collision data (HIRun2013 from run number 2610498 to run number 211631) and CMS 2013 proton-proton heavy-ion reference collision data (Run2013A from run number 211739 to run number 211831):\n      <table class="table">\n      <thead>\n     <tr><th>Run number</th><th>Software version</th><th>Trigger configuration</th></tr>\n      </thead>\n      <tbody>'

    with open("outputs/cms-trigger-information-2013-helper.html", "r") as fdesc:

        for line in fdesc.readlines():
            if "cosmic" in line or "special" in line:
                # Skip Cosmic and Special related triggers
                continue
            abstract_description += "\n"
            match = re.match(r"^(.*)<a href=\"files/(.*)\">(.*)</a>(.*)$", line)
            if match:
                intro, linkfile, linklabel, outro = match.groups()
                recid = LINK_INFO[linklabel]
                abstract_description += (
                    f'{intro}<a href="/record/{recid}">{linklabel}</a>{outro}'
                )
            else:
                abstract_description += line

    abstract_description += "\n      </tbody>\n      </table>"

    rec["abstract"]["description"] = abstract_description

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Trigger-Information",
    ]

    rec["date_created"] = [
        date_created,
    ]

    rec["date_published"] = date_published

    rec["experiment"] = "CMS"

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(RECID_START)

    rec["run_period"] = [run_number_pPb, run_number_pp]

    rec["title"] = f"High-Level Trigger information for CMS {date_created} open data"

    rec["type"] = {}
    rec["type"]["primary"] = "Supplementaries"
    rec["type"]["secondary"] = [
        "Trigger",
    ]

    print(
        json.dumps(
            [
                rec,
            ],
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        ),
    )


if __name__ == "__main__":
    main()
