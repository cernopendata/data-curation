#!/usr/bin/env python3

"""Verify record fixture file regarding distribution field.

Counts file information from the files field and updates
distribution.number_of_files and distribution.size accordingly.
"""

import json
import os
import sys

import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def verify_record_fixture_file(filename):
    """Verify record fixture file regarding distribution field.

    Counts file information from the files field and updates
    distribution.number_of_files and distribution.size accordingly.
    """
    with open(filename, "r") as fdesc:
        records = json.loads(fdesc.read())

    changes_needed = False
    for record in records:
        # get information
        rec_number_of_files = int(record.get("distribution", {}).get("number_files", 0))
        rec_size = int(record.get("distribution", {}).get("size", 0))
        rec_files_number = 0
        rec_files_size = 0
        rec_usage = record.get("usage", {}).get("description", "")
        rec_usage_filename_tarball = ""
        rec_usage_filename_data = ""
        rec_usage_filename_mc = ""
        for rec_files_afile in record.get("files", []):
            rec_files_number += 1
            rec_files_size += int(rec_files_afile.get("size"))
            rec_files_uri = rec_files_afile.get("uri")
            if ".zip" in rec_files_uri:
                rec_usage_filename_tarball = os.path.basename(rec_files_uri)
            if not rec_usage_filename_data and "data_" in rec_files_uri:
                rec_usage_filename_data = os.path.basename(rec_files_uri)
            if not rec_usage_filename_mc and "mc_" in rec_files_uri:
                rec_usage_filename_mc = os.path.basename(rec_files_uri)

        if rec_number_of_files != rec_files_number:
            record["distribution"]["number_files"] = rec_files_number
            changes_needed = True
        if rec_size != rec_files_size:
            record["distribution"]["size"] = rec_files_size
            changes_needed = True

        changes_needed = True
        rec_usage = "<p>" + rec_usage + "</p>"
        rec_usage = (
            f"<p>This dataset is provided as a zipped tarball (<code>{rec_usage_filename_tarball}</code>) and as a list of unzipped individually-accessible ROOT files containing the collision data (such as <code>{rec_usage_filename_data}</code>) and the simulated data (such as <code>{rec_usage_filename_mc}</code>). You can use either the tarball or the individual ROOT files.</p> "
            + rec_usage
        )
        record["usage"]["description"] = rec_usage

    if changes_needed:
        new_content = json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
        with open(filename, "w") as fdesc:
            fdesc.write(new_content + "\n")


if __name__ == "__main__":
    verify_record_fixture_file()
