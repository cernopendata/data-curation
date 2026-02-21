#!/usr/bin/env python

"""
Create JADE logbook records.
"""

import json
import re

recid_start = 26100
year_published = "2023"


def create_record(recid, path, size, checksum):
    """Create record for the given JADE logbook."""

    rec = {}

    try:
        logbook_number = re.match(r"^.*Log([0-9]+)\.pdf", path).groups(0)[0]
    except Exception:
        logbook_number = "FIXME"

    logbook_period = "1970"

    rec["abstract"] = {}
    rec["abstract"][
        "description"
    ] = f"This is JADE logbook {logbook_number} from {logbook_period}. FIXME add more description."

    rec["accelerator"] = "DESY-PETRA"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "JADE collaboration"
    rec["collaboration"]["recid"] = "451"

    rec["collections"] = [
        "JADE-Logbooks",
    ]

    rec["date_created"] = [
        logbook_period,
    ]
    rec["date_published"] = year_published

    rec["distribution"] = {}
    rec["distribution"]["formats"] = [
        "pdf",
    ]
    rec["distribution"]["number_files"] = 1
    rec["distribution"]["size"] = size

    rec["experiment"] = "JADE"

    rec["files"] = []
    rec["files"].append(
        {
            "checksum": "adler32:" + checksum,
            "size": size,
            "uri": path,
        }
    )

    rec["license"] = {}
    rec["license"]["attribution"] = "CC0"

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    rec["title"] = f"JADE logbook number {logbook_number}"

    rec["type"] = {}
    rec["type"]["primary"] = "Supplementaries"
    rec["type"]["secondary"] = [
        "Logbook",
    ]

    return rec


def create_records():
    """Create records."""
    with open("./inputs/eos-file-information-logbooks.txt", "r") as f:
        records = []
        recid = recid_start
        for line in f.readlines():
            match = re.match(r"^path=(.*) size=(.*) checksum=(.*)$", line.strip())
            if match:
                path, size, checksum = match.groups()
                size = int(size)
            records.append(create_record(recid, path, size, checksum))
            recid += 1
    return records


def print_records(records):
    """Print records."""
    print(
        json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    )


def main():
    "Do the job."

    records = create_records()
    print_records(records)


if __name__ == "__main__":
    main()
