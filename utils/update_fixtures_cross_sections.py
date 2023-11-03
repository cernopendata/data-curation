#!/usr/bin/env python3

"""Helper script for creating cross_section JSON field of simulated dataset record fixutres.

This helper script is useful for creating/updating the cross_sections JSON field in
the CMS 2015 simulated datasets found in the CERN Open Data record fixtures.

"""

import os
import subprocess
import click
import json


@click.command()
@click.option(
    "--cross_sections_path",
    "-c",
    required=True,
    help="Relative path to the cross-section values json files directory",
)
@click.option(
    "--input_path", "-i", required=True, help="Relative path to the input directory"
)
@click.option(
    "--output_path", "-o", required=True, help="Relative path to the output directory"
)
def main(cross_sections_path, input_path, output_path):  # noqa: D301,D412
    """Update datasets to include the cross_sections JSON field.

    Update datasets found at input_path to include the cross_sections JSON field
    and store the updated datasets at output_path.

    Example:

    \b
    $ ./utils/update_fixtures_cross_sections.py \\
         -c ../MC2015/StandardModelPhysics
         -i ../opendata.cern.ch/cernopendata/modules/fixtures/data/records \\
         -o ../opendata.cern.ch/cernopendata/modules/fixtures/data/records
    """
    # rename cross-section values json files to their corresponding dataset names to make rest of code simpler
    total_cross_section_files = 0
    sub_categories = os.listdir(cross_sections_path)
    for categ in sub_categories:
        for json_file_name in os.listdir(f"{cross_sections_path}/{categ}"):
            total_cross_section_files += 1
            json_file = open(f"{cross_sections_path}/{categ}/{json_file_name}", "r")
            json_file_content = json_file.read()
            json_file.close()

            json_record = json.loads(json_file_content)
            dataset = json_record[0]["metadata"]["Dataset"]

            new_file_name = f"{dataset.replace('/', '$')}.json"
            if new_file_name[0] != "$":
                new_file_name = "$" + new_file_name
            os.rename(
                f"{cross_sections_path}/{categ}/{json_file_name}",
                f"{cross_sections_path}/{categ}/{new_file_name}",
            )

    # find paths to all datasets that need to be updated
    find_datasets_cmd = (
        f'find {input_path} -type f -name "cms-simulated-datasets-2015*.json"'
    )
    target_datasets_paths = subprocess.getoutput(find_datasets_cmd).split("\n")

    total_datasets_amended = 0
    total_format1 = 0
    total_format2 = 0
    total_format3 = 0
    total_format4 = 0
    total_format5 = 0
    total_format6 = 0

    # amend target records of all target datasets
    for target_dataset_path in target_datasets_paths:
        # read target records
        target_dataset_basename = os.path.basename(target_dataset_path)[: -len(".json")]
        target_dataset_file = open(target_dataset_path, "r")
        target_dataset_content = target_dataset_file.read()
        target_dataset_file.close()
        target_records = json.loads(target_dataset_content)
        print(f"Processing {target_dataset_basename}...")

        # add cross_section metadata field
        new_target_records = []
        for record in target_records:
            # find the record's corresponding cross-section values json file
            cross_sections_file_name = record["title"].replace("/", "$")
            find_cross_sections_cmd = (
                f"find {cross_sections_path} -name '{cross_sections_file_name}.json'"
            )
            cross_sections_file = subprocess.getoutput(find_cross_sections_cmd)

            if not cross_sections_file:
                new_target_records.append(record)
                continue

            cross_sections_json_file = open(f"{cross_sections_file}", "r")
            cross_sections_json_content = cross_sections_json_file.read()
            cross_sections_json_file.close()
            cross_sections_json_record = json.loads(cross_sections_json_content)
            cross_sections_json_data = cross_sections_json_record[1]

            record["cross_section"] = {}
            # check the presence of certain attributes to identify the format the file is in
            # see: https://github.com/Ari-mu-l/OpenData/tree/main
            # Format 1
            if (
                "totX_beforeMat" in cross_sections_json_data
                and "matchingEff" in cross_sections_json_data
            ):
                total_format1 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = (
                    cross_sections_json_data["matchingEff"]
                )
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff_weights"
                ]
                record["cross_section"]["neg_weight_fraction"] = (
                    cross_sections_json_data["negWeightFrac"]
                )
            # Format 2
            elif "totX_beforeMat" in cross_sections_json_data:
                total_format2 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = ""
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff_weights"
                ]
                record["cross_section"]["neg_weight_fraction"] = ""
            # Format 3
            elif (
                "totX_beforeFilter" in cross_sections_json_data
                and "negWeightFrac" in cross_sections_json_data
            ):
                total_format3 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = ""
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff_weights"
                ]
                record["cross_section"]["neg_weight_fraction"] = (
                    cross_sections_json_data["negWeightFrac"]
                )
            # Format 6 (unlisted format, but it is there in some json files)
            elif "filterEff(weights)" in cross_sections_json_data:
                total_format6 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = ""
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff(weights)"
                ]
                record["cross_section"]["neg_weight_fraction"] = ""
            # Format 4
            elif "totX_beforeFilter" in cross_sections_json_data:
                total_format4 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = ""
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff_weights"
                ]
                record["cross_section"]["neg_weight_fraction"] = ""
            # Format 5
            else:
                total_format5 += 1
                record["cross_section"]["total_value"] = cross_sections_json_data[
                    "totX_final"
                ]
                record["cross_section"]["total_value_uncertainty"] = (
                    cross_sections_json_data["totX_final_err"]
                )
                record["cross_section"]["matching_efficiency"] = ""
                record["cross_section"]["filter_efficiency"] = cross_sections_json_data[
                    "filterEff_weights"
                ]
                record["cross_section"]["neg_weight_fraction"] = ""

            new_target_records.append(record)
            total_datasets_amended += 1

        # save the amended dataset
        new_dataset_json = json.dumps(
            new_target_records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )

        updated_dataset_path = f"{output_path}/{target_dataset_basename}.json"
        new_dataset_file = open(updated_dataset_path, "w")
        new_dataset_file.write(new_dataset_json + "\n")
        new_dataset_file.close()

        # clean resulting JSON file
        if os.path.exists("../opendata.cern.ch/scripts/clean_json_file.py"):
            os.system(
                f"../opendata.cern.ch/scripts/clean_json_file.py {updated_dataset_path}"
            )

    print(
        f"Total number of cross-section values json files: {total_cross_section_files}, Total number of amended datasets: {total_datasets_amended}"
    )
    print(f"Total number of datasets amended using Format 1: {total_format1}")
    print(f"Total number of datasets amended using Format 2: {total_format2}")
    print(f"Total number of datasets amended using Format 3: {total_format3}")
    print(f"Total number of datasets amended using Format 4: {total_format4}")
    print(f"Total number of datasets amended using Format 5: {total_format5}")
    print(f"Total number of datasets amended using Format 6: {total_format6}")


if __name__ == "__main__":
    main()
