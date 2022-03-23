#!/usr/bin/env python

import json
import datetime
import subprocess
import requests

import sys
sys.path.insert(1, '../cms-release-info')
from helpers import *

"""
Create validated data records.
"""

RECID_START = 14212
YEAR_RELEASED = 2015

def create_record(recid, year, filename):
    """Create record for the given year."""

    rec = {}

    year_created = year
    year = str(year)
    year_published = datetime.date.today().strftime("%Y")

    if "Muon" in filename:
        muon_text = ', only valid muons'
        muon_desc = ', for analyses requiring only valid muons'
    else:
        muon_text = ''
        muon_desc = ''

    
    rec["abstract"] = {}
    rec["abstract"]["description"] = (
            "<p>This file describes which luminosity sections in which runs are considered good and should be processed%s.</p>" % muon_desc
            + "<p>This list covers proton-proton data taking in %s.%s</p>" % (year, run_range_text(year))
        )

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Validated-Runs",
        "CMS-Validation-Utilities"
    ]

    rec["collision_information"] = {}
    rec["collision_information"]["energy"] = "13TeV"
    rec["collision_information"]["type"] = "pp"

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

    # Implement a check to see which run periods actually are in the json file 
    rec["run_period"] = read_run_periods(year, 'pp-phys')

    rec["title"] = (
        "CMS list of validated runs %s"
        % filename
        )
    
    rec["title_additional"] = (
        "CMS list of validated runs for primary datasets of %s data taking%s"
        % (year, muon_text)
        )

    rec["type"] = {}
    rec["type"]["primary"] = "Environment"
    rec["type"]["secondary"] = [
        "Validation",
    ]

    rec["usage"] = {}
    rec["usage"]["description"] = (
            "<p>Add the following lines in the configuration file for a cmsRun job: <br /> <pre>   import FWCore.ParameterSet.Config as cms</pre><pre>   import FWCore.PythonUtilities.LumiList as LumiList</pre><pre>   goodJSON = '%s'</pre><pre>   myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',') </pre></p><p> Add the file path if needed in the file name.</p><p> Add the following statements after the <code>process.source</code> input file definition: <br /><pre>   process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()</pre><pre>   process.source.lumisToProcess.extend(myLumis)</pre></p><p>Note that the two last statements must be placed after the <code>process.source</code> statement defining the input files.</p>" % (filename)
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
    recid = RECID_START
    year = str(YEAR_RELEASED) 

    # this would read from a local file
    # with open('./inputs/cms_release_info.json') as f:
    #      data = f.read()
    
    # # reconstructing the data as a dictionary
    # all_years = json.loads(data)    
    # this_year = all_years[year]

    # this gets json from the api server
    url = 'http://api-server-cms-release-info.app.cern.ch/years/'+year
    this_year = json.loads(requests.get(url).text.strip())
    
    for val in this_year["val_json"]:
        records.append(
            create_record(
                recid,
                this_year["year"],
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

