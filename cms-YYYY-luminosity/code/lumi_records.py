#!/usr/bin/env python

import json
import datetime
import requests

import sys

sys.path.insert(1, "../cms-release-info")

"""
Create a luminosity record.
Input arguments
- recid (May 2023, the last used recid was 1055 for 2015 pp)
- year to be released
- run era (for pp, give one of the released eras, it is needed to get the collision energy, stored per era)
- type (pp, pPb, pphiref, PbPb)

Inputs:
- 2013 pPb: 1056 2013 HIRun2013 pPb
- 2013 ppref: 1057 2013 Run2013A pphiref
- 2015 ppref: 1058 2015 Run2015E pphiref
- 2015 pp: 1055 2015 Run2015D pp (not used to build the current record, but tested to produce the same files)

"""


def create_record(recid, year, era, runtype, uncertainty, lumi_ref, val_recid):
    """Create record for the given year."""

    rec = {}

    year_created = year
    year_published = datetime.date.today().strftime("%Y")
    runtype = str(runtype)
    if "pphiref" in runtype:
        display_runtype = "pp"
    else:
        display_runtype = runtype

    # Get the energy
    # Using the run_era, for pp it is needed only here
    # Could be done differently but this is good enough
    url = "http://api-server-cms-release-info.app.cern.ch/runeras/?run_era=" + era
    this_json = json.loads(requests.get(url).text.strip())
    energy = this_json[0]["energy"]

    # NB the reference needs to be to cds for this to work:
    url = lumi_ref + "/?of=tm&ot=245__a"
    lumi_ref_title = requests.get(url).text.strip()

    pp_text = ""
    if "pphiref" in runtype:
        collision_text = (
            energy
            + " proton-proton collision data, needed as reference data for heavy-ion data analysis,"
        )
    elif "PbPb" in runtype:
        collision_text = energy + " PbPb heavy-ion collision data"
    elif "pPb" in runtype:
        collision_text = energy + " proton-Pb heavy-ion collision data"
    elif "pp" in runtype:
        collision_text = energy + " proton-proton collision data"
        run_range_input = year
        pp_text = (
            "(The integrated luminosity for validated runs and luminosity sections of all "
            + year
            + " p-p data taking is available in "
            + year
            + "lumi.txt.)"
        )
    else:
        print("Runtype unknown!")

    # additional text for pPb reverse luminosity
    inverse_text = ""
    if "pPb" in runtype:
        url = "http://api-server-cms-release-info.app.cern.ch/years/lumi_uncertainty_reverse?year=2013&type=pPb"
        reverse_lumi = json.loads(requests.get(url).text.strip())[0]
        inverse_text = (
            "("
            + str(reverse_lumi)
            + "% for the reverse beam direction) "
        )

    # normtag file only after Run-1
    normtag_text = ""
    if int(year) > 2014:
        normtag_text = (
            'The luminometer giving the best value for each luminosity section is recorded in a <strong>normtag</strong> file <a href="/record/'
            + str(recid)
            + "/files/normtag_PHYSICS_"
            + runtype
            + "_"
            + year
            + '.json">normtag_PHYSICS_'
            + runtype
            + "_"
            + year
            + ".json</a> that is used in the luminosity calculation."
        )

    rec["abstract"] = {}

    url = (
        "http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year="
        + year
        + "&type="
        + runtype
        + "-phys&released=yes"
    )
    od_runs = json.loads(requests.get(url).text.strip())

    # The use of variable in string with two different notations could be fixed in the following...
    # NB in the  +var+ notation, var needs to be a string
    rec["abstract"]["description"] = (
        "<p>CMS measures the luminosity using different luminometers (luminosity detectors) and algorithms. "
        + normtag_text
        + "</p>"
        "<p>The integrated luminosity for validated runs and luminosity sections of the %s taken in %s (%s) is available in %slumi.txt. %s</p>"
        % (collision_text, year, ",".join(od_runs), ",".join(od_runs), pp_text)
        + '<p> For luminosity calculation, a detailed list of luminosity by lumi section is provided in <a href="/record/%s/files/%s_%slumibyls.csv">%s_%slumibyls.csv</a> for the <a href="/record/%s">list of validated runs</a> and lumi sections.</p>'
        % (recid, runtype, year, runtype, year, val_recid)
        + '<p>The uncertainty in the luminosity measurement of %s data should be considered as %s%% %s(reference <a href="%s">%s</a>).</p>'
        % (year, uncertainty, inverse_text, lumi_ref, lumi_ref_title)
        + '<p>In your estimate for the integrated luminosity, check for which runs the trigger you have selected is active and sum the values for those runs. For prescaled triggers, the change of prescales (run, lumi section, index of prescales referring to the PrescaleService module in the High-Level Trigger configuration files) is recorded in <a href="/record/%s/files/prescale_%s%s.csv">prescale_%s%s.csv</a>.</p>'
        % (recid, runtype, year, runtype, year)
        + '<p>Additional information on how to extract luminosity values using the <strong>brilcalc tool</strong> can be found in the <a href="/docs/cms-guide-luminosity-calculation"> luminosity calculation guide</a>.</p>'
    )

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Luminosity-Information",
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

    rec["links"] = {}
    rec["links"] = [{"url": lumi_ref, "title": lumi_ref_title}]

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    rec["relations"] = {}
    rec["relations"] = [{"recid": str(val_recid), "type": "isRelatedTo"}]

    url = (
        "http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year="
        + year
        + "&type="
        + runtype
        + "-phys"
    )
    # rec["run_period"] = read_run_periods(year, 'pp-phys')
    rec["run_period"] = json.loads(requests.get(url).text.strip())

    rec["title"] = (
        "CMS luminosity information for " + collision_text + " taken in " + year
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
    recid = sys.argv[1]
    year = sys.argv[2]
    era = sys.argv[3]
    runtype = sys.argv[4]

    # this would read from the local json file
    # with open('./inputs/cms_release_info.json') as f:
    #      data = f.read()

    # # reconstructing the data as a dictionary
    # all_years = json.loads(data)
    # this_year = all_years[year]

    # this gets json from the api server
    url = (
        "http://api-server-cms-release-info.app.cern.ch/years?year="
        + year
        + "&type="
        + runtype
        + "&output=plain"
    )
    this_year = json.loads(requests.get(url).text.strip())

    records.append(
        create_record(
            recid,
            year,
            era,
            runtype,
            this_year["lumi_uncertainty"],
            this_year["luminosity_reference"],
            this_year["val_json"][0]["recid"],
        )  # This requires the json files to be in a specific order, with "golden" first
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
