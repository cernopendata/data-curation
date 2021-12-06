#!/usr/bin/env python

"""
Enrich created dataset records with file information.
"""

import json

from dataset_records import get_dataset_index_files, get_dataset_format

for part in range(1, 16):

    with open(f"./outputs/cms-2015-simulated_{part}.json", "r") as fdesc:
        records = json.loads(fdesc.read())

        for record in records:
            dataset = record["title"]
            dataset_format = get_dataset_format(dataset)
            record_files = get_dataset_index_files(
                dataset, eos_dir="./inputs/eos-file-indexes/"
            )
            if record_files:
                record["files"] = []
                for index_type in [".json", ".txt"]:
                    index_files = [f for f in record_files if f[0].endswith(index_type)]
                    for file_number, (file_uri, file_size, file_checksum) in enumerate(
                        index_files
                    ):
                        record["files"].append(
                            {
                                "checksum": "adler32:" + file_checksum,
                                "description": dataset
                                + dataset_format
                                + " dataset file index ("
                                + str(file_number + 1)
                                + " of "
                                + str(len(index_files))
                                + ") for access to data via CMS virtual machine",
                                "size": file_size,
                                "type": "index" + index_type,
                                "uri": file_uri,
                            }
                        )

        new_content = json.dumps(records, indent=2, sort_keys=records)
        with open(f"cms-2015-simulated_{part}.json", "w") as fdesc:
            for line in new_content.split("\n"):
                line = line.rstrip()
                fdesc.write(line + "\n")
