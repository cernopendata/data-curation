#!/usr/bin/env python

import json
import datetime
import requests

import sys
sys.path.insert(1, '../cms-release-info')

"""
Create a luminosity record.
"""

RECID_START = 1055
YEAR_RELEASED = 2015



def create_record(recid, year, uncertainty, lumi_ref, val_recid):
    """Create record for the given year."""

    rec = {}

    year_created = year
    year = str(year)
    year_published = datetime.date.today().strftime("%Y")
    # NB the reference needs to be to cds for this to work:
    url = lumi_ref+'/?of=tm&ot=245__a'
    lumi_ref_title = requests.get(url).text.strip()

    rec["abstract"] = {}

    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year='+year+'&released=yes'
    od_runs = json.loads(requests.get(url).text.strip())

    rec["abstract"]["description"] = (
            "<p>CMS measures the luminosity using different luminometers (luminosity detectors) and algorithms. The luminometer giving the best value for each luminosity section is recorded in a 'normtag' file <a href=\"/record/%s/files/normtag_PHYSICS_%s.json\">normtag_PHYSICS_%s.json</a> that is used in the luminosity calculation.</p>" % (recid, year, year)
            + "<p>The integrated luminosity for validated runs and luminosity sections of the %s public data (%s) is available in %slumi.txt (The integrated luminosity for validated runs and luminosity sections of all %s p-p data taking is available in %slumi.txt.)</p>" % (year, ",".join(od_runs),  ",".join(od_runs), year, year)
            + "<p> For luminosity calculation, a detailed list of luminosity by lumi section is provided in <a href=\"/record/%s/files/%slumibyls.csv\">%slumibyls.csv</a> for the <a href=\"/record/%s\">list of validated runs</a> and lumi sections.</p>" % (recid, year, year, val_recid)
            + "<p>The uncertainty in the luminosity measurement of %s data should be considered as %s%% (reference <a href=\"%s\">%s</a>).</p>" % (year, uncertainty, lumi_ref, lumi_ref_title)
            + "<p>In your estimate for the integrated luminosity, check for which runs the trigger you have selected is active and sum the values for those runs. If you are using prescaled triggers, you can find the trigger prescale factors as shown in <a href=\"/record/5004\">the trigger examples</a>. The change of prescales (run, lumi section, index of prescales) is recorded in <a href=\"/record/%s/files/prescale%s.csv\">prescale%s.csv</a></p>" % (recid, year, year)
            + "<p>Additional information on how to extract luminosity values using the <strong>brilcalc tool</strong> can be found in the <a href=\"/docs/cms-guide-luminosity-calculation\"> luminosity calculation guide</a>.</p>"
        )

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Luminosity-Information",
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

    rec["links"] = {}
    rec["links"]["url"] = lumi_ref
    rec["links"]["title"] = lumi_ref_title

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    rec["relations"] = {}
    rec["relations"]["recid"] = val_recid
    rec["relations"]["type"] = "isRelatedTo"

    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year='+year+'&type=pp-phys'
    #rec["run_period"] = read_run_periods(year, 'pp-phys')
    rec["run_period"] = json.loads(requests.get(url).text.strip())

    rec["title"] = (
        "CMS luminosity information, for %s CMS open data"
        % year
        )

    rec["type"] = {}
    rec["type"]["primary"] = "Supplementaries"
    rec["type"]["secondary"] = [
        "Luminosity",
    ]

    return rec

# @click.command()
def main():
    "Do the job."

    records = []
    recid = RECID_START
    year = str(YEAR_RELEASED)

    # this would read from the local json file
    # with open('./inputs/cms_release_info.json') as f:
    #      data = f.read()
    
    # # reconstructing the data as a dictionary
    # all_years = json.loads(data)    
    # this_year = all_years[year]

    # this gets json from the api server
    url = 'http://api-server-cms-release-info.app.cern.ch/years?year='+year+'&output=plain'
    this_year = json.loads(requests.get(url).text.strip())
    
    records.append(
        create_record(
            recid,
            this_year["year"],
            this_year["lumi_uncertainty"],
            this_year["luminosity_reference"],
            this_year["val_json"][0]["recid"]) # This requires the json files to be in a specific order, with "golden" first
    )



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

