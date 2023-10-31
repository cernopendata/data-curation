#!/usr/bin/env python3

"""Verify record fixture file regarding distribution.availability field.

If a dataset record contains 'ondemand' availability is found but the record
has attached some 'files' field, inform about this and update the file.

If a dataset record does not contain file and does not specify availability
field, inform about this and update the file.

Note: to be used mostly with CMS simulated datasets only.
"""

import json
import sys

import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def verify_record_fixture_file(filename):
    """Verify record fixture file regarding ondemand availability.

    If a dataset record contains 'ondemand' availability is found but the
    record has attached some 'files' field, inform about this and update
    the file.

    If a dataset record does not contain file and does not specify availability
    field, inform about this and update the file.
    """
    with open(filename, "r") as fdesc:
        records = json.loads(fdesc.read())

    changes_needed = False
    for record in records:
        # get information
        recid = record.get("recid")
        availability = record.get("distribution", {}).get("availability", "")
        files = record.get("files", None)
        # check records
        if availability == "ondemand" and files:
            changes_needed = True
            print(
                "[ERROR] Record {0} is 'ondemand' but has 'files'.".format(recid),
                file=sys.stderr,
            )
            del record["distribution"]["availability"]

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
