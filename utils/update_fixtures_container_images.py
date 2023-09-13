#!/usr/bin/env python3

"""Helper script for updating container_images JSON field of dataset record fixutres.

This helper script is useful for creating/updating the container_images JSON field in
the CMS datasets found in the CERN Open Data record fixtures. It utilizes the helper script
update_fixtures.py and cms-release-info/cms_release_container_images_info.json to update
the datasets.

"""

import os
import shutil
import subprocess
import click
import json


@click.command()
@click.option(
    "--input_path", "-i", required=True, help="Relative path to the input directory"
)
@click.option(
    "--output_path", "-o", required=True, help="Relative path to the output directory"
)
def main(input_path, output_path):  # noqa: D301,D412
    """Update datasets to include the container_images JSON field.

    Update datasets found at input_path to include the container_images JSON field
    and store the updated datasets at output_path.

    Example:

    \b
    $ ./utils/update_fixtures_container_images.py \\
         -i ../opendata.cern.ch/cernopendata/modules/fixtures/data/records \\
         -o ../opendata.cern.ch/cernopendata/modules/fixtures/data/records
    """
    # find paths to all datasets that need to be updated
    find_datasets_cmd = f'find {input_path} -type f -name "cms-*-datasets*.json"'
    target_datasets_paths = subprocess.getoutput(find_datasets_cmd).split("\n")

    # make a temporary directory to hold source records
    tmp_source_records_dir = "/tmp/source-records"
    isExist = os.path.exists(tmp_source_records_dir)
    if not isExist:
        os.mkdir(tmp_source_records_dir)

    # get container images info
    with open("./cms-release-info/cms_release_container_images_info.json") as f:
        container_images_info_json = f.read()
        container_images_info = json.loads(container_images_info_json)

    # amend target records of all target datasets
    for target_dataset_path in target_datasets_paths:
        # read target records
        target_dataset_basename = os.path.basename(target_dataset_path)[: -len(".json")]
        target_dataset_file = open(target_dataset_path, "r")
        target_dataset_content = target_dataset_file.read()
        target_dataset_file.close()
        target_records = json.loads(target_dataset_content)

        # prepare source records
        source_records = []
        releases_not_found = set()
        for record in target_records:
            source_record = {
                "title": record["title"],
                "system_details": record["system_details"],
            }

            release = record["system_details"]["release"].strip()
            if release not in container_images_info.keys():
                releases_not_found.add(release)
                continue
            source_record["system_details"]["container_images"] = container_images_info[
                release
            ]
            source_records.append(source_record)
        if len(releases_not_found) != 0:
            print(
                f"{target_dataset_basename}.json: could not find container images info for releases {releases_not_found}"
            )

        # save source records in a JSON file as required by update_fixtures.py
        source_records_json = json.dumps(
            source_records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
        source_records_path = (
            f"{tmp_source_records_dir}/{target_dataset_basename}_source.json"
        )
        source_records_file = open(source_records_path, "w")
        source_records_file.write(source_records_json + "\n")
        source_records_file.close()

        # amend taregt records using update_fixtures.py
        updated_dataset_path = f"{output_path}/{target_dataset_basename}.json"
        update_dataset_cmd = f"python3 ./utils/update_fixtures.py -s {source_records_path} -t {target_dataset_path} -m title -u system_details  > {updated_dataset_path}.NEW"
        p = subprocess.run(
            update_dataset_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if p.stderr:
            print(f"Error processing: {target_dataset_basename}.json")
            print(p.stderr.decode())
        os.rename(updated_dataset_path + ".NEW", updated_dataset_path)

    # remove temporary directory
    shutil.rmtree(tmp_source_records_dir)


if __name__ == "__main__":
    main()
