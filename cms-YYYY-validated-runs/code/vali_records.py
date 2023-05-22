#!/usr/bin/env python

import json
import datetime
import requests

import sys
sys.path.insert(1, '../cms-release-info')
from helpers import run_range_text

"""
Create validated data records.

Input arguments
- recid (May 2023, the last used recid was 14210 for 2015 pp)
- year to be released
- run era (for pp, give one of the released eras, it is needed to get the collision energy, stored per era)
- type (pp, pPb, pphiref, PbPb)

Inputs:
- 2013 pPb: 14216 2013 HIRun2013 pPb
- 2013 ppref: 14218 2013 Run2013A pphiref
- 2015 ppref: 14212 2015 Run2015E pphiref
- 2015 pp:  14210 2015 Run2015D pp (not used to build the current record, but tested to produce the same files)

"""

def create_record(recid, year, era, runtype, filename):
    """Create record for the given year."""

    rec = {}

    year=str(year)
    year_created = year
    year_published = datetime.date.today().strftime("%Y")
    runtype = str(runtype)
    # print(year)
    # print(runtype)
    # print(era)
    if "pphiref" in runtype :
        display_runtype = 'pp'
    else:
        display_runtype = runtype

    # Get the energy
    # Using the run_era, for pp it is needed only here
    # Could be done differently but this is good enough
    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/?run_era='+era
    this_json=json.loads(requests.get(url).text.strip())
    energy=this_json[0]["energy"]

    #print(energy)

    if "Muon" in filename:
        muon_text = ', only valid muons'
        muon_desc = ', for analyses requiring only valid muons'
    else:
        muon_text = ''
        muon_desc = ''

    run_range_input = era
    if "pphiref" in runtype:
        collision_text = energy+' proton-proton collision data, needed as reference data for heavy-ion data analysis,'
    elif "PbPb" in runtype:
        collision_text = energy+' PbPb heavy-ion collision data'
    elif "pPb" in runtype:
        collision_text = energy+' proton-Pb heavy-ion collision data'
    elif "pp" in runtype:
        collision_text = energy+' proton-proton collision data'
        run_range_input = year
    else:
        print('Runtype unknown!')

    # The input to run_range_text depends on runtype, defined above
    # Usage: era for HI, HI pp ref, year for normal pp
    # run_range_text takes care of taking only released runs when year as input 
    rec["abstract"] = {}
    rec["abstract"]["description"] = (
            "<p>This file describes which luminosity sections in which runs are considered good and should be processed"+muon_desc+".</p><p>This list covers "+collision_text+
            " taken in "+year+"."+run_range_text(run_range_input)+"</p>"
        )

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Validated-Runs",
        "CMS-Validation-Utilities"
    ]

    rec["collision_information"] = {}
    rec["collision_information"]["energy"] = energy

    rec["collision_information"]["type"] = display_runtype

    rec["date_created"] = [
        year_created,
    ]
    rec["date_published"] = year_published

    rec["experiment"] = "CMS"

    rec["license"] = {}
    rec["license"]["attribution"] = "CC0"

    #rec["links"] = {}

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    # Get run periods from the json file server (takes also not released)
    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year='+year+'&type='+runtype+'-phys'
    rec["run_period"] = json.loads(requests.get(url).text.strip())    

    rec["title"] = (
        "CMS list of validated runs "+filename
        )
    
    rec["title_additional"] = (
        "CMS list of validated runs for "+collision_text+" taken in "+year+muon_text
        )

    rec["type"] = {}
    rec["type"]["primary"] = "Environment"
    rec["type"]["secondary"] = [
        "Validation",
    ]

    rec["usage"] = {}
    rec["usage"]["description"] = (
            "<p>Add the following lines in the configuration file for a cmsRun job: <br /> <pre>   import FWCore.ParameterSet.Config as cms</pre><pre>   import FWCore.PythonUtilities.LumiList as LumiList</pre><pre>   goodJSON = '"+filename+"'</pre><pre>   myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',') </pre></p><p> Add the file path if needed in the file name.</p><p> Add the following statements after the <code>process.source</code> input file definition: <br /><pre>   process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()</pre><pre>   process.source.lumisToProcess.extend(myLumis)</pre></p><p>Note that the two last statements must be placed after the <code>process.source</code> statement defining the input files.</p>"
        )

    rec["validation"] = {}
    rec["validation"][
        "description"
    ] = "During data taking all the runs recorded by CMS are certified as good for physics analysis if all subdetectors, trigger, lumi and physics objects (tracking, electron, muon, photon, jet and MET) show the expected performance. Certification is based first on the offline shifters evaluation and later on the feedback provided by detector and Physics Object Group experts. Based on the above information, which is stored in a specific database called Run Registry, the Data Quality Monitoring group verifies the consistency of the certification and prepares a json file of certified runs to be used for physics analysis. For each reprocessing of the raw data, the above mentioned steps are repeated. For more information see:"
    rec["validation"]["links"] = [
        {
            "description": "The Data Quality Monitoring Software for the CMS experiment at the LHC: past, present and future",
            "url": "https://www.epj-conferences.org/articles/epjconf/pdf/2019/19/epjconf_chep2018_02003.pdf",
        },
    ]

    return rec

# @click.command()
def main():
    "Do the job."

    records = []
    recid = sys.argv[1]
    year = sys.argv[2]
    era = sys.argv[3]
    runtype = sys.argv[4]

    # this would read from a local file
    # with open('./inputs/cms_release_info.json') as f:
    #      data = f.read()
    
    # # reconstructing the data as a dictionary
    # all_years = json.loads(data)    
    # this_year = all_years[year]

    # this gets json from the api server
    url = 'http://api-server-cms-release-info.app.cern.ch/years?year='+year+'&type='+runtype+'&output=plain'
    this_json = json.loads(requests.get(url).text.strip())
    
    recid=int(recid)
    for val in this_json["val_json"]:
        records.append(
            create_record(
                str(recid),
                this_json["year"],
                era,
                runtype,
                val["url"].split("/")[-1].strip())
                #row["val_json_golden"].split("/")[-1].strip())
        )
        recid += 1


    print(
        json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    )


if __name__ == "__main__":
    main()

