#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

import json

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open('./outputs/hlt_config_files_link_info.py', 'r').read())

RECID_START = 6200

RECORD_TEMPLATE = """\
  <record>
    <datafield tag="264" ind1=" " ind2="0">
        <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
        <subfield code="a">%(info)s</subfield>
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
      <subfield code="a">CERN-LHC</subfield>
      <subfield code="e">CMS</subfield>
    </datafield>
    <datafield tag="964" ind1=" " ind2="0">
      <subfield code="c">Run2011A</subfield>
    </datafield>
        <subfield code="b">Research</subfield>
    </datafield>
   </record>"""


def expand_links(atext):
    "Take text and expand links based on LINK_INFO."
    btext = atext
    for key in LINK_INFO.keys():
        if key in btext:
            btext = btext.replace(key, '<a href="/record/%d">%s</a>' % (LINK_INFO[key], key))
    return btext


def create_rich_abstract(title, info):
    """Create rich abstract out of info items."""
    out = ' '
    out += '<p>High-Level Trigger path information %s.</p>' % title
    if info:
        out += '<blockquote>'
        for item in info:
            out += '<p>' + expand_links(item) + '</p>'
        out += '</blockquote>'
    out += '<p>See also the full list of triggers for CMS 2012 open data:'
    out += '<a href="/record/1701">Trigger information for 2012 CMS open data</a></p>'
    return out + ''


def main():
    """Do the main job."""

    year_created = '2012'
    year_published = '2017'
    run_period = '2012RunB-2012RunC'

    records = []
    recid = RECID_START
    title = None
    info = []
    for line in open('./inputs/hlt-trigger-path.txt', 'r').readlines():
        if line.startswith('Path'):
            if title:

                rec = {}

                rec['abstract'] = {}
                rec['abstract']['description'] = create_rich_abstract(title, info)

                rec['accelerator'] = "CERN-LHC"

                rec['collaboration'] = {}
                rec['collaboration']['name'] = 'CMS collaboration'
                rec['collaboration']['recid'] = '451'

                rec['collections'] = ['CMS-Trigger-Information', ]

                rec['collision_information'] = {}
                rec['collision_information']['energy'] = '8TeV'
                rec['collision_information']['type'] = 'pp'

                rec['date_created'] = year_created
                rec['date_published'] = year_published

                rec['experiment'] = 'CMS'

                rec['publisher'] = 'CERN Open Data Portal'

                rec['recid'] = str(recid)

                rec['run_period'] = run_period

                rec['title'] = 'High-Level Trigger path information ' + title

                rec['type'] = {}
                rec['type']['primary'] = 'Supplementaries'
                rec['type']['secondary'] = ['Trigger', ]

                records.append(rec)

                recid += 1
                info = []

            title = line.split(' ', 1)[1].strip()
            if title.endswith(':'):
                title = title[:-1]
        elif line.startswith(' - '):
            info.append(line[2:].strip())
        else:
            pass

    print(json.dumps(records, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
