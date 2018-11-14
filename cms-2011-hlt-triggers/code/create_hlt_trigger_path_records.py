#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

LINK_INFO = {
    '/cdaq/physics/Run2011/1e33/v2.4/HLT/V4': 3500,
    '/cdaq/physics/Run2011/1.4e33/v1.1/HLT/V1': 3501,
    '/cdaq/physics/Run2011/2e33/v1.2/HLT/V1': 3502,
    '/cdaq/physics/Run2011/5e33/v2.2/HLT/V4': 3503,
    '/cdaq/physics/Run2011/5e32/v4.3/HLT/V4': 3504,
    '/cdaq/physics/Run2011/5e32/v8.1/HLT/V6': 3505,
    '/cdaq/physics/Run2011HI/v1.1/HIHLT/V1': 3506,
    '/cdaq/physics/Run2011/2e33/v1.2/HLT/V7': 3507,
    '/cdaq/physics/Run2011/5e32/v6.2/HLT/V2': 3508,
    '/cdaq/physics/Run2011/5e32/v6.2/HLT/V3': 3509,
    '/cdaq/physics/Run2011/3e33/v1.2/HLT/V1': 3510,
    '/cdaq/physics/Run2011/3e33/v2.2/HLT/V2': 3511,
    '/cdaq/physics/Run2011/3e33/v4.0/HLT/V6': 3512,
    '/cdaq/physics/Run2011/5e32/v6.1/HLT/V6': 3513,
    '/cdaq/physics/Run2011/5e32/v8.3/HLT/V3': 3514,
    '/cdaq/physics/Run2011/5e32/v8.2/HLT/V3': 3515,
    '/cdaq/physics/Run2011HI/v1.0/HIHLT/V3': 3516,
    '/cdaq/physics/Run2011/5e32/v4.2/HLT/V5': 3517,
    '/cdaq/physics/Run2011/5e32/v5.3/HLT/V2': 3518,
    '/cdaq/physics/Run2011/2e33/v1.2/HLT/V4': 3519,
    '/cdaq/physics/Run2011HI/v1.7/HIHLT/V1': 3520,
    '/cdaq/physics/Run2011/5e32/v4.2/HLT/V2': 3521,
    '/cdaq/physics/Run2011/5e33/v2.2/HLT/V2': 3522,
    '/cdaq/physics/Run2011/1e33/v1.3/HLT/V2': 3523,
    '/cdaq/physics/Run2011/5e32/v5.3/HLT/V1': 3524,
    '/cdaq/physics/Run2011/1.4e33/v1.2/HLT/V1': 3525,
    '/cdaq/physics/Run2011/1e33/v2.4/HLT/V8': 3526,
    '/cdaq/physics/Run2011/1e33/v2.4/HLT/V5': 3527,
    '/cdaq/physics/Run2011/3e33/v1.1/HLT/V3': 3528,
    '/cdaq/physics/Run2011HI/v1.4/HIHLT/V1': 3529,
    '/cdaq/physics/Run2011/1e33/v1.3/HLT/V12': 3530,
    '/cdaq/physics/Run2011/3e33/v3.0/HLT/V2': 3531,
    '/cdaq/physics/Run2011HI/v1.6/HIHLT/V2': 3532,
    '/cdaq/physics/Run2011/1e33/v2.4/HLT/V6': 3533,
    '/cdaq/physics/Run2011/5e32/v8.1/HLT/V8': 3534,
    '/cdaq/physics/Run2011/1e33/v1.3/HLT/V6': 3535,
    '/cdaq/physics/Run2011/3e33/v2.0/HLT/V7': 3536,
    '/cdaq/physics/Run2011/3e33/v3.1/HLT/V1': 3537,
    '/cdaq/physics/Run2011/5e32/v4.2/HLT/V7': 3538,
    '/cdaq/physics/Run2011HI/2760GeV/v1.1/HLT/V4': 3539,
    '/cdaq/physics/Run2011HI/2760GeV/v1.1/HLT/V1': 3540,
    '/cdaq/physics/Run2011/3e33/v4.0/HLT/V5': 3541,
    '/cdaq/physics/Run2011/3e33/v2.1/HLT/V2': 3542,
    '/cdaq/physics/Run2011/5e32/v5.2/HLT/V7': 3543,
    '/cdaq/physics/Run2011/1e33/v2.5/HLT/V1': 3544,
    '/cdaq/physics/Run2011/2e33/v1.2/HLT/V5': 3545,
    '/cdaq/physics/Run2011HI/v1.3/HIHLT/V5': 3546,
    '/cdaq/physics/Run2011HI/v1.2/HIHLT/V2': 3547,
    '/cdaq/physics/Run2011/1e33/v2.4/HLT/V2': 3548,
    '/cdaq/physics/Run2011/5e32/v5.1/HLT/V3': 3549,
    '/cdaq/physics/Run2011/5e32/v6.1/HLT/V3': 3550,
    '/cdaq/physics/Run2011/2e33/v1.1/HLT/V1': 3551,
    '/cdaq/physics/Run2011/5e32/v5.2/HLT/V5': 3552,
    '/cdaq/physics/Run2011/1e33/v1.3/HLT/V13': 3553,
    '/cdaq/physics/Run2011/5e32/v4.2/HLT/V6': 3554,
    '/cdaq/physics/Run2011/5e32/v6.1/HLT/V1': 3555,
    '/cdaq/physics/Run2011/3e33/v1.1/HLT/V1': 3556,
    '/cdaq/physics/Run2011/2e33/v1.1/HLT/V2': 3557,
    '/cdaq/physics/Run2011/5e32/v6.2/HLT/V4': 3558,
    '/cdaq/physics/Run2011/5e32/v4.2/HLT/V8': 3559,
    '/cdaq/physics/Run2011HI/v1.3/HIHLT/V1': 3560,
    '/cdaq/physics/Run2011/3e33/v5.0/HLT/V1': 3561,
    '/cdaq/physics/Run2011/1.4e33/v1.2/HLT/V3': 3562,
    '/cdaq/physics/Run2011/5e32/v8.3/HLT/V2': 3563,
    '/cdaq/physics/Run2011HI/v1.0/HIHLT/V2': 3564,
    '/cdaq/physics/Run2011HI/2760GeV/v1.1/HLT/V3': 3565,
    '/cdaq/physics/Run2011/5e32/v8.1/HLT/V5': 3566,
    '/cdaq/physics/Run2011/3e33/v4.0/HLT/V2': 3567,
    '/cdaq/physics/Run2011/3e33/v4.0/HLT/V3': 3568,
    '/cdaq/physics/Run2011/5e32/v6.1/HLT/V5': 3569,
    '/cdaq/physics/Run2011/5e32/v5.2/HLT/V6': 3570,
    '/cdaq/physics/Run2011/5e33/v1.4/HLT/V3': 3571,
    '/cdaq/physics/Run2011/1e33/v1.3/HLT/V7': 3572,
    '/cdaq/physics/Run2011/5e32/v4.3/HLT/V3': 3573,
    '/cdaq/physics/Run2011/5e33/v1.4/HLT/V5': 3574,
    '/cdaq/physics/Run2011/1e33/v2.3/HLT/V3': 3575,
    '/cdaq/physics/Run2011/3e33/v2.3/HLT/V2': 3576,
    '/cdaq/physics/Run2011/3e33/v2.0/HLT/V4': 3577,
    '/cdaq/physics/Run2011/3e33/v2.2/HLT/V3': 3578,
    '/cdaq/physics/Run2011/3e33/v2.1/HLT/V1': 3579,
    '/cdaq/physics/Run2011/5e32/v8.3/HLT/V4': 3580,
    '/cdaq/physics/Run2011/3e33/v1.1/HLT/V4': 3581,
    '/cdaq/physics/Run2011HI/v1.6/HIHLT/V1': 3582,
    '/cdaq/physics/Run2011/1e33/v2.3/HLT/V1': 3583,
    '/cdaq/physics/Run2011/5e32/v5.2/HLT/V2': 3584,
}

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="w">451</subfield>
        <subfield code="a">CMS collaboration</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">High-Level Trigger path information %(title)s</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="b">CERN Open Data Portal</subfield>
        <subfield code="c">2016</subfield>
    </datafield>
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
    <datafield tag="942" ind1=" " ind2=" ">
        <subfield code="e">7TeV</subfield>
    </datafield>
    <datafield tag="964" ind1=" " ind2="0">
      <subfield code="c">Run2011A</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="a">CMS-Trigger-Information</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
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
    out = '<![CDATA[ '
    out += '<p>High-Level Trigger path information %s.</p>' % title
    if info:
        out += '<blockquote>'
        for item in info:
            out += '<p>' + expand_links(item) + '</p>'
        out += '</blockquote>'
    out += '<p>See also the full list of triggers for CMS 2011 open data:'
    out += '<a href="/record/1700">Trigger information for 2011 CMS open data</a></p>'
    return out + ']]>'


def main():
    """Do the main job."""

    recid = 2000
    title = None
    info = []
    print '  <collection>'
    for line in open('./inputs/trigger-path.txt', 'r').readlines():
        if line.startswith('Path'):
            if title:
                print RECORD_TEMPLATE % \
                    {'recid': recid,
                     'title': title,
                     'info': create_rich_abstract(title, info)}
                recid += 1
                info = []
            title = line.split(' ', 1)[1].strip()
            if title.endswith(':'):
                title = title[:-1]
        elif line.startswith(' - '):
            info.append(line[2:].strip())
        else:
            pass
    print '  </collection>'


if __name__ == '__main__':
    main()
