#!/usr/bin/env python3

"""
Create CMS 2016 trigger information record's HTML snippet.
"""

import json
import re
import sys

sys.path.insert(1, "../cms-release-info")
from helpers import run_range_text


RECID_START = 94299 # TPM: this is a good one
RUN_PERIOD = ["Run2017C", "Run2017E",]
YEAR_CREATED = "2017"
YEAR_PUBLISHED = "2024"


LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open("./outputs/hlt_config_files_link_info.py", "r").read())


def get_run_range(run_period):
    "Return the min and max run numbers for the given run period."
    output = run_range_text(run_period)
    run_range = re.findall(r'\b\d+\b', output)
    return run_range


def main():
    """Do the main job."""

    rec = {}

    rec["abstract"] = {}

    abstract_description = f"\n      The list of trigger configuration files for the CMS {YEAR_CREATED} proton-proton collision data ({RUN_PERIOD[0]} from run numbers {get_run_range(RUN_PERIOD[0])[0]} and {get_run_range(RUN_PERIOD[0])[1]} & {RUN_PERIOD[1]} from run number {get_run_range(RUN_PERIOD[1])[0]} and {get_run_range(RUN_PERIOD[1])[1]}):\n      <table class=\"ui table striped\">\n      <thead>\n     <tr><th>Run number</th><th>Software version</th><th>Trigger configuration</th></tr>\n      </thead>\n      <tbody>"


    with open("inputs/cms-trigger-information-run2-helper.html", "r") as fdesc:

        for line in fdesc.readlines():
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
    rec["collaboration"]["name"] = "CMS Collaboration"
    rec["collaboration"]["recid"] = ""

    rec["collections"] = [
        "CMS-Trigger-Information",
    ]

    rec["date_created"] = [
        YEAR_CREATED,
    ]

    rec["date_published"] = YEAR_PUBLISHED

    rec["experiment"] = "CMS"

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(RECID_START)

    rec["run_period"] = RUN_PERIOD

    rec["title"] = f"High-Level Trigger information for CMS {YEAR_CREATED} open data"

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
