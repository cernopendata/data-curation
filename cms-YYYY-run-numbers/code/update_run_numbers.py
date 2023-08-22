#!/usr/bin/python3

"""Helper script for updating run numbers in CMS dataset records."""

import click
import filecmp
import json
import os
import sys


def populate_runnumber_cache():
    """Read input information about run numbers and populate the cache."""
    cache = {}
    dataset = ""
    values = []
    for line in open("./inputs/allruns.txt", "r").readlines():
        line = line.strip()
        if line.startswith("/"):
            # finish information about the dataset
            if dataset in cache.keys():
                print(f"[ERROR] {dataset} existing several times in the input file.")
            else:
                if len(values):
                    values.sort()
                    cache[dataset] = values
            # start reading new dataset
            dataset = line
            values = []
        else:
            values.append(str(line))
    return cache


@click.command()
@click.option("--target", "-t", required=True, help="Target to modify? [file2]")
@click.option(
    "--check-only",
    "-c",
    is_flag=True,
    default=False,
    help="Check only without updating?",
)
def main(target, check_only):  # noqa: D301
    """Alter record fixtures (TARGET) based on run number file information.

    Example: (check run numbers in fixtures)

     \b
     $ for file in ~o/cernopendata/modules/fixtures/data/records/cms-*.json; \\
         do python ./code/update_run_numbers.py -c -t $file; done

    Example: (update run numbers in fixtures)

     \b
     $ for file in ~o/cernopendata/modules/fixtures/data/records/cms-*.json; \\
         do python ./code/update_run_numbers.py -t $file; done
    """  # noqa: E501
    # populate run number cache from input file
    cache = populate_runnumber_cache()

    # read target
    target_content = open(target, "r").read()
    target_records = json.loads(target_content)

    # check and amend target records
    errors_found = 0
    for target_record in target_records:
        dataset_full_name = target_record["title"]
        if dataset_full_name in cache.keys():
            run_numbers_existing = target_record.get("run_numbers", [])
            run_numbers_desired = cache[dataset_full_name]
            if check_only:
                if run_numbers_existing == run_numbers_desired:
                    pass  # all OK
                else:
                    errors_found = 1
                    print(
                        "ERROR Record {0} does not contain desired run numbers {1}".format(
                            target_record["recid"], run_numbers_desired
                        ),
                        file=sys.stderr,
                    )
            else:
                target_record["run_numbers"] = run_numbers_desired

    # report any problems
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

    target_new = target + "_modded"
    with open(target_new, "w") as fdesc:
        fdesc.write(new_content + "\n")

    if filecmp.cmp(target, target_new):
        os.remove(target_new)
    else:
        os.replace(target_new, target)


if __name__ == "__main__":
    main()
