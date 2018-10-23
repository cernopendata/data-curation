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
@click.option('--get-conf-files/--no-get-conf-files',
              default=False, show_default=True,
              help='Get configuration files for the datasets')
@click.option('--conf-dir', default='./inputs/config-store',
              show_default=True,
              help='Output directory for the configuration files')
def main(dataset_list, output_dir,
         create_eos_indexes, eos_dir,
         create_das_json_store, das_dir,
         get_conf_files, conf_dir):
    """
    Interface for manipulation of dataset records for OpenData portal.

    DATASET_LIST is a text file with a list of datasets, one per line.

    OUTPUT_DIR is the desired output directory.

    There are several steps to produce the final json files.

    step 1) generate EOS index files for the datasets

        \b
        $ export EOS_MGM_URL=root://eospublic.cern.ch
        $ python ./code/interface.py --create-eos-indexes DATASET_LIST

        This will populate EOS_DIR with a txt and json file for each dataset.
        The files contain list of root files of that dataset.

    step 2) get DAS metadata

        \b
        $ voms-proxy-init -voms cms -rfc
        $ python ./code/interface.py --create-das-json-store DATASET_LIST

        This creates a local cache. It queries DAS (Data Aggregation Service)
        for the dataset, parent, config and mcm information and store it in
        das-dir/{dataset/,parent/,config/,mcm/}.

        (It takes a lot of time to run)

    setp 3) get the config files

        \b
        $ voms-proxy-init -voms cms -rfc
        $ python ./code/interface.py --get-conf-files DATASET_LIST

    But you can also run everything in one go, assuming the voms-proxy lasts
    long enough:

        \b
        $ export EOS_MGM_URL=root://eospublic.cern.ch
        $ voms-proxy-init -voms cms -rfc
        $ python ./code/interface.py --create-eos-indexes \\
                                     --create-das-json-store \\
                                     --get-conf-files \\
                                     DATASET_LIST
    """
    datasets = get_datasets_from_dir(dataset_list)

    if create_eos_indexes:
        import create_eos_file_indexes
        create_eos_file_indexes.OUTPUTDIR = eos_dir
        create_eos_file_indexes.INPUT = dataset_list

        if os.environ.get("EOS_MGM_URL") == "root://eospublic.cern.ch":
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

    if get_conf_files:
        # check if user has voms-proxy
        proxyinfo = subprocess.run("voms-proxy-info", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if proxyinfo.returncode != 0:
            print("Error in VOMS proxy.")
            print('Did you forget to "voms-proxy-init -voms cms -rfc"?')
        else:
            import config_store
            config_store.main(eos_dir, das_dir, conf_dir, datasets)


if __name__ == '__main__':
    main()