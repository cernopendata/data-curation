#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS trigger information record's modification script.
"""

LINK_INFO = {}
exec(open('./outputs/hlt_config_files_link_info.py', 'r').read())


def main():
    """Do the main job."""
    for title, recid in LINK_INFO.items():
        print("""sed -i -e 's,<a href=\\\\\"/record/FIXME\\\\\">{0}</a>,<a href=\\\\\"/record/{1}\\\\\">{0}</a>,g' cernopendata/modules/fixtures/data/records/cms-trigger-information-2010.json""".format(title, recid))


if __name__ == '__main__':
    main()
