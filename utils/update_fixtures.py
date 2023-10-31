#!/usr/bin/python3

"""A helper script for updating record fixtures.

This helper script is useful for updating selected JSON fields in the CERN Open
Data record fixtures. For example, it permits to update the record
classification field or the record file location fields.

"""

import click
import json


@click.command()
@click.option("--source", "-s", required=True, help="Source of information? [file1]")
@click.option("--target", "-t", required=True, help="Target to modify? [file2]")
@click.option("--match", "-m", required=True, help='Field to match? E.g. "recid".')
@click.option(
    "--update", "-u", required=True, help='Field to update? E.g. "categories".'
)
def main(source, target, match, update):  # noqa: D301,D412,D413
    """Alter TARGET file based on SOURCE file information.

    Look through TARGET file records looking at MATCH fields and if some MATCH
    field is identical to an entry in SOURCE file records, then replace the
    UPDATE field value in the TARGET file with the value taken from the matched
    SOURCE file record. Print the updated records on the standard output.

    Example:

     \b
     $ head -10 new-categories.json
     [
       {
         "title": "/GluGluToHToZZTo4L_M-550_7TeV-powheg15-pythia6/.../AODSIM",
         "categories": {
           "primary": "Higgs Physics",
           "secondary": [
             "Standard Model"
           ],
           "source": "CMS Collaboration"
         }
     $ update_fixtures.py -s new-categories.json \\
                          -t cms-simulated-datasets-2011.json \\
                          -m title -u categories \\
             > cms-simulated-datasets-2011-NEW.json
     $ colordiff -u cms-simulated-datasets-2011.json \\
                    cms-simulated-datasets-2011-NEW.json
     $ mv cms-simulated-datasets-2011-NEW.json \\
          cms-simulated-datasets-2011.json
     $ git commit -a -s -m 'records: CMS category updates'
    """
    # read source
    source_content = open(source, "r").read()
    source_records = json.loads(source_content)

    # read target
    target_content = open(target, "r").read()
    target_records = json.loads(target_content)

    # amend target records
    for target_record in target_records:
        key = target_record[match]
        for source_record in source_records:
            if source_record[match] == key:
                target_record[update] = source_record[update]

    # print records
    new_content = json.dumps(
        target_records,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )
    print(new_content + "\n")


if __name__ == "__main__":
    main()
