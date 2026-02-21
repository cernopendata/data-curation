###############################################################################
# (c) Copyright 2023 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

"""
Create a record for the Open Data Portal from a given Bookkeeping path
"""

# DIRAC imports
from DIRAC import initialize
from DIRAC.Interfaces.API.Dirac import Dirac
from LHCbDIRAC.DataManagementSystem.Client.DMScript import DMScript
from LHCbDIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
from LHCbDIRAC.BookkeepingSystem.Client.BookkeepingClient import BookkeepingClient
from DIRAC.Core.Base.Script import Script
from DIRAC import gLogger, exit as diracExit

# Python imports
import argparse
import re
import os
import datetime
import json
import yaml
import requests
from jsonschema import validate
from collections import Counter

"""
Relevant fields from the JSON schema of the Open Data Portal 
Full schema at http://opendata.cern.ch/schema/records/record-v1.0.0.json
"""
odp_record = {
    "abstract": {
        "description": ""
    },
    "accelerator": "CERN-LHC",
    "collaboration": {
        "name": "LHCb collaboration",
        # LHCb author list for the {year} data release (455 for 2011 and 456 for 2012)
        "recid": ""
    },
    "recid": "",
    "collections": [
        "LHCb-Primary-Datasets"
    ],
    "collections": [],
    "collision_information": {
        "energy": "",
        "type": ""
    },
    "date_created": [],
    "date_published": "",
    "experiment": "LHCb",
    "stripping": {
        "version": "",
        "stream": ""
    },
    "distribution": {
        "formats": [],
        "number_events": 0,
        "number_files": 0,
        "size": 0
    },
    "magnet_polarity": "",
    "methodology": {
        "description": "",
        "steps": [],
    },
    "publisher": "CERN Open Data Portal",
    "run_period": [],
    "title": "",
    "title_additional": "",  # Will apear as a subtitle in the OD display
    "type": {
        "primary": "Dataset",
        "secondary": []
    },
    "usage": {
        "description": "<p> The data collected by the LHCb detector is available in .DST and .mDST formats. The data files can be explored using LHCb software but it is best to write the relevant columns to ROOT Tuples or preferred data format. <p> Instructions for exploring a DST and writing out ROOT tuples are available in LHCb Starterkit below. For \"tupling\" jobs, software called DaVinci is mainly used within LHCb, its documentation is also available bellow.",
        "links": [
            {
                "description": "LHCb StarterKit",
                "url": "https://lhcb.github.io/starterkit-lessons/first-analysis-steps/minimal-dv-job.html"
            },
            {
                "description": "DaVinci",
                "url": "http://lhcbdoc.web.cern.ch/lhcbdoc/davinci/"
            },
        ]
    }
}


# Helper functions


def point_to_authors_list(year):

    authorsreciddict = {"2011": "455",
                        "2012": "456"}

    return authorsreciddict[year]


def assign_recids(bkPath):
    """
    Assign record ID (recid) to a given Bookkeeping path. 

    LHCb record IDs start with 24500 and go by the order appearing in the
    config. 
    """
    bkpaths = []
    recids = []
    recid_dict = {}

    recid = 24500
    for dir in conf["directory"]:
        for stream in conf["stream"]:
            bkpaths.append(str(dir+stream))
            recids.append(recid)
            recid += 1

    for bkpath, recid in zip(bkpaths, recids):
        recid_dict[bkpath] = recid

    return str(recid_dict[bkPath])


def get_stream(bkPath):
    """
    Returns the stripping stream for a given bookkeeping path
    """
    stream = bkPath.split("/")[-1].removesuffix(".MDST").removesuffix(".DST")
    return str(stream)


def get_record_dict(res, verbose):
    """
    Return a dictionary for specified dirac query. 
    """
    if not res['OK']:
        gLogger.error("Error getting statistics from BK")
        diracExit(1)

    if res["Value"]["Records"] == [[0, None, None, None, None]]:
        gLogger.error("There are no records for this stream")
        diracExit(1)

    if "ParameterNames" in res["Value"]:
        paramNames = res['Value']['ParameterNames']
        records = [dict(zip(paramNames, record))
                   for record in res['Value']['Records']]
        if verbose:
            print("Found %d records that look like:" % len(records) + "\n")
            print(json.dumps(records[0], indent=4,
                  sort_keys=True, default=str))

    elif "Parameters" in res["Value"]:
        records = {key: dict(value) for key, value in list(
            res['Value']['Records'].items())}
        if verbose:
            print(json.dumps(records, indent=4, sort_keys=True, default=str))

    return records


def get_dataset_type(queryDict):
    """
    Returns the type of a dataset (Collision or Simulated).
    """
    return {
        "LHCb": "Collision",
        "MC": "Simulated",
    }[queryDict["ConfigName"]]


def get_run(year):
    """
    Returns either Run1 or Run2 according to the year of data taking.
    """
    if year == "2011" or "2012" or "2013":
        return "Run1"
    elif year == "2015" or "2016" or "2017" or "2018":
        return "Run2"


def get_collision_type(queryDict):
    """
    Returns type of the collision
    """
    if queryDict["ConfigName"] == "LHCb":
        type_name = "".join(filter(str.isalpha, queryDict["ConfigVersion"]))
        return {
            "Collision": "pp",                # proton-proton
            "Ionproton": "Pbp",
            "Protonion": "pPb",
            "Lead": "PbPb",
            "Protonargon": "PbAr",
            "Protonhelium": "PbHe",
            "Xenon": "XeXe",
        }[type_name]
    else:
        # TODO: For MC, the ConfigVersion is just the year. Need to get collision type from the Gauss step
        raise NotImplementedError()


def get_collision_type_text(queryDict):
    """
    Returns type of the collision in text
    """
    if queryDict["ConfigName"] == "LHCb":
        type_name = "".join(filter(str.isalpha, queryDict["ConfigVersion"]))
        return {
            "Collision": "proton-proton (pp)",                # proton-proton
            "Ionproton": "lead-proton (Pbp)",
            "Protonion": "proton-lead (pPb)",
            "Lead": "lead-lead (PbPb)",
            "Protonargon": "lead-argon (PbAr)",
            "Protonhelium": "lead-helium (PbHe)",
            "Xenon": "xenon-xenon (XeXe)",
        }[type_name]
    else:
        # TODO: For MC, the ConfigVersion is just the year. Need to get collision type from the Gauss step
        raise NotImplementedError()


def get_year(queryDict):
    """
    Returns the year of data taking
    """
    if queryDict["ConfigName"] == "LHCb":
        year = re.search(r"\d\d", queryDict["ConfigVersion"]).group(0)
        return "20"+year
    elif queryDict["ConfigName"] == "MC":
        return queryDict["ConfigVersion"]
    else:
        raise NotImplementedError()


def get_energy(queryDict):
    """
    Returns beam energy in TeV
    """
    if "BeamOff" in queryDict["ConditionDescription"]:
        return "0TeV"
    beam_energy = int(
        re.search(r"Beam(\d*)GeV", queryDict["ConditionDescription"]).group(1))
    beam_energy /= 500.  # Beam energy in GeV -> Collision energy in TeV
    return f"{beam_energy:g}TeV"


def get_file_format(queryDict):
    """
    Returns the format of the file
    """
    return queryDict["FileType"].split(".")[-1]


def printProds(title, prods, verbose):
    """
    Prints production ID and type for a given dictionary.  
    """
    typeDict = {}
    for prod, prodType in prods.items():
        typeDict.setdefault(prodType, []).append(prod)
    for prodType, prodList in typeDict.items():
        if verbose:
            print('(%s): %s' % (prodType, ','.join(
                [str(prod) for prod in sorted(prodList)])))
    return prodType, prodList[0]


def get_stripping_version(queryDict):
    """
    Get the stripping version from a query dict. 
    "a" is stripped because it introduces a missmatch between stripping project homepage 
    processing pass in the bkk path.
    """
    return (str(queryDict["ProcessingPass"]).split("/")[-1].lower().strip("a"))


def file_size(size, decimal_places=3):
    """
    Converts the file size to human readable format. 
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1000.0:
            break
        size /= 1000.0
    return f"{size:.{decimal_places}f} {unit}"


# Read in the configuration file
with open("../config.yaml", "r") as f:
    conf = yaml.safe_load(f)

# Use command line arguments via argparse.
parser = argparse.ArgumentParser()
parser.add_argument("--BK",      required=True, help="Bookkeeping Path")
parser.add_argument("--verbose", action=argparse.BooleanOptionalAction,
                    default=False, help="Verbose flag")
parser.add_argument("--staging", action=argparse.BooleanOptionalAction, default=False,
                    help="Staging flag to write out AccessURLs for the files in the BKPath")
parser.add_argument("--release_dir",
                    default=conf["release_dir"], help="Output directory for the metadata.")
parser.add_argument("--stagefrac", default = conf["stage_frac"], help = "Fraction of files to be staged from the data set")
parser.add_argument("--eos_existing", default=conf["eos_existing"], help = "Path to the list of existing files on eos" )
args = parser.parse_args()

def main():
    # Initialize and configure DIRAC
    initialize()

    # Documentation output via the help flag (Needs to be written up, now resorting to default)
    Script.setUsageMessage(__doc__ + '\n'.join([]))

    # Data Management Script
    dmScript = DMScript()

    # Set the binary flags for output logging and writing out files to stage on ODP
    verbose = args.verbose
    staging = args.staging

    print("Running with arguments: \n", 
          "verbose = ", verbose,   "\n", 
          "staging = ", staging,   "\n", 
          "Release Directory: ", args.release_dir)

    # Access to DIRAC scripts
    dirac = Dirac()

    # Define Transformation Client
    tfClient = TransformationClient()

    # Define the BookkeepingClient
    bkClient = BookkeepingClient()

    # Returns a BKQuery from the registered --BK switch in the Command Line using the Data Management System
    dmScript.setBKQuery(args.BK)

    bkQuery = dmScript.getBKQuery()

    # Returns the path given to --BK switch in the Command Line for a given BKQuery
    bkPath = bkQuery.getPath()

    # Returns the dictionary of data available with the BKQuery
    queryDict = bkQuery.getQueryDict()

    # Start filling in the JSON fields

    # Assign recid pointing to authors list for each record
    odp_record["collaboration"]["recid"] = point_to_authors_list(
        get_year(queryDict))

    # RecID assigned according to year -> polarity (down, then up) -> stream listed as in bkk.
    odp_record["recid"] = assign_recids(bkPath)

    if verbose:
        print("\n Assigned the following recid: " + assign_recids(bkPath))
        print("\n Obtained the following queryDict from given Bookkeeping path: ------------------------------------------------------------------------------------------------------- \n")
        print(json.dumps(queryDict, indent=4, sort_keys=True, default=str))

    # Abstract field
    odp_record["abstract"]["description"] = \
        f"""Data from {get_collision_type_text(queryDict)} collisions collected by 
  the LHCb experiment in the year {get_year(queryDict)} of {get_run(get_year(queryDict))} of the LHC."""

    # Date Published Field
    odp_record["date_published"] = str(datetime.datetime.now().year)

    # Magnet Polarity Field
    odp_record["magnet_polarity"] = str(
        queryDict["ConditionDescription"].split("-")[2])

    # Usage field, stream pages TODO will have to link to correct URL of ODP
    odp_record["usage"]["links"].append({
        "description": f"Stripping lines index for {get_stripping_version(queryDict)}",
        "url": f"/docs/{get_stripping_version(queryDict)}-index"
    })

    # Title Field is filled in with Bookkeeping path
    title_tuple = (queryDict["ConfigName"],
                   get_year(queryDict),
                   queryDict["ConditionDescription"].split("-")[0],
                   queryDict["ConditionDescription"].split("-")[2],
                   get_stream(bkPath),
                   "Stream",
                   get_stripping_version(queryDict).capitalize())

    odp_record["title"] = " ".join(title_tuple)

    # LHCb specific facet
    odp_record["stripping"]["stream"] = get_stream(bkPath)

    # There are some suffixes we don't need, they appear in the bkk path but not stripping project homepage
    odp_record["stripping"]["version"] = get_stripping_version(queryDict)

    # Collision information entries (energy, type) are filled using helper functions
    odp_record["collision_information"] = {
        "energy": get_energy(queryDict),
        "type": get_collision_type(queryDict),
    }

    # Metadata on all the files in a given bkk path
    res = bkClient.getFilesSummary(queryDict)

    # Dictionary of metadata for the first file for some general info on files
    if verbose:
        print("\n Got the files summary for your query: ------------------------------------------------------------------------------------------------------------------------------- \n")

    filesSummary = get_record_dict(res, verbose)[0]

    odp_record["distribution"] = {
        "formats":       [get_file_format(queryDict)],
        "number_events": filesSummary["NumberOfEvents"],
        "number_files":  filesSummary["NbofFiles"],
        "size":          filesSummary["FileSize"],
    }

    # Returns metadata on all files
    res = bkClient.getFilesWithMetadata(queryDict)

    # Returns dictionary of metadata for all files
    if verbose:
        print("\n Got the files metadata: --------------------------------------------------------------------------------------------------------------------------------------------- \n")

    filesWithMetadata = get_record_dict(res, verbose)

    if filesWithMetadata == []:
        print(bkPath)
        print(queryDict)
        print(filesWithMetadata)
        print(bkClient.getFilesSummary(queryDict))

    # Get date of creation from the first finished file
    if filesWithMetadata != []:
        odp_record["date_reprocessed"] = str(
            filesWithMetadata[0]["JobEnd"].year)
        odp_record["date_created"] = [get_year(queryDict)]
        odp_record["run_period"] = [get_year(queryDict)]

    # Dataset type (Collision, Simulated or Derived) goes in two places
    odp_record["type"]["secondary"] = [get_dataset_type(queryDict)]
    odp_record["collections"] = [
        f"LHCb-{get_dataset_type(queryDict)}-Datasets"]

    # Set the name of the json file to be written out
    filename = "LHCb_" + get_year(queryDict) + "_" + "_".join([
        queryDict[k] for k in ["ConditionDescription", "ProcessingPass", "FileType"]
    ]).replace(" ", "").replace("/", "_").replace("__", "_").replace(".", "_").replace("-", "_")

    # Retrieve the list of TCKs used for the files in the chose bookkeeping path
    listoftcks = [record["TCK"] for record in filesWithMetadata]
    tckcount = dict(Counter(listoftcks))

    if verbose:
        print("\n Got a count of the TCKs for your query ------------------------------------------------------------------------------------------------------------------------------ \n")
        print(tckcount)

    # Write out https access URLs for staging files on Open Data Portal
    if staging:

        stagejson = {
            "files": []
        }

        # Get LFNs and sizes from bkClient
        cumulativesize = 0
        sizewritten = 0

        # Check whether the specified path exists or not
        staging_path_exists = os.path.exists(args.release_dir + "staging/")

        # Create a new directory if it does not exist
        if not staging_path_exists:
            os.makedirs(args.release_dir + "staging/")

        # Check if list of existing files was passed to metadata_writer, if not, just create an empty list. All files will be processed. 
        if args.eos_existing != None:
            with open(args.eos_existing, "r") as f:
                existing_files = f.read()
        else: 
            existing_files = []

        for record in sorted(res["Value"]["Records"], key=lambda x: x[0]):
            if cumulativesize < int(args.stagefrac*filesSummary["FileSize"]):  # Fraction by size of files saved
                cumulativesize += int(record[2])

                repdict = dirac.getReplicas(
                    record[0], active=True, diskOnly=True)
                SE1 = list(repdict['Value']['Successful'][record[0]].keys())[0]
                urldict = dirac.getAccessURL(
                    record[0], SE1, protocol=["https"])
                url = list(urldict['Value']['Successful'].values())[0]

                # Check if file was already staged
                if "/".join(url.split("/")[-3:]) not in existing_files:
                    sizewritten += int(record[2])

                    stagejson["files"].append({
                        "sources": [url],
                        "filesize": record[2],
                        "destinations": ["https://eospublic.cern.ch/eos/opendata/lhcb/upload/" + "/".join((str(url.split("/")[-5]), get_stream(bkPath), filename, "/".join(url.split("/")[-3:])))]
                    })
                else:
                    print("/".join(url.split("/")[-3:]), " exists")

                checkpath = "/eos/opendata/lhcb/" + \
                    "/".join((str(url.split("/")[-5]), get_stream(bkPath),
                             filename, "/".join(url.split("/")[-3:])))
                with open(args.release_dir + "staging/" + f"IntegrityCheck.txt", "a") as fl:
                    fl.write(f"path={checkpath} size={record[2]}\n")
        with open(args.release_dir + "staging/" + f"{filename}_FilesToStage.txt", "w") as fl:
            json.dump(stagejson, fl, indent=2)

        # Keep track of sizes in different written out streams (up to 50TB during first OD Release)
        with open(args.release_dir + "staging/" + f"size_of_staged_files_{datetime.datetime.now().strftime('%Y_%m_%d_%H')}.txt", "a") as fl:
            fl.write(str(file_size(sizewritten)) + "\n")

    # Create a .txt file with a list of LFNs and fill in the associated fields in .json
    if verbose:
        print("\n Got a list of LFNs in the path -------------------------------------------------------------------------------------------------------------------------------------- \n")

    # Check whether the specified path exists or not

    LFNSdir = args.release_dir + "LFNS/"
    lfnspathexists = os.path.exists(LFNSdir)

    if not lfnspathexists:
        # Create a new directory because it does not exist
        os.makedirs(LFNSdir)

    lfnslist = bkQuery.getLFNs(res, printOutput=verbose)

    LFNsfilename = LFNSdir + filename + "_LFNS.txt"

    with open(LFNsfilename, "w") as fl:
        for lfn in lfnslist:
            fl.write(lfn + "\n")

    # Production summary
    res = bkClient.getProductionSummary(queryDict)

    if verbose:
        print("\n Got a production summary for your query ----------------------------------------------------------------------------------------------------------------------------- \n")

    # In principle more than one prod can write to a BK path
    prod_summaries = get_record_dict(res, verbose)

    # Get Production ID
    prodid = prod_summaries[0]["Production"]

    odp_record["methodology"]["description"] += "<p> This dataset was created in several production steps. These steps, software used and the configuration is provided below. </p> \n"
    odp_record["methodology"]["description"] += "<p> <strong> Prod ID: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong> " + \
        str(prodid) + "\n"

    if verbose:
        print(
            f"\n Retreived production information on ProdID {prodid} -------------------------------------------------------------------------------------------------------------------- \n")

    prod_info = bkClient.getProductionInformation(prodid)

    if verbose:
        print(json.dumps(odp_record, indent=4, sort_keys=True))

    # Retreive production hierarchy (steps)
    import six

    parents = {}
    productions = {}
    tr = TransformationClient()

    prods = bkQuery.getBKProductions()

    if verbose:
        print(f"\n Got list of productions: {prods}")

    for prod in prods:
        ptypeprod = tr.getTransformation(prod).get(
            'Value', {}).get('Type', 'Unknown')
        productions[prod] = ptypeprod
        parent = tr.getBookkeepingQuery(prod).get(
            'Value', {}).get('ProductionID', '')
        while isinstance(parent, six.integer_types):
            ptypeparent = tr.getTransformation(parent).get(
                'Value', {}).get('Type', 'Unknown')
            parents[parent] = ptypeparent
            parent = tr.getBookkeepingQuery(parent).get(
                'Value', {}).get('ProductionID', '')

    if not prods:
        print("No productions found!!!")
    else:
        printProds('Productions found', productions, verbose)
        odp_record["methodology"][
            "description"] += f"<p> <strong>Prod type:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </strong> {str(ptypeprod)}"
        if parents:
            partype, parid = printProds('Parent productions', parents, verbose)
            odp_record["methodology"][
                "description"] += f"<p> <strong> Parent Prod ID:&nbsp;&nbsp;&nbsp;&nbsp; </strong> {str(parid)}"
            odp_record["methodology"][
                "description"] += f"<p> <strong> Parent Prod type: </strong> {str(partype)}"

    # Create a Table of TCKs
        tcktable = \
            """
    <p><strong>TCK &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Number of Files </strong>
    """
    for key, value in tckcount.items():

        tcktable += \
            f"""
     <p>{key} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {value}
     """

    # Save DDB and CondDB Tags
    odp_record["methodology"]["description"] += f"<p> <strong> Conditions: </strong>" + "<p>" + \
        str("<p>".join((prod_info["Value"]["Steps"][0][4],
            prod_info["Value"]["Steps"][0][5]))) + "</strong>"
    odp_record["methodology"][
        "description"] += f"<p> <strong> List of Trigger Configuration Keys (TCK): </strong> </p> <p>{tcktable}"

    # Get production steps config files
    request_id = tfClient.getTransformation(prod_summaries[0]["Production"])[
        "Value"]["TransformationFamily"]
    request = tfClient.getTransformations({"TransformationFamily": request_id})
    prod_ids = [prod["TransformationID"] for prod in request["Value"]]

    for prod_id in prod_ids:
        step_list = bkClient.getSteps(prod_id)["Value"]
        for name, app, ver, opts, dddb, conddb, extras, stepid, visible in step_list:

            # Define commands for Production Script
            odp_record["methodology"]["steps"] += [{
                "configuration_files": [{"title": str(path).strip("$APPCONFIGOPTS")[1:]} for path in opts.split(";")],
                "type": f"{name}".split("-DV-")[0],
                "release": " \n ".join([f"\n  {app}.{ver}", *extras.split(";")]),
            }]

    # Validate JSON
    if verbose:
        print("\n Filled in JSON file: ------------------------------------------------------------------------------------------------------------------------------------------------ \n")
        print(json.dumps(odp_record, indent=4, sort_keys=True))

    # Making a get request for json schema from the Open Data portal
    # Can't validate if Open Data portal is down!
    response = requests.get(
        'http://opendata.cern.ch/schema/records/record-v1.0.0.json')
    SchemaFile = response.json()

    # Validating the output json against the schema
    validate(odp_record, SchemaFile)
    print("\n Output json validated against the schema: SUCCESS \n")

    recordsdir = args.release_dir + "records/"

    # Check whether the specified path exists or not
    isExist = os.path.exists(recordsdir)

    if not isExist:

        # Create a new directory because it does not exist
        os.makedirs(recordsdir)

    # Write out a json file ---------------------------------------------------------------------------------------------------------------------------------
    with open(recordsdir + filename + ".json", "w") as f:
        f.write("[")    # Each JSON file must be a list
        json.dump(odp_record, f, indent=2, sort_keys=True)
        f.write("]")


# Let .py script run like a macro
if __name__ == "__main__":
    main()
