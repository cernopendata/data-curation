#!/usr/bin/env python3

"""
Aggregate dataset records created in the output directory.
"""

import json
import os

DIR = "./outputs/records-2024-03/"
GROUP_BY = 500

files = os.listdir(DIR)

part = 0
i = 0
records = []
for afile in files:

    with open(os.path.join(DIR, afile), "r") as fdr:
        try:
            record = json.loads(fdr.read())
        except:
            record = {}
            print(f"[ERROR] {afile}")
    if record:
        records.append(record)
        i = i + 1

    if i >= GROUP_BY:
        part = part + 1
        part_content = json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
        with open(f"cms-simulated-datasets-2016-part_{part:02}.json", "w") as fdw:
            fdw.write(part_content + "\n")
        i = 0
        records = []

part = part + 1
part_content = json.dumps(
    records, indent=2, sort_keys=True, ensure_ascii=False, separators=(",", ": ")
)
with open(f"cms-simulated-datasets-2016-part_{part:02}.json", "w") as fdw:
    fdw.write(part_content + "\n")
