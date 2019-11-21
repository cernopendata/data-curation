#!/usr/bin/env python

import hashlib
import json
import os
import zlib

EVENTDIR = './inputs/events'

template = """\
{
    "recid": "%(recid)s",
    "collaboration": {
        "name": "OPERA collaboration",
        "recid": "454"
    },
    "type": {
        "primary": "Dataset",
        "secondary": [
            "Derived"
        ]
    },
    "title": "OPERA electron neutrino event %(eventid)s",
    "title_additional": "OPERA electron neutrino event %(eventid)s",
    "distribution": {
        "formats": [
            "csv"
        ],
        "number_events": 1,
        "number_files": %(nbfiles)s,
        "size": %(nbbytes)s
    },
    "publisher": "CERN Open Data Portal",
    "date_published": "2019",
    "date_created": [
        "2008",
        "2009",
        "2010"
    ],
    "dataset_semantics": [
        {
            "variable": "amplL",
            "description": "PMT amplitude measured from the \\"left\\" side of a scintillator strip (in photo-electrons)"
        },
        {
            "variable": "amplR",
            "description": "PMT amplitude measured from the \\"right\\" side of a scintillator strip (in photo-electrons)"
        },
        {
            "variable": "amplRec",
            "description": "PMT amplitude reconstructed from the \\"left\\" and \\"right\\" side amplitudes of a scintillator strip taking into account light attenuation in a WLS fiber (in photo-electrons)"
        },
        {
            "variable": "clLength",
            "description": "cluster length (in cm)"
        },
        {
            "variable": "driftDist",
            "description": "drift distance (in cm)"
        },
        {
            "variable": "Erec",
            "description": "reconstructed energy of an event (in GeV)"
        },
        {
            "variable": "ErecErr",
            "description": "reconstructed energy error (in GeV)"
        },
        {
            "variable": "evID",
            "description": "event Id"
        },
        {
            "variable": "globPosX",
            "description": "X position of a vertex in the OPERA detector system of reference (in cm)"
        },
        {
            "variable": "globPosY",
            "description": "Y position of a vertex in the OPERA detector system of reference (in cm)"
        },
        {
            "variable": "globPosZ",
            "description": "Z position of a vertex in the OPERA detector system of reference (in cm)"
        },
        {
            "variable": "posX",
            "description": "For Electronic Detector events, X position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, X position of a track/vertex in the OPERA brick system of reference (in micrometers)."
        },
        {
            "variable": "posX1",
            "description": "X position of the beginning of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "posX2",
            "description": "X position of the end of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "posY",
            "description": "For Electronic Detector events, Y position of an RPC hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Y position of a track/vertex in the OPERA brick system of reference (in micrometers)."
        },
        {
            "variable": "posY1",
            "description": "Y position of the beginning of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "posY2",
            "description": "Y position of the end of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "posZ",
            "description": "For Electronic Detector events, Z position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Z position of a track/vertex in the OPERA brick system of reference (in micrometers)."
        },
        {
            "variable": "posZ1",
            "description": "Z position of the beginning of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "posZ2",
            "description": "Z position of the end of a line in the OPERA brick system of reference (in micrometers)"
        },
        {
            "variable": "slopeXZ",
            "description": "tangent of a track angle in XZ view"
        },
        {
            "variable": "slopeYZ",
            "description": "tangent of a track angle in YZ view"
        },
        {
            "variable": "timestamp",
            "description": "event time in milliseconds since 01/01/1970"
        },
        {
            "variable": "trType",
            "description": "type of a track: 12 - electron at the neutrino interaction vertex or e+/e- shower, initiated by the electron; 3 - e+/e- shower(s), initiated by gamma conversion"
        }
    ],
    "abstract": {
        "description": "The OPERA detector event is a muon neutrino interaction with the lead target where a muon was reconstructed in the final state. The event data from Electronic Detectors are available in the Drift Tube, RPC, and Target Tracker files. The event data from Emulsion Detectors are available in the Tracks and Vertex files. The EventInfo file presents general information about the event."
    },
    "license": {
        "attribution": "CC0"
    },
    "usage": {
        "description": "These OPERA event data files can be visualised using the online OPERA event display",
        "links": [
            {
                "url": "/visualise/events/opera/%(eventid)s",
                "description": "Visualise OPERA electron neutrino event %(eventid)s"
            }
        ]
    },
    "accelerator": "CERN-SPS",
    "experiment": "OPERA",
    "collections": [
       "OPERA-Detector-Events"
    ],
    "relations": [
        {
            "type": "isPartOf",
            "description": "This event is part of OPERA Electronic Detector electron neutrino dataset",
            "recid": "13155"
        },
        {
            "type": "isPartOf",
            "description": "This event is part of OPERA Emulsion Detector electron neutrino dataset",
            "recid": "13156"
        }
    ],
    "files": [
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file0name)s",
            "size": %(file0size)s,
            "checksum": "adler32:%(file0checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file1name)s",
            "size": %(file1size)s,
            "checksum": "adler32:%(file1checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file2name)s",
            "size": %(file2size)s,
            "checksum": "adler32:%(file2checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file3name)s",
            "size": %(file3size)s,
            "checksum": "adler32:%(file3checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file4name)s",
            "size": %(file4size)s,
            "checksum": "adler32:%(file4checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file5name)s",
            "size": %(file5size)s,
            "checksum": "adler32:%(file5checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file6name)s",
            "size": %(file6size)s,
            "checksum": "adler32:%(file6checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file7name)s",
            "size": %(file7size)s,
            "checksum": "adler32:%(file7checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file8name)s",
            "size": %(file8size)s,
            "checksum": "adler32:%(file8checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file9name)s",
            "size": %(file9size)s,
            "checksum": "adler32:%(file9checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file10name)s",
            "size": %(file10size)s,
            "checksum": "adler32:%(file10checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file11name)s",
            "size": %(file11size)s,
            "checksum": "adler32:%(file11checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file12name)s",
            "size": %(file12size)s,
            "checksum": "adler32:%(file12checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/electron-neutrinos/%(file13name)s",
            "size": %(file13size)s,
            "checksum": "adler32:%(file13checksum)s"
        }
    ]
}"""


def get_file_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    return hex(zlib.adler32(open(afile, 'rb').read(), 1) & 0xffffffff)[2:]

def clean_json_file(filename):
    """Clean JSON file.

    Cleans JSON file so as to fix indentation, order fields, and remove
    trailing whitespace.
    """
    with open(filename, 'r') as fdesc:
        records = json.loads(fdesc.read())

    new_content = json.dumps(records, indent=2, sort_keys=True,
                             ensure_ascii=False, separators=(',', ': '))

    with open(filename, 'w') as fdesc:
        fdesc.write(new_content + '\n')

ed_events = {}
for filename in os.listdir(EVENTDIR):
    if filename.endswith('.csv'):
        event = filename.split('_',1)[0]
        if event in ed_events:
            ed_events[event].append(filename)
        else:
            ed_events[event] = [filename]


fd = open('./outputs/opera-events.json', 'w')
fd.write('[\n')
recid = 13157
eventskeys = list(ed_events.keys())
eventskeys.sort()
for event in eventskeys[:-1]:
    ed_events[event].sort()
    fd.write(template % \
        {'recid': recid,
         'eventid': event,
         'nbfiles': len(ed_events[event]),
         'nbbytes': sum([os.path.getsize(os.path.join(EVENTDIR, f)) for f in ed_events[event]]),
         'filedir': EVENTDIR,
         'file0name': ed_events[event][0],
         'file0size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][0])),
         'file0checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][0])),
         'file1name': ed_events[event][1],
         'file1size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][1])),
         'file1checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][1])),
         'file2name': ed_events[event][2],
         'file2size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][2])),
         'file2checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][2])),
         'file3name': ed_events[event][3],
         'file3size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][3])),
         'file3checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][3])),
         'file4name': ed_events[event][4],
         'file4size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][4])),
         'file4checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][4])),
         'file5name': ed_events[event][5],
         'file5size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][5])),
         'file5checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][5])),
         'file6name': ed_events[event][6],
         'file6size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][6])),
         'file6checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][6])),
         'file7name': ed_events[event][7],
         'file7size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][7])),
         'file7checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][7])),
         'file8name': ed_events[event][8],
         'file8size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][8])),
         'file8checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][8])),
         'file9name': ed_events[event][9],
         'file9size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][9])),
         'file9checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][9])),
         'file10name': ed_events[event][10],
         'file10size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][10])),
         'file10checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][10])),
         'file11name': ed_events[event][11],
         'file11size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][11])),
         'file11checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][11])),
         'file12name': ed_events[event][12],
         'file12size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][12])),
         'file12checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][12])),
         'file13name': ed_events[event][13],
         'file13size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][13])),
         'file13checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][13])),})
    fd.write(',\n')
    recid += 1
for event in eventskeys[-1:]:
    ed_events[event].sort()
    fd.write(template % \
             {'recid': recid,
              'eventid': event,
              'nbfiles': len(ed_events[event]),
              'nbbytes': sum([os.path.getsize(os.path.join(EVENTDIR, f)) for f in ed_events[event]]),
              'filedir': EVENTDIR,
              'file0name': ed_events[event][0],
              'file0size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][0])),
              'file0checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][0])),
              'file1name': ed_events[event][1],
              'file1size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][1])),
              'file1checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][1])),
              'file2name': ed_events[event][2],
              'file2size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][2])),
              'file2checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][2])),
              'file3name': ed_events[event][3],
              'file3size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][3])),
              'file3checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][3])),
              'file4name': ed_events[event][4],
              'file4size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][4])),
              'file4checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][4])),
              'file5name': ed_events[event][5],
              'file5size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][5])),
              'file5checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][5])),
              'file6name': ed_events[event][6],
              'file6size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][6])),
              'file6checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][6])),
              'file7name': ed_events[event][7],
              'file7size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][7])),
              'file7checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][7])),
              'file8name': ed_events[event][8],
              'file8size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][8])),
              'file8checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][8])),
              'file9name': ed_events[event][9],
              'file9size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][9])),
              'file9checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][9])),
              'file10name': ed_events[event][10],
              'file10size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][10])),
              'file10checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][10])),
              'file11name': ed_events[event][11],
              'file11size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][11])),
              'file11checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][11])),
              'file12name': ed_events[event][12],
              'file12size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][12])),
              'file12checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][12])),
              'file13name': ed_events[event][13],
              'file13size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][13])),
              'file13checksum': get_file_checksum(os.path.join(EVENTDIR, ed_events[event][13])),})
    fd.write('\n')
    recid += 1
fd.write(']\n')
fd.close()

clean_json_file('./outputs/opera-events.json')
