#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

import json

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open("./outputs/hlt_config_files_link_info.py", "r").read())

RECID_START = 22600


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
    out += "<p>See also the full list of triggers for CMS 2015 open data:"
    out += ' <a href="/record/23900">Trigger information for CMS 2015 open data</a></p>'
    return out + ""


def main():
    """Do the main job."""

    year_created = "2015"
    year_published = "2021"

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
                rec["collaboration"]["recid"] = "451"

                rec["collections"] = [
                    "CMS-Trigger-Information",
                ]

                rec["date_created"] = [
                    year_created,
                ]
                rec["date_published"] = year_published

                rec["experiment"] = "CMS"

                rec["publisher"] = "CERN Open Data Portal"

                rec["recid"] = str(recid)

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
