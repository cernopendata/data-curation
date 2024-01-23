#!/usr/bin/env python3

"""
Create CMS 2015 trigger information record's HTML snippet.
"""

import json
import re
import sys

RECID_START = 23900

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open("./outputs/hlt_config_files_link_info.py", "r").read())


def main():
    """Do the main job."""

    rec = {}

    rec["abstract"] = {}

    abstract_description = "\n      The list of trigger configuration files for the CMS 2015 proton-proton collision data (Run2015D from run number 256630 to run number 260627, Run2015G from run number 261445 to run number 262328):\n      <table class=\"table\">\n      <thead>\n     <tr><th>Run number</th><th>Software version</th><th>Trigger configuration</th></tr>\n      </thead>\n      <tbody>"
    with open("inputs/cms-trigger-information-run2-helper.html", "r") as fdesc:

        for line in fdesc.readlines():
            if "cosmic" in line or "special" in line:
                # Skip Cosmic and Special related triggers
                continue
            abstract_description += "\n"
            match = re.match(r"^(.*)<a href=\"files/(.*)\">(.*)</a>(.*)$", line)
            if match:
                intro, linkfile, linklabel, outro = match.groups()
                recid = LINK_INFO[linklabel]
                abstract_description += f'{intro}<a href="/record/{recid}">{linklabel}</a>{outro}'
            else:
                abstract_description += line

    abstract_description += '\n      </tbody>\n      </table>'

    rec["abstract"]["description"] = abstract_description

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Trigger-Information",
    ]

    rec["date_created"] = [
        "2015",
    ]

    rec["date_published"] = "2021"

    rec["experiment"] = "CMS"

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(RECID_START)

    rec["run_period"] = [
        "Run2015D",
        "Run2015G",
    ]

    rec["title"] = "High-Level Trigger information for CMS 2015 open data"

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
