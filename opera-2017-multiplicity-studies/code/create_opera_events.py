#!/usr/bin/env python

import os

FILEDIR = '/tmp/opendata.cern.ch-fft-file-cache'

template = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="024" ind1="7" ind2=" ">
      <subfield code="a">%(doi)s</subfield>
      <subfield code="2">DOI</subfield>
    </datafield>
    <datafield tag="110" ind1=" " ind2=" ">
      <subfield code="a">OPERA collaboration</subfield>
      <subfield code="w">452</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
      <subfield code="a">OPERA Detector Event %(eventid)s</subfield>
    </datafield>
    <datafield tag="246" ind1=" " ind2=" ">
      <subfield code="a">OPERA Detector Event %(eventid)s</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="a">Dataset</subfield>
      <subfield code="e">1</subfield>
      <subfield code="t">events</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="f">%(nbfiles)s</subfield>
      <subfield code="t">files</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="b">%(nbbytes)s</subfield>
      <subfield code="t">bytes in total</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
      <subfield code="b">CERN Open Data Portal</subfield>
      <subfield code="c">2017</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
      <subfield code="c">2010-2012</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">amplL</subfield>
      <subfield code="g">PMT amplitude measured from the "left" side of a scintillator strip (in photo-electrons)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">amplR</subfield>
      <subfield code="g">PMT amplitude measured from the "right" side of a scintillator strip (in photo-electrons)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">amplRec</subfield>
      <subfield code="g">PMT amplitude reconstructed from the "left" and "right" side amplitudes of a scintillator strip taking into account light attenuation in a WLS fiber (in photo-electrons)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">clLength</subfield>
      <subfield code="g">cluster length (in cm)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">driftDist</subfield>
      <subfield code="g">drift distance (in cm)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">enHad</subfield>
      <subfield code="g">energy of a hadron jet (in GeV)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">enNeu</subfield>
      <subfield code="g">energy of a neutrino (in GeV)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">enVis</subfield>
      <subfield code="g">visible energy (in MeV)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">evID</subfield>
      <subfield code="g">event Id (11-digit number)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">globPosX</subfield>
      <subfield code="g">X position of a vertex in the OPERA detector system of reference (in cm)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">globPosY</subfield>
      <subfield code="g">Y position of a vertex in the OPERA detector system of reference (in cm)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">globPosZ</subfield>
      <subfield code="g">Z position of a vertex in the OPERA detector system of reference (in cm)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">mult</subfield>
      <subfield code="g">number of ECC tracks attached to the vertex</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">muMom</subfield>
      <subfield code="g">momentum of a muon (in GeV/c)</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">posX</subfield>
      <subfield code="g">For Electronic Detector events, X position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, X position of a track/vertex in the OPERA brick system of reference (in micrometers).</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">posY</subfield>
      <subfield code="g">For Electronic Detector events, Y position of an RPC hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Y position of a track/vertex in the OPERA brick system of reference (in micrometers).</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">posZ </subfield>
      <subfield code="g">For Electronic Detector events, Z position of a drift tube, RPC, Target Tracker hit in the OPERA detector system of reference (in cm). For Emulsion Detector events, Z position of a track/vertex in the OPERA brick system of reference (in micrometers).</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">slopeXZ</subfield>
      <subfield code="g">tangent of a track angle in XZ view</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">slopeYZ</subfield>
      <subfield code="g">tangent of a track angle in YZ view</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">timestamp</subfield>
      <subfield code="g">event time in milliseconds since 01/01/1970</subfield>
    </datafield>
    <datafield tag="505" ind1=" " ind2=" ">
      <subfield code="t">trType</subfield>
      <subfield code="g">type of a track: 1 - muon; 2 - hadron; 3 - electron; 4 - black; 5 - back black; 6 - gray; 7 - back gray</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
      <subfield code="a">The OPERA detector event is a muon neutrino interaction with the lead target where a muon was reconstructed in the final state. The event data from Electronic Detectors are available in the Drift Tube, RPC, and Target Tracker files. The event data from Emulsion Detectors are available in the Tracks and Vertex files. The EventInfo file presents general information about the event.</subfield>
    </datafield>
    <datafield tag="540" ind1=" " ind2=" ">
      <subfield code="a">CC0</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
      <subfield code="a">These OPERA event data files can be visualised using the online OPERA event display</subfield>
      <subfield code="u">http://opendata.cern.ch/visualise/events/OPERA/%(eventid)s</subfield>
      <subfield code="y">Visualise OPERA detector event %(eventid)s</subfield>b
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
      <subfield code="a">CERN-SPS</subfield>
      <subfield code="e">OPERA</subfield>
    </datafield>
   <datafield tag="786" ind1=" " ind2=" ">
      <subfield code="a">This event is part of OPERA Electronic Detector dataset</subfield>
      <subfield code="w">3900</subfield>
    </datafield>
   <datafield tag="786" ind1=" " ind2=" ">
      <subfield code="a">This event is part of OPERA Emulsion Detector dataset</subfield>
      <subfield code="w">3901</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="a">OPERA-Detector-Events</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="b">Education</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ecc-datasets/%(filename0a)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ecc-datasets/%(filename0b)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename1)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename2)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename3)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename4)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename5)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename6)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename7)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename8)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename9)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename10)s</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(filedir)s/opera-ed-datasets/%(filename11)s</subfield>
    </datafield>
  </record>
"""

dois = {}
recid = 4000
for line in open('./inputs/dois-opera-818.txt', 'r').readlines():
    dois[recid] = line.strip()
    recid += 1

ed_events = {}
for filename in os.listdir(FILEDIR + os.sep + 'opera-ed-datasets'):
    if filename.endswith('.csv'):
        event = filename.split('_',1)[0]
        if event in ed_events:
            ed_events[event].append(filename)
        else:
            ed_events[event] = [filename]

ecc_events = {}
for filename in os.listdir(FILEDIR + os.sep + 'opera-ecc-datasets'):
    if filename.endswith('.csv'):
        event = filename.split('_',1)[0]
        if event in ecc_events:
            ecc_events[event].append(filename)
        else:
            ecc_events[event] = [filename]

fd = open('./outputs/opera-events.xml', 'w')
fd.write('<collection>\n')
recid = 4000
eventskeys = list(ed_events.keys())
eventskeys.sort()
for event in eventskeys:
    ed_events[event].sort()
    ecc_events[event].sort()
    fd.write(template % {'recid': recid,
                         'doi': dois[recid],
                         'eventid': event,
                         'nbfiles': len(ed_events[event] + ecc_events[event]),
                         'nbbytes': sum([os.path.getsize(os.path.join(FILEDIR, 'opera-ed-datasets', f)) for f in ed_events[event]] +
                                        [os.path.getsize(os.path.join(FILEDIR, 'opera-ecc-datasets', f)) for f in ecc_events[event]]),
                         'filedir': FILEDIR,
                         'filename0a' : ecc_events[event][0],
                         'filename0b' : ecc_events[event][1],
                         'filename1' : ed_events[event][0],
                         'filename2' : ed_events[event][1],
                         'filename3' : ed_events[event][2],
                         'filename4' : ed_events[event][3],
                         'filename5' : ed_events[event][4],
                         'filename6' : ed_events[event][5],
                         'filename7' : ed_events[event][6],
                         'filename8' : ed_events[event][7],
                         'filename9' : ed_events[event][8],
                         'filename10' : ed_events[event][9],
                         'filename11' : ed_events[event][10]})
    recid += 1
fd.write('</collection>\n')
fd.close()
