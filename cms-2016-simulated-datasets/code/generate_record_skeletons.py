#!/usr/bin/env python3

"""
Generate CMS 2016 record skeletons including only persistent identifiers.
"""

import json
import os

# Import record ID information
RECID_INFO = {}
exec(open("./inputs/recid_info.py", "r").read())

# Import DOI information
dois = {}
with open("./inputs/doi-sim.txt", "r") as fdesc:
    for line in fdesc.readlines():
        dataset, doi = line.split()
        dois[dataset] = doi

# Generate record skeletons
records = []
for dataset in RECID_INFO.keys():
    records.append(
        {
            "title": dataset,
            "recid": str(RECID_INFO[dataset]),
            "doi": dois[dataset],
        }
    )

# Print record skeletons
new_content = json.dumps(
    records, indent=2, sort_keys=True, ensure_ascii=False, separators=(",", ": ")
)
if not os.path.exists("./outputs"):
    os.makedirs("./outputs")
with open("./outputs/cms-simulated-datasets-2016-skeletons.json", "w") as fdesc:
    fdesc.write(new_content + "\n")
