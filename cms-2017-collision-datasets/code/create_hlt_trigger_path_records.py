#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

import json

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open("./outputs/hlt_config_files_link_info.py", "r").read())

RECID_START = 94300 # TPM: this should be good
YEAR_CREATED = "2017"
YEAR_PUBLISHED = "2024"
COLLISION_ENERGY = "13TeV"
COLLISION_TYPE = "pp"
RUN_PERIOD = "Run2017"


def expand_links(atext):
    "Take text and expand links based on LINK_INFO."
    btext = atext
    for key in LINK_INFO.keys():
        if key in btext:
            btext = btext.replace(
                key, '<a href="/record/%d">%s</a>' % (LINK_INFO[key], key)
            )
    return btext


def create_rich_abstract(title, info):
    """Create rich abstract out of info items."""
    out = " "
    out += "<p>High-Level Trigger path information %s.</p>" % title
    if info:
        out += "<blockquote>"
        for item in info:
            out += "<p>" + expand_links(item) + "</p>"
        out += "</blockquote>"
    out += f"<p>See also the full list of triggers for CMS {YEAR_CREATED} open data:"
    out += f' <a href="/record/30300">Trigger information for CMS {YEAR_CREATED} open data</a></p>'
    return out + ""


def main():
    """Do the main job."""

    records = []
    recid = RECID_START
    title = None
    info = []
    for line in open("./inputs/hlt-trigger-path.txt", "r").readlines():
        if line.startswith("Path"):
            if title:

                rec = {}

                rec["abstract"] = {}
                rec["abstract"]["description"] = create_rich_abstract(title, info)

                rec["accelerator"] = "CERN-LHC"

                rec["collaboration"] = {}
                rec["collaboration"]["name"] = "CMS Collaboration"
                rec["collaboration"]["recid"] = ""
                rec["collections"] = [
                    "CMS-Trigger-Information",
                ]

                rec["collision_information"] = {}

                rec["collision_information"]["energy"] = COLLISION_ENERGY
                rec["collision_information"]["type"] = COLLISION_TYPE

                rec["date_created"] = [
                    YEAR_CREATED,
                ]
                rec["date_published"] = YEAR_PUBLISHED

                rec["experiment"] = "CMS"

                rec["publisher"] = "CERN Open Data Portal"

                rec["recid"] = str(recid)

                rec["run_period"] = [
                    RUN_PERIOD,
                ]

                rec["title"] = "High-Level Trigger path information " + title

                rec["type"] = {}
                rec["type"]["primary"] = "Supplementaries"
                rec["type"]["secondary"] = [
                    "Trigger",
                ]

                records.append(rec)

                recid += 1
                info = []

            title = line.split(" ", 1)[1].strip()
            if title.endswith(":"):
                title = title[:-1]
        elif line.startswith(" - "):
            info.append(line[2:].strip())
        else:
            pass

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
