#!/usr/bin/python3

"""A helper script for creating generic EOS file indexes.

This helper script is useful for creating generic EOS index files for
individual use cases. Note that various upload campaigns contain their own file
index creation scripts as well.
"""

import click
import json
import os
import re
import subprocess


def get_dataset_files(directory, extension='', pattern=''):  # noqa: E501
    """Return file list with information about name, size, URI.

    Handle all files in the DIRECTORY that have given file EXTENSION.
    """
    files = []
    output = subprocess.getoutput('eos find --xurl --size --checksum ' +
                                  directory)
    for line in output.split('\n'):
        if line and line != 'file-indexes':
            match = re.match(r'^path=(.*) size=(.*) checksum=(.*)$', line)
            if match:
                path, size, checksum = match.groups()
                if extension and path.endswith(extension):
                    # detect file URI
                    uri = path
                    if extension == 'h5':
                        # prefer to expose HTTP instead of XRootD
                        uri = path.replace(
                            'root://eospublic.cern.ch//eos/opendata/',
                            'http://opendata.cern.ch/eos/opendata/')
                    # detect file name
                    filename = os.path.basename(path)
                    if pattern and pattern not in filename:
                        # exclude files not matching pattern
                        continue
                    files.append({'filename': filename,
                                  'size': int(size),
                                  'checksum': 'adler32:' + checksum,
                                  'uri': uri})
    return files


def create_index_file(name, directory, extension, style='txt', pattern=''):
    """Create index file in the given style format (text, json)."""
    files = get_dataset_files(directory, extension, pattern)
    filebase = name + '_' + extension + '_file_index'
    filename = filebase + '.' + style
    fdesc = open(filename, 'w')
    if style == 'txt':
        for afile in files:
            fdesc.write(afile['uri'])
            fdesc.write('\n')
    elif style == 'json':
        content = json.dumps(files, indent=2, sort_keys=True,
                             ensure_ascii=False, separators=(',', ': '))
        fdesc.write(content + '\n')
    fdesc.close()
    return filename


@click.command()
@click.option('--name', '-n', required=True,
              help='Which datset name? E.g. HiggsToBBNTuple_HiggsToBB_QCD_RunII_13TeV_MC_test')  # noqa: E501
@click.option('--directory', '-d', required=True,
              help='Which directory? E.g. /eos/opendata/cms/datascience/HiggsToBBNTuple_HiggsToBB_QCD_RunII_13TeV_MC/test/')  # noqa: E501
@click.option('--extension', '-e', required=True,
              help='Which file extension? E.g. h5.')
@click.option('--pattern', '-p',
              help='Which file pattern to match? Optional. E.g. detachedTripletStepHitDoublets')  # noqa: E501
def main(name, directory, extension, pattern=''):  # noqa: D301
    """Create file list index files for given directory and file extension."""
    create_index_file(name, directory, extension, 'txt', pattern)
    create_index_file(name, directory, extension, 'json', pattern)


if __name__ == '__main__':
    main()
