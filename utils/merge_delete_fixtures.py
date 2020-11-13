#!/usr/bin/python3

"""A helper script for merging and deleting record fixtures.

This helper script is useful for merging and deleting selected JSON
fields in the CERN Open Data record fixtures.

For example, if one wishes to merge "note" to "description", only needs to
provide information e.x input file (JSON), full path to "note" and
"description", wrap symbol for separating two texts, path to the node
that later will be deleted.

"""

import click
import json
import logging
import codecs
import os


@click.command()
@click.option('--input_file', '-f', required=True,
              help='File to read data from')
@click.option('--source_path', '-sp', required=True,
              help='Source path to the node you want to copy \
              from (ex. "note&description")')
@click.option('--target_path', '-tp', required=True,
              help='Target path to the node you want to concatenates \
              source to (ex. "abstract&description")')
@click.option('--delete_path', '-dp', required=True,
              help='Path to the node you want to delete (ex. "note")')
@click.option('--wrap_symbol', '-ws', required=True,
              help='Symbol you want wrap source text arround \
              (ex. "<p>&</p>" will result in "<p>Some text in source</p>)"')
def main(input_file, source_path, target_path, delete_path, wrap_symbol):
    r"""Merge and delete record fixtures.

    Saves processed file in ./output directory, which must be created before
    running script in the same directory.
    \b
    $ python ./merge_delete_fixtures.py \\
                -f ./input/cms-hlt-configuration-files-2012.json \\
                -sp "note&description" \\
                -tp "abstract&description" \\
                -dp "note" \\
                -ws "<p>&</p>" \\
    """
    input_paths = input_file.split("/")
    source_paths = source_path.split("&")
    target_paths = target_path.split("&")
    wrap_symbols = wrap_symbol.split("&")
    delete_paths = delete_path.split("&")

    # read input file
    content = open(input_file, 'r').read()
    records = json.loads(content)

    # concatenate and delete records
    for record in records:
        try:
            value = get_nested_value(record, source_paths)
            wraped_value = text_wrapper(value, wrap_symbols)
            record = concat_nested_value(record, target_paths, wraped_value)
            record = delete_nested_value(record, delete_paths)
        except KeyError:
            logging.error("Path you specified not found! Will continue to \
            the next record...")

    write_file(records, input_paths[-1])


def text_wrapper(val, symb):
    """Wrap text in any tag user provided with (e.g. <p>Some text</p>)."""
    return symb[0] + val + symb[1]


def get_nested_value(records, source_paths):
    """Retrieve value from nested JSON records."""
    for path in source_paths:
        records = records[path]
    return records


def concat_nested_value(records, target_paths, value):
    """Concatenate given path to target_path with specified value."""
    if len(target_paths) == 1:
        records[target_paths[0]] = ' '.join([records[target_paths[0]], value])
        return records
    else:
        records[target_paths[0]] = concat_nested_value(
          records[target_paths[0]], target_paths[1:], value)
        return records


def delete_nested_value(records, delete_paths):
    """Delete nested node from the specified path."""
    if len(delete_paths) == 1:
        return records.pop(delete_paths[0], None)
    else:
        return delete_nested_value(records[delete_paths[0]], delete_paths[1:])


def write_file(records, file_name):
    """Save JSON to file."""
    full_path = os.path.abspath(os.path.join("outputs", file_name))
    with codecs.open(full_path, 'w', encoding='utf-8') as f:
        json.dump(records,
                  f,
                  ensure_ascii=False,
                  indent=2,
                  sort_keys=True,
                  separators=(',', ': '))


if __name__ == '__main__':
    main()
