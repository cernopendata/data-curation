#!/usr/bin/env python

"""
Interface for manipulation of dataset records.
"""

import click
import os


@click.command()
@click.argument('dataset-list', type=click.Path(exists=True))
@click.argument('output-dir', default="./output/")
@click.option('--create-eos-indexes/--no-create-eos-indexes', default=False,
              show_default=True,
              help="Create EOS rich index files")
@click.option('--eos-output-dir', default='./inputs/eos-file-indexes',
              show_default=True,
              help='Output directory for the EOS file indexes')
def main(dataset_list, output_dir, create_eos_indexes, eos_output_dir):
    """
    Interface for manipulation of dataset records for OpenData portal.

    DATASET_LIST is a text file with a list of datasets, one per line.

    OUTPUT_DIR is the desired output directory.

    There are several steps to produce the final json files.

    step 1) generate EOS index files for the datasets

        $ export EOS_MGM_URL=root://eospublic.cern.ch
        $ python ./code/interface.py --create-eos-indexes DATASET_LIST
    """
    if create_eos_indexes:
        import create_eos_file_indexes
        create_eos_file_indexes.OUTPUTDIR = eos_output_dir
        create_eos_file_indexes.INPUT = dataset_list

        if "EOS_MGM_URL" in os.environ:
            create_eos_file_indexes.main()
        else:
            print("EOS_MGM_URL not set.")
            print('Did you forget to "export EOS_MGM_URL=root://eospublic.cern.ch"?')

if __name__ == '__main__':
    main()