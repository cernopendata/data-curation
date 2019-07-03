#!/usr/bin/python3


"""A helper script to update CMS 2011 MC generator information.

Port generator information from ``generator`` field to
``methodology.steps.generators`` field as for the other 2010 2012 etc MC
records.
"""

import click
import json


@click.command()
@click.option('--source', '-s', required=True,
              help='Source of information? [file1]')
def main(source):  # noqa: D301
    """A helper script to update generator information."""
    # read source
    content = open(source, 'r').read()
    records = json.loads(content)

    # amend records
    for record in records:
        if 'methodology' in record.keys():
            methodology_steps = record['methodology']['steps']
            for methodology_step in methodology_steps:
                if methodology_step['type'] == 'SIM':
                    methodology_step['generators'] = record['generator']['names']
                    del(record['generator'])

    # print records
    new_content = json.dumps(records, indent=2, sort_keys=True,
                             ensure_ascii=False)
    for line in new_content.split('\n'):
        line = line.rstrip()
        print(line)


if __name__ == '__main__':
    main()
