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
@click.option('--create-eos-indexes/--no-create-eos-indexes', default=False,
              show_default=True,
              help="Create EOS rich index files")
@click.option('--eos-dir', default='./inputs/eos-file-indexes/',
              show_default=True,
              help='Output directory for the EOS file indexes')
@click.option('--ignore-eos-store/--no-ignore-eos-store',
              show_default=True, default=False,
              help='Presence of EOS file indexes')
@click.option('--create-das-json-store/--no-create-das-json-store',
              default=False, show_default=True,
              help="Get DAS json information")
@click.option('--das-dir', default='./inputs/das-json-store',
              show_default=True,
              help='Output directory for the DAS metadata')
@click.option('--create-mcm-store/--no-create-mcm-store',
              default=False, show_default=True,
              help="Get McM json information")
@click.option('--mcm-dir', default='./inputs/mcm-store',
              show_default=True,
              help='Output directory for the DAS metadata')
@click.option('--get-conf-files/--no-get-conf-files',
              default=False, show_default=True,
              help='Get configuration files for the datasets')
@click.option('--conf-dir', default='./inputs/config-store',
              show_default=True,
              help='Output directory for the configuration files')
@click.option('--print-categorisation', default=False,
              show_default=True, is_flag=True,
              help='Print results of categorisation')
@click.option('--print-results', default=False,
              show_default=True, is_flag=True,
              help='Print results of categorisation with gen info')
@click.option('--create-records', default=False,
              show_default=True, is_flag=True,
              help='Create json file for records')
@click.option('--create-conffile-records', default=False,
              show_default=True, is_flag=True,
              help='Create json file for conffiles')
@click.option('--recid-file', default="./inputs/recid_info.py",
              show_default=True, type=click.Path(),
              help='File with record IDs')
@click.option('--doi-file', default='./inputs/doi-sim.txt',
              show_default=True, type=click.Path(),
              help='File with DOI information')
def main(dataset_list,
         create_eos_indexes, eos_dir, ignore_eos_store,
         create_das_json_store, das_dir,
         create_mcm_store, mcm_dir,
         get_conf_files, conf_dir,
         print_categorisation, print_results,
         create_records,
         create_conffile_records,
         recid_file, doi_file):
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
        for the dataset, parent, and release information and store it in
        DAS_DIR/{dataset/,parent/,release/}.

        \b
        (It takes a lot of time to run, up to ~30 seconds / dataset)

    step 3) get McM scripts to run cmsDriver

        \b
        $ python ./code/interface.py --create-mcm-store DATASET_LIST

        This will query McM to get the dict and setup scripts for each dataset.
        It also queries the input_dataset (GEN-SIM).

    step 4) get the config files

        \b
        in ~/.globus/ dir, follow the instructions from
        https://ca.cern.ch/ca/help/?kbid=024010 and also this other command:
        $ openssl pkcs12 -in myCert.p12 -nocerts -nodes -out userkey.nodes.pem
        Then run the interface code

        $ python ./code/interface.py --get-conf-files DATASET_LIST

        This downloads the configuration files to CONF_DIR.

    step 5) generate the records

        \b
        $ python ./code/interface.py --create-records DATASET_LIST
        $ python ./code/interface.py --create-conffile-records DATASET_LIST

    To get a markdown file with the results of the previous steps:

        $ python ./code/interface.py --print-results DATASET_LIST

        This will use all the information from the local cache to produe a list
        with all the datasets in their categories, with as much additional
        information as we got.

    In case you are interested only in the categorisation, there is no need
    to create the local cache, just run:

        $ python ./code/interface.py --print-categorisation DATASET_LIST > categorisation.md
    """
    datasets = get_datasets_from_dir(dataset_list)

    if create_eos_indexes:
        import eos_store

        if os.environ.get("EOS_MGM_URL") == "root://eospublic.cern.ch":
            eos_store.main(datasets, eos_dir)
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
            das_json_store.main(das_dir, eos_dir, datasets, ignore_eos_store)

    if create_mcm_store:
        import mcm_store
        mcm_store.create(datasets, mcm_dir, eos_dir, ignore_eos_store)

    if get_conf_files:
        # check if user has key and cert
        if os.path.isfile(os.environ.get("HOME") + "/.globus/usercert.pem") and os.path.isfile(os.environ.get("HOME") + "/.globus/userkey.nodes.pem"):
            import config_store
            config_store.main(eos_dir, mcm_dir, conf_dir, datasets, ignore_eos_store)
        else:
            print("Error in key and certificate pairs (~/.globus/usercert.pem, ~/.globus/userkey.nodes.pem).")
            print('Did you forget to ')
            print("\t$ openssl pkcs12 -in myCert.p12 -clcerts -nokeys -out usercert.pem")
            print("\t$ openssl pkcs12 -in myCert.p12 -nocerts -nodes -out userkey.nodes.pem")
            print('in the ~/.globus dir?')

    if print_categorisation or print_results:
        import categorisation
        import printer

        categorised = categorisation.categorise_titles(datasets)
        printer.print_results(categorised, das_dir, mcm_dir, recid_file, doi_file, print_results)

    if create_records:
        import dataset_records
        dataset_records.main(datasets, eos_dir, das_dir, mcm_dir, conf_dir, doi_file, recid_file)

    if create_conffile_records:
        import conffiles_records
        conffiles_records.main(datasets, eos_dir, das_dir, mcm_dir, conf_dir)


if __name__ == '__main__':
    main()
