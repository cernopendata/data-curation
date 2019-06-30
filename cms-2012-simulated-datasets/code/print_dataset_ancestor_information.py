#!/usr/bin/env python3

"""
Print information about dataset ancestors.
"""

import subprocess

from create_dataset_records import \
    get_dataset_index_file_base, \
    get_parent_dataset, \
    newer_dataset_version_exists


def get_oldest_ancestor_dataset(dataset):
    """Find oldest ancestor of the dataset."""
    output = dataset
    parent_dataset = get_parent_dataset(output)
    while parent_dataset:
        output = parent_dataset
        print('    - Parent dataset: [%s](%s)' %
              (output,
               'https://cmsweb.cern.ch/das/request?view=list&limit=5&instance=prod%2Fglobal&input=' + quote(output, safe='')))
        generator_parameters = get_generator_parameters(output)
        if generator_parameters:
            print('        - Generator parameters:')
            print('            - Cross section:', generator_parameters.get('cross_section', None))
            print('            - Filter efficiency:', generator_parameters.get('filter_efficiency', None))
            print('            - Filter efficiency error:', generator_parameters.get('filter_efficiency_error', None))
            print('            - Match efficiency:', generator_parameters.get('match_efficiency', None))
            print('            - Match efficiency error:', generator_parameters.get('match_efficiency_error', None))
        for conffile_id in get_conffile_ids(output):
            conffile_location = get_conffile_location_from_conffile_id(conffile_id)
            if not get_conffile_content(conffile_id):
                download_config_file(conffile_id)
            print('        - Configuration file: [%s](%s)' % (conffile_id,
                                                              conffile_location))
            print('            - Process: %s' % get_conffile_process(conffile_id))
            print('            - Python filename: %s' % get_conffile_python_filename(conffile_id))
        parent_dataset = get_parent_dataset(output)
    return output


def main():
    "Do the job."
    for line in open('./inputs/mc-datasets-selected-for-18-dec-2017-release.txt', 'r').readlines():
        dataset_full_name = line.strip()
        parent_dataset = get_parent_dataset(dataset_full_name)
        grandparent_dataset = get_parent_dataset(parent_dataset)
        print('* Dataset: ' + dataset_full_name)
        try:
            print('** Parent: ' + parent_dataset)
        except:
            print('** No parent dataset')
        try:
            print('*** Grandparent: ' + grandparent_dataset)
        except:
            print('*** No grandparent dataset')
        print('')


if __name__ == '__main__':
    main()
