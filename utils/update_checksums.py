#!/usr/bin/python3

"""Helper script for updating file size and checksum information."""

import click
import json
import re
import sys


def populate_file_cache(filename):
    """Read EOS file information from FILENAME and populate the cache."""
    files = {}
    for line in open(filename, "r").readlines():
        line = line.strip()
        match = re.search(r"^path=(.*) size=(.*) checksum=(.*)", line)
        if match:
            path, size, checksum = match.groups()
            files[path] = {
                "checksum": "adler32:" + checksum,
                "size": int(size),
            }
    return files


@click.command()
@click.option("--source", "-s", required=True, help="Source of information? [file1]")
@click.option("--target", "-t", required=True, help="Target to modify? [file2]")
@click.option(
    "--check-only",
    "-c",
    is_flag=True,
    default=False,
    help="Check only without updating?",
)
def main(source, target, check_only):  # noqa: D301
    """Alter record fixtures (TARGET) based on EOS file information (SOURCE).

    Example: (check fixtures)

     \b
     $ eos find --xurl --size --checksum -name "*_file_index.*" /eos/opendata/ > z.txt
     $ for file in cernopendata/modules/fixtures/data/records/*.json; \\
         do ../data-curation/utils/update_checksums.py -c -s z.txt -t $file; done

    Example: (update file info in fixtures)

     \b
     $ eos find --xurl --size --checksum /eos/opendata/alice/modules > alice.txt
     $ head -3 alice.txt
     path=root://eospublic.cern.ch//eos/opendata/alice/modules/PtAnalysis.tgz size=2086046 checksum=1c06f1e5
     path=root://eospublic.cern.ch//eos/opendata/alice/modules/alice-mc.tgz size=31139203 checksum=49beca01
     path=root://eospublic.cern.ch//eos/opendata/alice/modules/alice-raa.tgz size=15469921 checksum=154c512a
     $ update_checksums.py -s alice.txt \\
             -t cernopendata/modules/fixtures/data/records/alice-analysis-modules.json
             > alice-analysis-modules-NEW.json
     $ colordiff -u alice-analysis-modules.json \\
                    alice-analysis-modules-NEW.json
     $ mv alice-analysis-modules-NEW.json \\
          alice-analysis-modules.json
     $ git commit -a -s -m 'records: ALICE file information update'
    """  # noqa: E501
    # read source
    files = populate_file_cache(source)

    # read target
    target_content = open(target, "r").read()
    target_records = json.loads(target_content)

    # check and amend target records
    errors_found = 0
    for target_record in target_records:
        for record_file in target_record.get("files", []):
            if check_only:
                if record_file["uri"] in files:
                    if (
                        record_file["size"] == files.get(record_file["uri"])["size"]
                        and record_file["checksum"]
                        == files.get(record_file["uri"])["checksum"]
                    ):  # noqa: E501
                        pass  # all OK
                    else:
                        errors_found = 1
                        print(
                            "ERROR with record {0} file {1}".format(
                                target_record["recid"], record_file["uri"]
                            ),
                            file=sys.stderr,
                        )
            else:
                try:
                    eos_size = files.get(record_file["uri"])["size"]
                    eos_checksum = files.get(record_file["uri"])["checksum"]
                    record_file["size"] = eos_size
                    record_file["checksum"] = eos_checksum
                except Exception:
                    print(
                        "ERROR with record {0} file {1}".format(
                            target_record["recid"], record_file["uri"]
                        ),
                        file=sys.stderr,
                    )
    if check_only:
        sys.exit(errors_found)

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
