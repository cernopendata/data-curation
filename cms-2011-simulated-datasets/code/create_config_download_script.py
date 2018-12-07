#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create config download script.
"""

from create_das_json_store import get_das_json, get_from_deep_json

CFG_CMSWEBURL = 'https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/'


def get_config_urls(das):
    urls = []
    config_ids = get_from_deep_json(das, 'config_id')
    if isinstance(config_ids, str):
        config_ids = [config_ids, ]
    if config_ids:
        for config_id in config_ids:
            cmd = 'curl -o ./inputs/config-store/%s.configFile -k '\
                  '--key /tmp/x509up_u5073 '\
                  '--cert /tmp/x509up_u5073 "%s/%s/configFile"' % \
                  (config_id, CFG_CMSWEBURL, config_id)
            urls.append(cmd)
    return urls


def get_input_dataset(das):
    return get_from_deep_json(das, 'input_dataset')


def main():
    """Generate script to download DAS configurations for Kati."""

    print "#!/bin/sh"
    print "mkdir -p ./inputs/config-store"

    def print_cmd_for_dataset(title):
        das = get_das_json(title)
        config_urls = get_config_urls(das)
        if not config_urls:
            print '[ERROR] No config for dataset %s.' % title
        for url in get_config_urls(das):
            print url
        return get_input_dataset(das)

    for title in open('./inputs/cms-mc-nov-2015.txt', 'r').readlines():
        title = title.strip()
        input_dataset = title
        while input_dataset:
            input_dataset = print_cmd_for_dataset(input_dataset)


if __name__ == '__main__':
    main()
