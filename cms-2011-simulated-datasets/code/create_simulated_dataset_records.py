#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS Simulated Dataset records.
"""

import glob
import json
import re
import subprocess
import sys

from create_das_json_store import get_das_json, get_from_deep_json
from create_config_download_script import get_input_dataset

LINK_INFO = {}
exec(open('./outputs/config_files_link_info.py', 'r').read())

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="024" ind1="7" ind2=" ">
        <subfield code="2">DOI</subfield>
        <subfield code="a">%(doi)s</subfield>
    </datafield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="a">CMS collaboration</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">%(title)s</subfield>
    </datafield>
    <datafield tag="246" ind1=" " ind2=" ">
        <subfield code="a">%(title_heading)s</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="a">Dataset</subfield>
        <subfield code="e">%(nb_events)s</subfield>
        <subfield code="t">events</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="f">%(nb_files)s</subfield>
        <subfield code="t">files</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="b">%(nb_bytes)s</subfield>
        <subfield code="t">bytes in total</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="b">CERN Open Data Portal</subfield>
        <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
        <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
        <subfield code="a"><![CDATA[
          <p>%(title_heading)s</p>
          <p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>]]>
        </subfield>
    </datafield>
    <datafield tag="538" ind1=" " ind2=" ">
        <subfield code="a">Recommended release for analysis: CMSSW_5_3_32</subfield>
        <subfield code="b">Global tag: %(global_tag)s</subfield>
    </datafield>
    <datafield tag="540" ind1=" " ind2=" ">
        <subfield code="a">CC0</subfield>
    </datafield>
    <datafield tag="556" ind1=" " ind2=" ">
        <subfield code="a">These simulated datasets correspond to the collision data collected by the CMS experiment in 2011.</subfield>
    </datafield>
    <datafield tag="567" ind1=" " ind2=" ">
        <subfield code="a">%(generator_parameters)s</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
        <subfield code="a">You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in</subfield>
        <subfield code="u">http://opendata.cern.ch/VM/CMS#2011</subfield>
        <subfield code="y">How to install the CMS Virtual Machine</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
        <subfield code="u">http://opendata.cern.ch/getting-started/CMS#2011</subfield>
        <subfield code="y">Getting started with CMS open data</subfield>
    </datafield>
    <datafield tag="583" ind1=" " ind2=" ">
        <subfield code="a">The generation and simulation of simulated Monte Carlo data has been validated through general CMS validation procedures.</subfield>
    </datafield>
    <datafield tag="593" ind1=" " ind2=" ">
        <subfield code="a">Generators: %(generators)s</subfield>
        <subfield code="b">Global tag: %(global_tag)s</subfield>
    </datafield>
    <datafield tag="655" ind1=" " ind2="7">
        <subfield code="a">%(category)s</subfield>
        <subfield code="9">CMS Collaboration</subfield>
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
        <subfield code="a">CERN-LHC</subfield>
        <subfield code="e">CMS</subfield>
    </datafield>
    <datafield tag="770" ind1=" " ind2=" ">
        <subfield code="a">/MinBias_TuneZ2_7TeV-pythia6/Summer11Leg-START53_LV4-v1/GEN-SIM</subfield>
        <subfield code="w">3600</subfield>
    </datafield>
    <datafield tag="772" ind1=" " ind2=" ">
        <subfield code="a">%(raw)s</subfield>
    </datafield>
%(8567s)s
    <datafield tag="942" ind1=" " ind2=" ">
        <subfield code="e">7TeV</subfield>
    </datafield>
    <datafield tag="964" ind1=" " ind2="0">
        <subfield code="c">Run2011A</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="a">CMS-Simulated-Datasets</subfield>
    </datafield>
%(FFTs)s
  </record>"""

TEMPLATE_FFT = """\
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-eos-file-indexes/%(filename)s</subfield>
      <subfield code="z">%(dataset)s dataset file index (%(nb_dataset)s of %(nb_total)s) for access to data via CMS virtual machine</subfield>
    </datafield>
"""

def create_8567s(dataset):
    out = ''
    junk, dataset_prefix, dataset_middle, dataset_suffix = dataset.split('/')
    dataset_version = dataset_middle[dataset_middle.index('PU_S13'):]
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*_%s_*xml' % (dataset_prefix, dataset_version))
    filenames.sort()
    for filename in filenames:
        out += open(filename, 'r').read()
        out = out.rstrip()
    return out


def create_FFTs(dataset):
    out = ''
    junk, dataset_prefix, dataset_middle, dataset_suffix = dataset.split('/')
    dataset_version = dataset_middle[dataset_middle.index('PU_S13'):]
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*_%s_*txt' % (dataset_prefix, dataset_version))
    filenames.sort()
    nb_total = len(filenames)
    for nb_dataset, filename in enumerate(filenames):
        out += TEMPLATE_FFT % {
            'dataset': dataset,
            'filename': filename.replace('./inputs/eos-file-indexes/', ''),
            'nb_dataset': str(nb_dataset + 1),
            'nb_total': str(nb_total)
        }
    return out.rstrip()


def get_version(dataset):
    if dataset in ['ForwardTriggers',]:
        return '2'
    else:
        return '1'


def get_nb_files(dataset):
    out = 0
    filenames = glob.glob('*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += 1
    return out


def get_nb_bytes(dataset):
    out = 0
    filenames = glob.glob('*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += int(match.groups()[0])
    return out


def get_doi(recid):
    dois = {
        1300: '10.7483/OPENDATA.CMS.VPJH.JZHB',
        1301: '10.7483/OPENDATA.CMS.V6AN.FXJJ',
        1302: '10.7483/OPENDATA.CMS.GA4B.CKA7',
        1303: '10.7483/OPENDATA.CMS.9MHK.R9U4',
        1304: '10.7483/OPENDATA.CMS.D72N.TR5C',
        1305: '10.7483/OPENDATA.CMS.5YJP.R4GT',
        1306: '10.7483/OPENDATA.CMS.FMNR.TQP3',
        1307: '10.7483/OPENDATA.CMS.ZPH2.MXP5',
        1308: '10.7483/OPENDATA.CMS.HJYH.UMWG',
        1309: '10.7483/OPENDATA.CMS.MQ7E.J9NE',
        1310: '10.7483/OPENDATA.CMS.KUMT.WEYE',
        1311: '10.7483/OPENDATA.CMS.UB82.2FZU',
        1312: '10.7483/OPENDATA.CMS.M5CN.BTGB',
        1313: '10.7483/OPENDATA.CMS.2JTU.TNBJ',
        1314: '10.7483/OPENDATA.CMS.EPE5.ZUXC',
        1315: '10.7483/OPENDATA.CMS.9RHV.X49V',
        1316: '10.7483/OPENDATA.CMS.HKCE.U6EM',
        1317: '10.7483/OPENDATA.CMS.FCES.39BQ',
        1318: '10.7483/OPENDATA.CMS.QKZU.PZQ6',
        1319: '10.7483/OPENDATA.CMS.4W5F.MMUP',
        1320: '10.7483/OPENDATA.CMS.JG6J.FHZY',
        1321: '10.7483/OPENDATA.CMS.UYU2.WCAG',
        1322: '10.7483/OPENDATA.CMS.5KC9.YA5J',
        1323: '10.7483/OPENDATA.CMS.PK4V.5EUK',
        1324: '10.7483/OPENDATA.CMS.D3JK.78CF',
        1325: '10.7483/OPENDATA.CMS.BY94.Z63F',
        1326: '10.7483/OPENDATA.CMS.CK2Q.STKY',
        1327: '10.7483/OPENDATA.CMS.CNRK.R8J7',
        1328: '10.7483/OPENDATA.CMS.RRK8.3ZSV',
        1329: '10.7483/OPENDATA.CMS.BGSX.JJTM',
        1330: '10.7483/OPENDATA.CMS.CR5X.YVQN',
        1331: '10.7483/OPENDATA.CMS.FZAJ.JFW7',
        1332: '10.7483/OPENDATA.CMS.U683.H59F',
        1333: '10.7483/OPENDATA.CMS.TJV5.RZM3',
        1334: '10.7483/OPENDATA.CMS.6QJD.ZDHJ',
        1335: '10.7483/OPENDATA.CMS.JRWG.74V6',
        1336: '10.7483/OPENDATA.CMS.446C.HV8G',
        1337: '10.7483/OPENDATA.CMS.NVP4.XMYR',
        1338: '10.7483/OPENDATA.CMS.P4HX.J233',
        1339: '10.7483/OPENDATA.CMS.X5EZ.K2ZR',
        1340: '10.7483/OPENDATA.CMS.2QR5.9P6G',
        1341: '10.7483/OPENDATA.CMS.KH7Q.Q67U',
        1342: '10.7483/OPENDATA.CMS.96U2.3YAH',
        1343: '10.7483/OPENDATA.CMS.57TZ.6Z9Q',
        1344: '10.7483/OPENDATA.CMS.AGBK.K9CX',
        1345: '10.7483/OPENDATA.CMS.AYFR.VX72',
        1346: '10.7483/OPENDATA.CMS.AGGR.9TEK',
        1347: '10.7483/OPENDATA.CMS.DNZB.34U3',
        1348: '10.7483/OPENDATA.CMS.QJND.HA88',
        1349: '10.7483/OPENDATA.CMS.34MQ.7N72',
        1350: '10.7483/OPENDATA.CMS.3R3P.5JYR',
        1351: '10.7483/OPENDATA.CMS.D2RV.NB9M',
        1352: '10.7483/OPENDATA.CMS.NKM7.VS8G',
        1353: '10.7483/OPENDATA.CMS.2X8H.237F',
        1354: '10.7483/OPENDATA.CMS.PTR7.4RER',
        1355: '10.7483/OPENDATA.CMS.BN7K.8N4A',
        1356: '10.7483/OPENDATA.CMS.WEE7.MUNW',
        1357: '10.7483/OPENDATA.CMS.TZH7.EFE7',
        1358: '10.7483/OPENDATA.CMS.MXSE.G54G',
        1359: '10.7483/OPENDATA.CMS.8E2V.PX7B',
        1360: '10.7483/OPENDATA.CMS.CSJG.AWBA',
        1361: '10.7483/OPENDATA.CMS.7BD2.8XD2',
        1362: '10.7483/OPENDATA.CMS.448D.ZHNC',
        1363: '10.7483/OPENDATA.CMS.466D.T3D9',
        1364: '10.7483/OPENDATA.CMS.RC9V.B5KX',
        1365: '10.7483/OPENDATA.CMS.5NPW.3HWE',
        1366: '10.7483/OPENDATA.CMS.RSKY.VC8C',
        1367: '10.7483/OPENDATA.CMS.P9Z6.X85N',
        1368: '10.7483/OPENDATA.CMS.2K8R.VJJH',
        1369: '10.7483/OPENDATA.CMS.WKRR.DCJP',
        1370: '10.7483/OPENDATA.CMS.CX2X.J3KW',
        1371: '10.7483/OPENDATA.CMS.R5SH.7ZY2',
        1372: '10.7483/OPENDATA.CMS.K64Z.CP2F',
        1373: '10.7483/OPENDATA.CMS.EMGG.EKKB',
        1374: '10.7483/OPENDATA.CMS.HC3V.2QBD',
        1375: '10.7483/OPENDATA.CMS.P6U8.T9N8',
        1376: '10.7483/OPENDATA.CMS.JPW9.E5HW',
        1377: '10.7483/OPENDATA.CMS.6UGA.H7QV',
        1378: '10.7483/OPENDATA.CMS.BYY5.YKS5',
        1379: '10.7483/OPENDATA.CMS.GHZE.S4M3',
        1380: '10.7483/OPENDATA.CMS.VP6H.AWDC',
        1381: '10.7483/OPENDATA.CMS.AZW4.R2GG',
        1382: '10.7483/OPENDATA.CMS.7G2E.4PGB',
        1383: '10.7483/OPENDATA.CMS.ZCNM.27A3',
        1384: '10.7483/OPENDATA.CMS.WK2P.WZSF',
        1385: '10.7483/OPENDATA.CMS.25XG.XPSU',
        1386: '10.7483/OPENDATA.CMS.E8VC.3JS5',
        1387: '10.7483/OPENDATA.CMS.DV6X.5SGW',
        1388: '10.7483/OPENDATA.CMS.2JK2.HTVJ',
        1389: '10.7483/OPENDATA.CMS.U6JT.SMMC',
        1390: '10.7483/OPENDATA.CMS.4G5S.44WQ',
        1391: '10.7483/OPENDATA.CMS.D5KD.U5MR',
        1392: '10.7483/OPENDATA.CMS.UUG7.4NHT',
        1393: '10.7483/OPENDATA.CMS.T8RZ.D52D',
        1394: '10.7483/OPENDATA.CMS.4475.SSXE',
        1395: '10.7483/OPENDATA.CMS.TXT4.4RRP',
        1396: '10.7483/OPENDATA.CMS.PKN9.A4F4',
        1397: '10.7483/OPENDATA.CMS.WJ99.85PE',
        1398: '10.7483/OPENDATA.CMS.5E6B.Q3MJ',
        1399: '10.7483/OPENDATA.CMS.AGZZ.26HG',
        1400: '10.7483/OPENDATA.CMS.DWBP.WWWZ',
        1401: '10.7483/OPENDATA.CMS.44RZ.E298',
        1402: '10.7483/OPENDATA.CMS.MFHX.N8UZ',
        1403: '10.7483/OPENDATA.CMS.JG5S.UCWE',
        1404: '10.7483/OPENDATA.CMS.AD9J.A8ZY',
        1405: '10.7483/OPENDATA.CMS.6PZJ.YEYN',
        1406: '10.7483/OPENDATA.CMS.K8YT.RH62',
        1407: '10.7483/OPENDATA.CMS.UA4D.XGRQ',
        1408: '10.7483/OPENDATA.CMS.9WT8.WCNQ',
        1409: '10.7483/OPENDATA.CMS.YPVY.T53Z',
        1410: '10.7483/OPENDATA.CMS.JV8S.DCSK',
        1411: '10.7483/OPENDATA.CMS.566N.P583',
        1412: '10.7483/OPENDATA.CMS.E85J.TK3G',
        1413: '10.7483/OPENDATA.CMS.S45A.U3CR',
        1414: '10.7483/OPENDATA.CMS.3T6G.QCWD',
        1415: '10.7483/OPENDATA.CMS.GFC7.JB6P',
        1416: '10.7483/OPENDATA.CMS.YGNF.8NP7',
        1417: '10.7483/OPENDATA.CMS.GU9E.KN89',
        1418: '10.7483/OPENDATA.CMS.WCT5.U54E',
        1419: '10.7483/OPENDATA.CMS.6M5H.WRYA',
        1420: '10.7483/OPENDATA.CMS.JV26.YXEA',
        1421: '10.7483/OPENDATA.CMS.C4W8.ENKU',
        1422: '10.7483/OPENDATA.CMS.X8CT.GS2X',
        1423: '10.7483/OPENDATA.CMS.P54T.CSJS',
        1424: '10.7483/OPENDATA.CMS.YSTQ.AYGQ',
        1425: '10.7483/OPENDATA.CMS.SKKX.D34G',
        1426: '10.7483/OPENDATA.CMS.S7NK.ZK8U',
        1427: '10.7483/OPENDATA.CMS.H437.HAQB',
        1428: '10.7483/OPENDATA.CMS.ZASR.7BEP',
        1429: '10.7483/OPENDATA.CMS.CFVD.W4HF',
        1430: '10.7483/OPENDATA.CMS.EZJS.9PZA',
        1431: '10.7483/OPENDATA.CMS.EPUN.P56F',
        1432: '10.7483/OPENDATA.CMS.PJSX.D6DN',
        1433: '10.7483/OPENDATA.CMS.V3VD.KPV5',
        1434: '10.7483/OPENDATA.CMS.UMWW.RPZN',
        1435: '10.7483/OPENDATA.CMS.AUT8.MD6N',
        1436: '10.7483/OPENDATA.CMS.K2MK.P4GY',
        1437: '10.7483/OPENDATA.CMS.5VHJ.9NM3',
        1438: '10.7483/OPENDATA.CMS.9RXN.W3PT',
        1439: '10.7483/OPENDATA.CMS.2ZMR.GBW5',
        1440: '10.7483/OPENDATA.CMS.EEY2.9Y2U',
        1441: '10.7483/OPENDATA.CMS.MPUZ.TBZK',
        1442: '10.7483/OPENDATA.CMS.GWRW.TZ86',
        1443: '10.7483/OPENDATA.CMS.G4SB.Y2BX',
        1444: '10.7483/OPENDATA.CMS.8XNT.2XRX',
        1445: '10.7483/OPENDATA.CMS.DRDE.DFZA',
        1446: '10.7483/OPENDATA.CMS.C8MG.CVMR',
        1447: '10.7483/OPENDATA.CMS.GQG8.72PH',
        1448: '10.7483/OPENDATA.CMS.C2EZ.E8TN',
        1449: '10.7483/OPENDATA.CMS.MDXY.CUAJ',
        1450: '10.7483/OPENDATA.CMS.DXGT.MJGD',
        1451: '10.7483/OPENDATA.CMS.4QNQ.86MW',
        1452: '10.7483/OPENDATA.CMS.9WHE.UE26',
        1453: '10.7483/OPENDATA.CMS.8QK3.83V9',
        1454: '10.7483/OPENDATA.CMS.DENC.DHVT',
        1455: '10.7483/OPENDATA.CMS.J48K.6VMY',
        1456: '10.7483/OPENDATA.CMS.UNTH.MX69',
        1457: '10.7483/OPENDATA.CMS.FX3M.49C6',
        1458: '10.7483/OPENDATA.CMS.3W3N.DX7X',
        1459: '10.7483/OPENDATA.CMS.QZ66.35WA',
        1460: '10.7483/OPENDATA.CMS.KPWJ.6M93',
        1461: '10.7483/OPENDATA.CMS.VYCM.5UT6',
        1462: '10.7483/OPENDATA.CMS.H375.RGYJ',
        1463: '10.7483/OPENDATA.CMS.YY2Y.EQ9E',
        1464: '10.7483/OPENDATA.CMS.K9ED.PD36',
        1465: '10.7483/OPENDATA.CMS.A8UU.6R88',
        1466: '10.7483/OPENDATA.CMS.EFVZ.663S',
        1467: '10.7483/OPENDATA.CMS.7WRD.KQUR',
        1468: '10.7483/OPENDATA.CMS.JEZ4.4ZZS',
        1469: '10.7483/OPENDATA.CMS.X3XQ.USQR',
        1470: '10.7483/OPENDATA.CMS.PE7B.23XG',
        1471: '10.7483/OPENDATA.CMS.CZPT.843Y',
        1472: '10.7483/OPENDATA.CMS.T4MG.3GJC',
        1473: '10.7483/OPENDATA.CMS.WZ2J.Y5B2',
        1474: '10.7483/OPENDATA.CMS.4NZC.69BR',
        1475: '10.7483/OPENDATA.CMS.WZJR.DEYH',
        1476: '10.7483/OPENDATA.CMS.TPNT.6PYK',
        1477: '10.7483/OPENDATA.CMS.K8X4.NNGC',
        1478: '10.7483/OPENDATA.CMS.DMQP.VWE9',
        1479: '10.7483/OPENDATA.CMS.274Q.PNTF',
        1480: '10.7483/OPENDATA.CMS.AD5H.5SVP',
        1481: '10.7483/OPENDATA.CMS.YGD3.HSPT',
        1482: '10.7483/OPENDATA.CMS.Q4M9.UVJN',
        1483: '10.7483/OPENDATA.CMS.Z6PA.3Z5K',
        1484: '10.7483/OPENDATA.CMS.FB4K.G8ZF',
        1485: '10.7483/OPENDATA.CMS.YQNF.2PTX',
        1486: '10.7483/OPENDATA.CMS.ZYMN.WQRP',
        1487: '10.7483/OPENDATA.CMS.SZWT.H9MC',
        1488: '10.7483/OPENDATA.CMS.6K25.N4HP',
        1489: '10.7483/OPENDATA.CMS.FVJE.FT4R',
        1490: '10.7483/OPENDATA.CMS.MQBV.53VN',
        1491: '10.7483/OPENDATA.CMS.BKTE.D4WG',
        1492: '10.7483/OPENDATA.CMS.SGVW.KQY2',
        1493: '10.7483/OPENDATA.CMS.ZVP5.ZHCN',
        1494: '10.7483/OPENDATA.CMS.7M6H.92RR',
        1495: '10.7483/OPENDATA.CMS.4XCW.MVRR',
        1496: '10.7483/OPENDATA.CMS.ANHK.PC9F',
        1497: '10.7483/OPENDATA.CMS.F9K9.3JFC',
        1498: '10.7483/OPENDATA.CMS.UMPG.E6HN',
        1499: '10.7483/OPENDATA.CMS.6TNM.5YPM',
        1500: '10.7483/OPENDATA.CMS.P4E7.SYG5',
        1501: '10.7483/OPENDATA.CMS.45EN.Z925',
        1502: '10.7483/OPENDATA.CMS.WSBR.SUNJ',
        1503: '10.7483/OPENDATA.CMS.VGWV.J3UC',
        1504: '10.7483/OPENDATA.CMS.7K7C.UMET',
        1505: '10.7483/OPENDATA.CMS.YYEE.6MPY',
        1506: '10.7483/OPENDATA.CMS.DBZT.4AZ6',
        1507: '10.7483/OPENDATA.CMS.K9EW.KRDS',
        1508: '10.7483/OPENDATA.CMS.JE22.RQ5J',
        1509: '10.7483/OPENDATA.CMS.496E.7BVA',
        1510: '10.7483/OPENDATA.CMS.VAHX.5WHS',
        1511: '10.7483/OPENDATA.CMS.GFKH.PH6Y',
        1512: '10.7483/OPENDATA.CMS.SZKA.ERNS',
        1513: '10.7483/OPENDATA.CMS.FR3C.3BZX',
        1514: '10.7483/OPENDATA.CMS.TPBS.77DC',
        1515: '10.7483/OPENDATA.CMS.FX8Y.YFTT',
        1516: '10.7483/OPENDATA.CMS.S4FG.DM8Y',
        1517: '10.7483/OPENDATA.CMS.K59T.T7V3',
        1518: '10.7483/OPENDATA.CMS.5UTX.X5U7',
        1519: '10.7483/OPENDATA.CMS.WY8C.B9A5',
        1520: '10.7483/OPENDATA.CMS.QV9U.GCS7',
        1521: '10.7483/OPENDATA.CMS.KW3V.6B3S',
        1522: '10.7483/OPENDATA.CMS.M8Y3.EHUC',
        1523: '10.7483/OPENDATA.CMS.YD32.QVWD',
        1524: '10.7483/OPENDATA.CMS.54YJ.6M72',
        1525: '10.7483/OPENDATA.CMS.55JN.R5JH',
        1526: '10.7483/OPENDATA.CMS.WJSD.P4ET',
        1527: '10.7483/OPENDATA.CMS.KS7P.TDC7',
        1528: '10.7483/OPENDATA.CMS.TUTH.HDWQ',
        1529: '10.7483/OPENDATA.CMS.E5PB.5JXM',
        1530: '10.7483/OPENDATA.CMS.PRK8.9HPT',
        1531: '10.7483/OPENDATA.CMS.2GVF.QYV5',
        1532: '10.7483/OPENDATA.CMS.C6C3.WVKB',
        1533: '10.7483/OPENDATA.CMS.WA6F.6PP7',
        1534: '10.7483/OPENDATA.CMS.5RG6.NNDK',
        1535: '10.7483/OPENDATA.CMS.NGMR.3734',
        1536: '10.7483/OPENDATA.CMS.9WR5.454D',
        1537: '10.7483/OPENDATA.CMS.P6B9.Z7SK',
        1538: '10.7483/OPENDATA.CMS.U3DR.GNRZ',
        1539: '10.7483/OPENDATA.CMS.Q3BX.69VQ',
        1540: '10.7483/OPENDATA.CMS.FSMU.EQHG',
        1541: '10.7483/OPENDATA.CMS.2KY2.4T48',
        1542: '10.7483/OPENDATA.CMS.SRSZ.C6XC',
        1543: '10.7483/OPENDATA.CMS.X7DE.P5GJ',
        1544: '10.7483/OPENDATA.CMS.ZBGF.H543',
        1545: '10.7483/OPENDATA.CMS.6CWA.JUW2',
        1546: '10.7483/OPENDATA.CMS.VTKQ.J8B7',
        1547: '10.7483/OPENDATA.CMS.2Z2V.EF7N',
        1548: '10.7483/OPENDATA.CMS.QH9R.SCTN',
        1549: '10.7483/OPENDATA.CMS.CARQ.ZYN6',
        1550: '10.7483/OPENDATA.CMS.8KEK.TM28',
        1551: '10.7483/OPENDATA.CMS.RYHH.BH37',
        1552: '10.7483/OPENDATA.CMS.X9KD.4XT7',
        1553: '10.7483/OPENDATA.CMS.BKTD.SGJX',
        1554: '10.7483/OPENDATA.CMS.V53F.8KR4',
        1555: '10.7483/OPENDATA.CMS.84VC.RU8W',
        1556: '10.7483/OPENDATA.CMS.972P.PY4C',
        1557: '10.7483/OPENDATA.CMS.3FQQ.KTS6',
        1558: '10.7483/OPENDATA.CMS.EJT7.KSAY',
        1559: '10.7483/OPENDATA.CMS.BUG8.SW65',
        1560: '10.7483/OPENDATA.CMS.S3D5.KF2C',
        1561: '10.7483/OPENDATA.CMS.SMGE.ACWS',
        1562: '10.7483/OPENDATA.CMS.PUTE.7H2H',
        1563: '10.7483/OPENDATA.CMS.N3RG.2JM7',
        1564: '10.7483/OPENDATA.CMS.AHB7.MRSZ',
        1565: '10.7483/OPENDATA.CMS.BW53.8D8E',
        1566: '10.7483/OPENDATA.CMS.S3MW.PQD7',
        1567: '10.7483/OPENDATA.CMS.AS5B.AHYT',
        1568: '10.7483/OPENDATA.CMS.ZBRH.87CA',
        1569: '10.7483/OPENDATA.CMS.AN8T.8KD6',
        1570: '10.7483/OPENDATA.CMS.GRVM.SMAJ',
        1571: '10.7483/OPENDATA.CMS.8SWS.TSW9',
        1572: '10.7483/OPENDATA.CMS.EWAE.G37G',
        1573: '10.7483/OPENDATA.CMS.EG44.NUAB',
        1574: '10.7483/OPENDATA.CMS.N4ZH.FZ6H',
        1575: '10.7483/OPENDATA.CMS.JC4Y.UX8Z',
        1576: '10.7483/OPENDATA.CMS.XVMZ.QX3Q',
        1577: '10.7483/OPENDATA.CMS.PTRW.XFGC',
        1578: '10.7483/OPENDATA.CMS.4CTX.T6S6',
        1579: '10.7483/OPENDATA.CMS.K9BP.QJ7P',
        1580: '10.7483/OPENDATA.CMS.E7AD.YR82',
        1581: '10.7483/OPENDATA.CMS.EU6J.F4P7',
        1582: '10.7483/OPENDATA.CMS.AMM3.D89B',
        1583: '10.7483/OPENDATA.CMS.4PMB.42GH',
        1584: '10.7483/OPENDATA.CMS.XVN9.JU8Y',
        1585: '10.7483/OPENDATA.CMS.GF4R.PRT2',
        1586: '10.7483/OPENDATA.CMS.Q8CE.3CJQ',
        1587: '10.7483/OPENDATA.CMS.D7BJ.BYEG',
        1588: '10.7483/OPENDATA.CMS.HXNW.6KKK',
        1589: '10.7483/OPENDATA.CMS.73DT.ASJS',
        1590: '10.7483/OPENDATA.CMS.NKYE.HJK9',
        1591: '10.7483/OPENDATA.CMS.CG8H.BYSK',
        1592: '10.7483/OPENDATA.CMS.CYDJ.SRGR',
        1593: '10.7483/OPENDATA.CMS.BY6Y.7XG9',
        1594: '10.7483/OPENDATA.CMS.8Z65.HCQP',
        1595: '10.7483/OPENDATA.CMS.WUTT.HEVB',
        1596: '10.7483/OPENDATA.CMS.PPG2.SMMR',
        1597: '10.7483/OPENDATA.CMS.RS4N.ASTQ',
        1598: '10.7483/OPENDATA.CMS.QFGX.WD6P',
        1599: '10.7483/OPENDATA.CMS.8AXG.MKR4',
        1600: '10.7483/OPENDATA.CMS.3SK5.62JZ',
        1601: '10.7483/OPENDATA.CMS.2JNC.K65J',
        1602: '10.7483/OPENDATA.CMS.C92E.U2AH',
        1603: '10.7483/OPENDATA.CMS.JAKG.T248',
        1604: '10.7483/OPENDATA.CMS.87NH.MW74',
        1605: '10.7483/OPENDATA.CMS.79TB.DPW8',
        1606: '10.7483/OPENDATA.CMS.E2SY.QM37',
        1607: '10.7483/OPENDATA.CMS.EZKX.D9AU',
        1608: '10.7483/OPENDATA.CMS.VDSC.RMYB',
        1609: '10.7483/OPENDATA.CMS.P5A8.MRQN',
        1610: '10.7483/OPENDATA.CMS.M8SR.A4GR',
        1611: '10.7483/OPENDATA.CMS.YZXV.3KB9',
        1612: '10.7483/OPENDATA.CMS.QKJW.BJGY',
        1613: '10.7483/OPENDATA.CMS.UY5P.JH9H',
        1614: '10.7483/OPENDATA.CMS.7CGC.HQQF',
        1615: '10.7483/OPENDATA.CMS.PZWS.FCZH',
        1616: '10.7483/OPENDATA.CMS.2UW6.KY6M',
        1617: '10.7483/OPENDATA.CMS.NPGP.5JH9',
        1618: '10.7483/OPENDATA.CMS.B7AU.EP94',
        1619: '10.7483/OPENDATA.CMS.QEMB.3WV2',
        1620: '10.7483/OPENDATA.CMS.S976.NCGF',
        1621: '10.7483/OPENDATA.CMS.25UM.SHS8',
        1622: '10.7483/OPENDATA.CMS.3F4C.YEE5',
        1623: '10.7483/OPENDATA.CMS.X4WM.EDRT',
        1624: '10.7483/OPENDATA.CMS.GQHR.SEQF',
        1625: '10.7483/OPENDATA.CMS.J44N.S7SU',
        1626: '10.7483/OPENDATA.CMS.W9KY.C8C9',
        1627: '10.7483/OPENDATA.CMS.AGS4.CBN8',
        1628: '10.7483/OPENDATA.CMS.PPAU.YSMN',
        1629: '10.7483/OPENDATA.CMS.8V6Q.F7TN',
        1630: '10.7483/OPENDATA.CMS.69AS.YDUF',
        1631: '10.7483/OPENDATA.CMS.PVMZ.QEYQ',
        1632: '10.7483/OPENDATA.CMS.UM9N.54X2',
        1633: '10.7483/OPENDATA.CMS.U7P6.CKVB',
        1634: '10.7483/OPENDATA.CMS.3H7E.UVVA',
        1635: '10.7483/OPENDATA.CMS.W32C.8MSV',
        1636: '10.7483/OPENDATA.CMS.M6DQ.SB9N',
        1637: '10.7483/OPENDATA.CMS.CE6Y.X78E',
        1638: '10.7483/OPENDATA.CMS.AYNJ.DVM3',
        1639: '10.7483/OPENDATA.CMS.Q2TQ.ZVF6',
        1640: '10.7483/OPENDATA.CMS.JCDC.9CUH',
        1641: '10.7483/OPENDATA.CMS.RNK8.M6NR',
        1642: '10.7483/OPENDATA.CMS.74ZB.STJC',
        1643: '10.7483/OPENDATA.CMS.236Q.R8TQ',
        1644: '10.7483/OPENDATA.CMS.FHQF.BQ53',
        1645: '10.7483/OPENDATA.CMS.4TQG.Q2SY',
        1646: '10.7483/OPENDATA.CMS.5GG4.DBJ5',
        1647: '10.7483/OPENDATA.CMS.FG73.WJ46',
        1648: '10.7483/OPENDATA.CMS.95DX.4BMP',
        1649: '10.7483/OPENDATA.CMS.6FGH.RMKT',
        1650: '10.7483/OPENDATA.CMS.BF8Y.7WSJ',
        1651: '10.7483/OPENDATA.CMS.XWVK.M4VG',
        1652: '10.7483/OPENDATA.CMS.UHTP.T7WF',
        1653: '10.7483/OPENDATA.CMS.SHE7.2B6V',
        1654: '10.7483/OPENDATA.CMS.4C7T.ABQB',
        1655: '10.7483/OPENDATA.CMS.8WEU.B6D8',
        1656: '10.7483/OPENDATA.CMS.39DX.GD5E',
        1657: '10.7483/OPENDATA.CMS.6R4H.NHMN',
        1658: '10.7483/OPENDATA.CMS.B2CK.Q4AQ',
        1659: '10.7483/OPENDATA.CMS.9BT8.5DRB',
        1660: '10.7483/OPENDATA.CMS.EG8Z.8AFD',
        1661: '10.7483/OPENDATA.CMS.FGDH.9YJ9',
        1662: '10.7483/OPENDATA.CMS.VNS2.C226',
        1663: '10.7483/OPENDATA.CMS.ZKQ8.NRMD',
        1664: '10.7483/OPENDATA.CMS.2AEX.34VT',
        1665: '10.7483/OPENDATA.CMS.7D6V.YTKX',
        1666: '10.7483/OPENDATA.CMS.PTSP.YCQ7',
        1667: '10.7483/OPENDATA.CMS.QNZU.CCWV',
        1668: '10.7483/OPENDATA.CMS.N4B2.4DKV',
        1669: '10.7483/OPENDATA.CMS.89DA.G2QV',
        1670: '10.7483/OPENDATA.CMS.G6N5.S9CE',
        1671: '10.7483/OPENDATA.CMS.KZV6.W86V',
        1672: '10.7483/OPENDATA.CMS.GHZE.PZER',
        1673: '10.7483/OPENDATA.CMS.MVVE.33HX',
        1674: '10.7483/OPENDATA.CMS.HB9Y.8B4H',
        1675: '10.7483/OPENDATA.CMS.Q7MA.G5CR',
        1676: '10.7483/OPENDATA.CMS.PM7G.7PGC',
        1677: '10.7483/OPENDATA.CMS.4TH5.SVD6',
        1678: '10.7483/OPENDATA.CMS.A354.RGSQ',
        1679: '10.7483/OPENDATA.CMS.A5DW.6RSE',
        1680: '10.7483/OPENDATA.CMS.4GWY.M6BX',
    }
    return dois[recid]


def get_category(title):
    """Guess category for the title."""
    title_lower = title.lower()

    if 'lambda' in title_lower or \
       'Bu' in title or \
       'Bd' in title or \
       'jpsi' in title_lower or \
       'upsilon' in title_lower:
        return 'B-physics'

    elif 'higgs2p' in title_lower or \
         'bsm' in title_lower or \
         'graviton2' in title_lower or \
         'higgs0' in title_lower:
        return 'BSM Higgs'

    elif 'matchingup' in title_lower or \
         'matchingdown' in title_lower or \
         'scaleup' in title_lower or \
         'scaledown' in title_lower or \
         re.search(r'tt_weights.*auet2', title_lower) or \
         '_mt' in title_lower or \
         '_mass' in title_lower:
        return 'SM Systematic Variations'

    elif 'higgs' in title_lower or \
         'hto' in title_lower or \
         '_hcontin' in title_lower or \
         '_smhcontin' in title_lower or \
         'h_m' in title_lower:
        return 'SM Higgs'

    elif 'HT' in title or \
         'Pt' in title or \
         'enriched' in title_lower or \
         re.search(r'[0-9]jet', title_lower):
        return 'SM Exclusive'

    return 'SM Inclusive'


def get_brief_title(title):
    "Return brief version of the dataset title."
    return title.split("/")[1]


def get_title_heading(title):
    "Return nice title heading for title."
    return "Simulated dataset %s in AODSIM format for 2011 collision data (%s)" % (get_brief_title(title), get_category(title))


def get_generator_text(dataset):
    """Return generator text for given dataset."""
    import os
    from create_config_file_records import get_title as get_generator_title
    from create_config_file_records import get_process
    config_ids = get_from_deep_json(get_das_json(dataset), 'config_id')
    if isinstance(config_ids, str):
        config_ids = [config_ids, ]
    process = ''
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            if process:
                process += ' '
            process += get_process(afile)
    lhe_info_needed = False
    out = '<p>'
    out += '<strong>Step %s</strong>' % process
    out += '<br>Release: %s' % get_from_deep_json(get_das_json(dataset), 'release')
    out += '<br>Global tag: %s' % get_from_deep_json(get_das_json(dataset), 'conditions')
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            generator_text = get_generator_title(afile)
            out += '<br><a href="/record/%s">%s</a>' % (LINK_INFO[config_id], generator_text)
            if 'LHE' in generator_text:
                lhe_info_needed = True
    out += '<br>Output dataset: %s' % dataset
    out += '</p>'
    if lhe_info_needed:
        out += """
        <p><strong>Note</strong>
        <br>
To extract the exact LHE configuration, you can use the following script available in the <a href="/getting-started/CMS">CMS working environment</a> on the <a href="/VM/CMS">CMS Open Data VM</a>:

        <blockquote>
        <pre>
$ dumpLHEHeader.py input=file:somefile.root output=testout.lhe
        </pre>
        </blockquote>

where <code>"somefile.foot"</code> is one of the root files in this dataset.

For example, in the existing working area, you can read the generator information directly from any of the root files of this dataset on the CERN Open Data area (the path to the root files is available from the file index of the record):

        <blockquote>
        <pre>
cd CMSSW_5_3_32/src
cmsenv
dumpLHEHeader.py input=file:root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/TTJets_MSDecays_dileptonic_matchingdown_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6_ext1-v1/60000/0282B13B-490E-E511-8E8A-001E67A3EF70.root output=testout.lhe
        </pre>
        </blockquote>
        </p>
        """
    return """
%s
""" % out


def get_all_generator_text(dataset):
    """Return generator text for given dataset and all its parents."""
    out = '<p>These data were processed in several steps:</p>'
    input_dataset = dataset
    out_blocks = []
    while input_dataset:
        out_blocks.append(get_generator_text(input_dataset))
        input_dataset = get_input_dataset(get_das_json(input_dataset))
    out_blocks.reverse()
    return out + "".join(out_blocks)


def get_number_of_events(das):
    "Return number of events from DAS json."
    return get_from_deep_json(das, 'nevents')


def get_number_of_files(das):
    "Return number of files from DAS json."
    return get_from_deep_json(das, 'nfiles')


def get_number_of_bytes(das):
    "Return number of bytes from DAS json."
    return get_from_deep_json(das, 'size')


def get_cmssw_release(das):
    "Return CMSSW release number from DAS json."
    return get_from_deep_json(das, 'release')


def get_global_tag(das):
    "Return global tagfrom DAS json."
    global_tag = get_from_deep_json(das, 'conditions')
    return global_tag.replace('::All', '')


def get_generators(das):
    "Return string representing list of generators from the DAS json."
    generators = get_from_deep_json(das, 'generators')
    if isinstance(generators, list):
        generators = " ".join(generators)
    return generators


def main():
    """Do the main job."""

    print "<collection>"
    recid = 1300
    for title in open('./inputs/cms-mc-nov-2015.txt', 'r').readlines():
        title = title.strip()
        dataset = title
        das = get_das_json(title)
        print RECORD_TEMPLATE % \
            {
                'recid': str(recid),
                'category': get_category(title),
                'doi': get_doi(recid),
                'dataset': dataset,
                'nb_events': get_number_of_events(das),
                'nb_files': get_number_of_files(das),
                'nb_bytes': get_number_of_bytes(das),
                'cmssw_release': get_cmssw_release(das),
                'generators': get_generators(das),
                'global_tag': get_global_tag(das),
                'title': title,
                'title_heading': get_title_heading(title),
                'raw': title,
                'generator_parameters': '<![CDATA[' + get_all_generator_text(dataset) + ']]>',
                '8567s': create_8567s(dataset),
                'FFTs': create_FFTs(dataset),
            }
        recid += 1
    print "</collection>"


if __name__ == '__main__':
    main()
