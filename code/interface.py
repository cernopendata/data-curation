#!/usr/bin/env python

"""
Interface for manipulation of dataset records.
"""

import click
import os
import subprocess
from utils import get_datasets_from_dir


@click.command()
@click.argument('dataset-list', type=click.Path(exists=True))
@click.argument('output-dir', default="./output/")
@click.option('--create-eos-indexes/--no-create-eos-indexes', default=False,
              show_default=True,
              help="Create EOS rich index files")
@click.option('--eos-dir', default='./inputs/eos-file-indexes',
              show_default=True,
              help='Output directory for the EOS file indexes')
@click.option('--create-das-json-store/--no-create-das-json-store',
              default=False, show_default=True,
              help="Get DAS json information")
@click.option('--das-dir', default='./inputs/das-json-store',
              show_default=True,
              help='Output directory for the DAS metadata')
def main(dataset_list, output_dir,
         create_eos_indexes, eos_dir,
         create_das_json_store, das_dir):
    """
    Interface for manipulation of dataset records for OpenData portal.

    DATASET_LIST is a text file with a list of datasets, one per line.

    OUTPUT_DIR is the desired output directory.

    There are several steps to produce the final json files.

    step 1) generate EOS index files for the datasets

        $ export EOS_MGM_URL=root://eospublic.cern.ch
        $ python ./code/interface.py --create-eos-indexes DATASET_LIST

        This will populate EOS_DIR with a txt and json file for each dataset
        with the list of root files.

    step 2) get DAS metadata

        $ voms-proxy-init -voms cms -rfc
        $ python ./code/interface.py --create-das-json-store DATASET_LIST
    """
    datasets = get_datasets_from_dir(dataset_list)

    if create_eos_indexes:
        import create_eos_file_indexes
        create_eos_file_indexes.OUTPUTDIR = eos_dir
        create_eos_file_indexes.INPUT = dataset_list

        if "EOS_MGM_URL" in os.environ:  # FIXME this does not check if user set the variable
            create_eos_file_indexes.main(datasets)
        else:
            print("EOS_MGM_URL not set.")
            print('Did you forget to "export EOS_MGM_URL=root://eospublic.cern.ch"?')

    if create_das_json_store:
        # check if user has voms-proxy
        proxyinfo = subprocess.run("voms-proxy-info", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if proxyinfo.returncode != 0:
            print("Error in VOMS proxy.")
            print('Did you forget to "voms-proxy-init -voms cms -rfc"?')
        else:
            import das_json_store
            das_json_store.main(das_dir, eos_dir, datasets)

if __name__ == '__main__':
    main()