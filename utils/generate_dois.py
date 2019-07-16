#!/usr/bin/env python2

"""Verify whether records need DOI generation.

If a dataset record contains 'files' and does not have 'doi' yet, generate one.

Print record fixtures updated with the generated DOI.

Note: to be run on datasets, software examples, and the like.  Not on
configuration files and the like.

Note: to be run inside the container after setting
APP_PIDSTORE_DATACITE_DOI_PREFIX=10.7483 properly in
fully loaded COD instance.
"""

import json
import subprocess

import click


def generate_doi(experiment=''):
    """Return generated DOI for given experiment."""
    cmd = 'cernopendata datacite gen-doi'
    if experiment:
        cmd += ' --exp {0}'.format(experiment)
    return subprocess.check_output(cmd, shell=True).decode().rstrip('\r\n')


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('experiment', default='')
def generate_dois_if_needed(filename, experiment):
    """Verify whether records need DOI generation.

    If a dataset record contains 'files' and does not have 'doi' yet,
    generate one.  If 'experiment' is provided, use that for prefix.

    Print record fixtures updated with the generated DOI.

    Note: to be run on datasets, software examples, and the like.  Not on
    configuration files and the like.
    """
    with open(filename, 'r') as fdesc:
        records = json.loads(fdesc.read())

    changes_needed = False
    new_dois = []
    for record in records:
        # get information
        recid = record.get('recid')
        doi = record.get('doi')
        files = record.get('files', None)
        # check record
        if files and not doi:
            changes_needed = True
            print("[INFO] Record %s has 'files' but no 'doi'."
                  " Minting one." % recid)

            while True:
                new_doi = generate_doi(experiment)
                if new_doi not in new_dois:
                    new_dois.append(new_doi)
                    record['doi'] = new_doi
                    break

    if changes_needed:
        new_content = json.dumps(records, indent=2, sort_keys=True,
                                 ensure_ascii=True, separators=(',', ': '))
        with open(filename, 'w') as fdesc:
            fdesc.write(new_content + '\n')


if __name__ == '__main__':
    generate_dois_if_needed()
