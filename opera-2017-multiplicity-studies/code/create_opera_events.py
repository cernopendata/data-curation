#!/usr/bin/env python

import hashlib
import os

EVENTDIR = './inputs/events'

template = """\
{
    "recid": "%(recid)s",
    "doi": "%(doi)s",
    "collaboration": {
            "name": "OPERA collaboration",
            "recid": 452
    },
    "type": "Dataset",
    "subtype": "Primary Dataset",
    "title": "OPERA Detector Event %(eventid)s",
    "additional_title": "OPERA Detector Event %(eventid)s",
    "distribution": {
        "formats": [
            "csv"
        ],
        "number_events": "1",
        "number_files": "%(nbfiles)s",
        "size": "%(nbbytes)s"
    },
    "publisher": "CERN Open Data Portal",
    "date_published": "2017",
    "date_created": "2010-2012",
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
            "variable": "enHad",
            "description": "energy of a hadron jet (in GeV)"
        },
        {
            "variable": "enNeu",
            "description": "energy of a neutrino (in GeV)"
        },
        {
            "variable": "enVis",
            "description": "visible energy (in MeV)"
        },
        {
            "variable": "evID",
            "description": "event Id (11-digit number)"
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
            "variable": "mult",
            "description": "number of ECC tracks attached to the vertex"
        },
        {
            "variable": "muMom",
            "description": "momentum of a muon (in GeV/c)"
        },
        {
            "variable": "posX",
            "description": "For Electronic Detector events, X position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, X position of a track/vertex in the OPERA brick system of reference (in micrometers)."
        },
        {
            "variable": "posY",
            "description": "For Electronic Detector events, Y position of an RPC hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Y position of a track/vertex in the OPERA brick system of reference (in micrometers)."
        },
        {
            "variable": "posZ ",
            "description": "For Electronic Detector events, Z position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Z position of a track/vertex in the OPERA brick system of reference (in micrometers)."
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
            "description": "type of a track: 1 - muon; 2 - hadron; 3 - electron; 4 - black; 5 - back black; 6 - gray; 7 - back gray"
        }
    ],
    "abstract": "The OPERA detector event is a muon neutrino interaction with the lead target where a muon was reconstructed in the final state. The event data from Electronic Detectors are available in the Drift Tube, RPC, and Target Tracker files. The event data from Emulsion Detectors are available in the Tracks and Vertex files. The EventInfo file presents general information about the event.",
    "license": {
        "attribution": "CC0"
    },
    "usage": {
        "description": "These OPERA event data files can be visualised using the online OPERA event display",
        "links": [
            {
                "url": "http://opendata.cern.ch/visualise/events/OPERA/%(eventid)s",
                "description": "Visualise OPERA detector event %(eventid)s"
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
            "description": "This event is part of OPERA Electronic Detector dataset",
            "recid": "3900"
        },
        {
            "type": "isPartOf",
            "description": "This event is part of OPERA Emulsion Detector dataset",
            "recid": "3901"
        }
    ],
    "files": [
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file0name)s",
            "size": %(file0size)s,
            "checksum": "sha1:%(file0checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file1name)s",
            "size": %(file1size)s,
            "checksum": "sha1:%(file1checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file2name)s",
            "size": %(file2size)s,
            "checksum": "sha1:%(file2checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file3name)s",
            "size": %(file3size)s,
            "checksum": "sha1:%(file3checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file4name)s",
            "size": %(file4size)s,
            "checksum": "sha1:%(file4checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file5name)s",
            "size": %(file5size)s,
            "checksum": "sha1:%(file5checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file6name)s",
            "size": %(file6size)s,
            "checksum": "sha1:%(file6checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file7name)s",
            "size": %(file7size)s,
            "checksum": "sha1:%(file7checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file8name)s",
            "size": %(file8size)s,
            "checksum": "sha1:%(file8checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file9name)s",
            "size": %(file9size)s,
            "checksum": "sha1:%(file9checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file10name)s",
            "size": %(file10size)s,
            "checksum": "sha1:%(file10checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file11name)s",
            "size": %(file11size)s,
            "checksum": "sha1:%(file11checksum)s"
        },
        {
            "uri": "root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity/%(file12name)s",
            "size": %(file12size)s,
            "checksum": "sha1:%(file12checksum)s"
        }
    ]
}"""

dois = {}
recid = 4000
for line in open('./inputs/dois-opera-818.txt', 'r').readlines():
    dois[recid] = line.strip()
    recid += 1

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
recid = 4000
eventskeys = list(ed_events.keys())
eventskeys.sort()
for event in eventskeys[:-1]:
    ed_events[event].sort()
    fd.write(template % \
        {'recid': recid,
         'doi': dois[recid],
         'eventid': event,
         'nbfiles': len(ed_events[event]),
         'nbbytes': sum([os.path.getsize(os.path.join(EVENTDIR, f)) for f in ed_events[event]]),
         'filedir': EVENTDIR,
         'file0name': ed_events[event][0],
         'file0size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][0])),
         'file0checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][0]), 'rb').read()).hexdigest(),
         'file1name': ed_events[event][1],
         'file1size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][1])),
         'file1checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][1]), 'rb').read()).hexdigest(),
         'file2name': ed_events[event][2],
         'file2size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][2])),
         'file2checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][2]), 'rb').read()).hexdigest(),
         'file3name': ed_events[event][3],
         'file3size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][3])),
         'file3checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][3]), 'rb').read()).hexdigest(),
         'file4name': ed_events[event][4],
         'file4size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][4])),
         'file4checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][4]), 'rb').read()).hexdigest(),
         'file5name': ed_events[event][5],
         'file5size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][5])),
         'file5checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][5]), 'rb').read()).hexdigest(),
         'file6name': ed_events[event][6],
         'file6size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][6])),
         'file6checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][6]), 'rb').read()).hexdigest(),
         'file7name': ed_events[event][7],
         'file7size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][7])),
         'file7checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][7]), 'rb').read()).hexdigest(),
         'file8name': ed_events[event][8],
         'file8size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][8])),
         'file8checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][8]), 'rb').read()).hexdigest(),
         'file9name': ed_events[event][9],
         'file9size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][9])),
         'file9checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][9]), 'rb').read()).hexdigest(),
         'file10name': ed_events[event][10],
         'file10size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][10])),
         'file10checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][10]), 'rb').read()).hexdigest(),
         'file11name': ed_events[event][11],
         'file11size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][11])),
         'file11checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][11]), 'rb').read()).hexdigest(),
         'file12name': ed_events[event][12],
         'file12size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][12])),
         'file12checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][12]), 'rb').read()).hexdigest()})
    fd.write(',\n')
    recid += 1
for event in eventskeys[-1:]:
    ed_events[event].sort()
    fd.write(template % \
             {'recid': recid,
              'doi': dois[recid],
              'eventid': event,
              'nbfiles': len(ed_events[event]),
              'nbbytes': sum([os.path.getsize(os.path.join(EVENTDIR, f)) for f in ed_events[event]]),
              'filedir': EVENTDIR,
              'file0name': ed_events[event][0],
              'file0size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][0])),
              'file0checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][0]), 'rb').read()).hexdigest(),
              'file1name': ed_events[event][1],
              'file1size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][1])),
              'file1checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][1]), 'rb').read()).hexdigest(),
              'file2name': ed_events[event][2],
              'file2size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][2])),
              'file2checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][2]), 'rb').read()).hexdigest(),
              'file3name': ed_events[event][3],
              'file3size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][3])),
              'file3checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][3]), 'rb').read()).hexdigest(),
              'file4name': ed_events[event][4],
              'file4size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][4])),
              'file4checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][4]), 'rb').read()).hexdigest(),
              'file5name': ed_events[event][5],
              'file5size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][5])),
              'file5checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][5]), 'rb').read()).hexdigest(),
              'file6name': ed_events[event][6],
              'file6size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][6])),
              'file6checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][6]), 'rb').read()).hexdigest(),
              'file7name': ed_events[event][7],
              'file7size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][7])),
              'file7checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][7]), 'rb').read()).hexdigest(),
              'file8name': ed_events[event][8],
              'file8size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][8])),
              'file8checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][8]), 'rb').read()).hexdigest(),
              'file9name': ed_events[event][9],
              'file9size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][9])),
              'file9checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][9]), 'rb').read()).hexdigest(),
              'file10name': ed_events[event][10],
              'file10size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][10])),
              'file10checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][10]), 'rb').read()).hexdigest(),
              'file11name': ed_events[event][11],
              'file11size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][11])),
              'file11checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][11]), 'rb').read()).hexdigest(),
              'file12name': ed_events[event][12],
              'file12size': os.path.getsize(os.path.join(EVENTDIR, ed_events[event][12])),
              'file12checksum': hashlib.sha1(open(os.path.join(EVENTDIR, ed_events[event][12]), 'rb').read()).hexdigest()})
    fd.write('\n')
    recid += 1
fd.write(']\n')
fd.close()
