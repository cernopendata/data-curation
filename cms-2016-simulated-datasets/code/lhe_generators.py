#!/usr/bin/env python3

import datetime
import fnmatch
import os
import re
import requests
import subprocess
import urllib3

from dataset_records import *
from mcm_store import get_mcm_dict
from utils import get_from_deep_json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RECID_INFO = {}
exec(open("inputs/recid_info.py", "r").read())  # import RECID_INFO


def log(recid, logtype, logmessage):
    """Store a log message of a certain type to record-ID-based log file system."""
    logdir = f'./lhe_generators/2016-sim/gridpacks/{recid}'
    
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    with open(f"{logdir}/LOG.txt", "a") as fdesc:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fdesc.write(f"{now} | {logtype} | {logmessage}\n")


def get_lhe(dataset, mcm_dir):
    """Get LHE Parent or False"""
    path = mcm_dir + "/chain/" + dataset.replace("/", "@")
    try:
        step_dirs = os.listdir(path)
    except:
        return False
    for step in step_dirs:
        step_dir = path + "/" + step
        datatier = get_from_deep_json(get_mcm_dict(dataset, step_dir), "datatier")
        if datatier and "LHE" in datatier:
            return step_dir
    return False


def cmd_run(cmds, recid):

    for cmd in cmds:
        err = subprocess.run(
            cmd,
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        ).stderr.decode()
        
        if err:
            log(recid, "ERROR", f"Error {err}")
            return False

    return True

    
def create_lhe_generator(
    dataset, recid, mcm_dir, gen_store="./lhe_generators/2016-sim"
):
    '''
    mcm_dir is the directory of the LHE step
    '''
    mcdb_id = get_from_deep_json(get_mcm_dict(dataset, mcm_dir), "mcdb_id") or 0
    
    if mcdb_id > 1:

        parent_dir = f'{gen_store}/mcdb'
        
        '''
        Make dir if it doesn't already exist
        '''
        if not os.path.isdir(parent_dir):
            os.makedirs(parent_dir)

        filepath = f'{gen_store}/mcdb/{mcdb_id}'

        '''
        If the header file already exists and is not empty
        we are already done so return.
        '''
        if os.path.exists(filepath + "_header.txt") and get_file_size(f'{filepath}_header.txt') > 1024:
            print(
                f'{mcdb_id} mcdb id exists, skipping'
            )
            return
    
        #We only want .xz or .lhe extensions.
        files = [
            f for f in os.listdir(f'/eos/cms/store/lhe/{mcdb_id}') if os.path.isfile(os.path.join(f'/eos/cms/store/lhe/{mcdb_id}', f)) and
            (os.path.splitext(f)[1] == '.xz' or os.path.splitext(f)[1] == '.lhe') 
        ]
        
        
        #If we have no files then return.
        if len(files) == 0:
            print(
                f'<exterr>\n {mcdb_id}: no files found with .xz or .lhe extension\n </exterr>',
                file=sys.stderr
            )
            return

        #If there are multiple files with either .xz or .lhe
        #extensions then take the first one anyway.

        #TODO: If multiple files then use _0? Is it certain that it exists?
        #See https://github.com/cernopendata/data-curation/issues/97
        (_, ext) = os.path.splitext(files[0])

        generators = get_from_deep_json(
            get_mcm_dict(dataset, mcm_dir), "generators") or 0

        cmds = [
            f"xz -d -c /eos/cms/store/lhe/{mcdb_id}/* > {filepath} " if ext == '.xz'
            else f"cp /eos/cms/store/lhe/{mcdb_id}/*  {filepath} ",
            f"awk '/<!--/,/-->/' {filepath} > {filepath}_header.txt" if generators == ["MCFM701"]
            else f"awk '/<header>/,/<\/header>/' {filepath} > {filepath}_header.txt"
        ]
        
        if cmd_run(cmds, dataset):
            size = get_file_size(f'{filepath}_header.txt')

            if size <= 1024:
                
                #If empty, take comments (assume it is a MCFM701)
                cmd_run(
                    [
                        f"awk '/<!--/,/-->/' {filepath} > {filepath}_header.txt; \
                           awk '/<init>/,/<\/init>/' {filepath} >> {filepath}_header.txt;"
                    ],
                    dataset
                )
                
                size = get_file_size(
                    f'{filepath}_header.txt'
                )

                if size <= 1024:
                    print(
                        f'<size>\n[Warning] in {dataset}\n mcdb_id: {mcdb_id} \n==>\t Header file size is only {size} Bytes\n</size>',
                        file=sys.stderr
                    )

            #If we got the _header.txt file then, there is no need to keep original files
            cmd_run(
                [
                    f'rm -rf {filepath}'
                ],
                dataset
            )    
            
    # Find fragment
    fragment = get_from_deep_json(get_mcm_dict(dataset, mcm_dir), "fragment")
    if not fragment:
        log(
            recid,
            "ERROR",
            f"No fragment URL and Empty fragment in mcm dict; skipping.",
        )
        return

    # Find gridpack path
    # path = re.search(r"cms.vstring\(['\"\[]\s*(/cvmfs.*?)['\"]", fragment)
    path = re.search(r"(/cvmfs/cms.cern.ch/phys_generator/gridpacks[^']*)", fragment)
    if not path:
        log(
            recid,
            "ERROR",
            f"No '/cvmfs/cms.cern.ch/phys_generator/gridpacks' found in fragment; skipping.",
        )
        return

    path = path.groups()[0]
    log(recid, "INFO", f"Found path {path}")
    outfilepath = "{gen_store}/gridpacks/{recid}".format(
        gen_store=gen_store, recid=recid
    )
    if os.path.exists(outfilepath) and len(os.listdir(outfilepath)) > 1:
        log(
            recid,
            "WARNING",
            f"Gridpack seems to exist for this record ID already. Skipping.",
        )
        return

    # Identify gridpack case
    gridpack_case = "UNKNOWN"
    path_lower = path.lower()
    path_lower_position = {}
    for acase in ["amcatnlo", "madgraph", "powheg", "jhugen", "phantom", "mcfm"]:
        path_lower_position[acase] = path_lower.find(acase)
    found = 1e10
    for key, val in path_lower_position.items():
        if val > 0 and val < found:
            gridpack_case = key
    if gridpack_case == "UNKNOWN":
        log(recid, "ERROR", f"Found case {gridpack_case}")
    else:
        log(recid, "INFO", f"Found case {gridpack_case}")

    # List content if all files in gridpack tarball
    files_all = []
    res = subprocess.check_output(f"tar tf {path}", shell=True)
    for line in res.splitlines():
        files_all.append(line.decode())

    # Select interesting files based on gridpack case
    files = [
        "./InputCards/*.dat",
        "./runcmsgrid.sh",
        "InputCards/*.dat",
        "runcmsgrid.sh",
    ]
    if gridpack_case == "amcatnlo":
        files.extend(
            [
                "./process/Cards/param_card.dat",
                "./process/Cards/proc_card*.dat",
                "./process/Cards/run_card.dat",
                "process/Cards/param_card.dat",
                "process/Cards/proc_card*.dat",
                "process/Cards/run_card.dat",
            ]
        )
    elif gridpack_case == "madgraph":
        files.extend(
            [
                "./process/madevent/Cards/param_card.dat",
                "./process/madevent/Cards/proc_card*.dat",
                "./process/madevent/Cards/run_card.dat",
                "process/madevent/Cards/param_card.dat",
                "process/madevent/Cards/proc_card*.dat",
                "process/madevent/Cards/run_card.dat",
            ]
        )
    elif gridpack_case == "powheg":
        files.extend(
            [
                "*.input",
            ]
        )
    elif gridpack_case == "jhugen":
        files.extend(
            [
                "./jhugen.input",
                "./JHUGen.input",
                "./jhugen_decay.input",
                "./JHUGen_decay.input",
                "./*_JHUGen/JHUGen.input",
                "./*_JHUGen/JHUGen_decay.input",
                "jhugen.input",
                "JHUGen.input",
                "jhugen_decay.input",
                "JHUGen_decay.input",
                "*_JHUGen/JHUGen.input",
                "*_JHUGen/JHUGen_decay.input",
            ]
        )
    elif gridpack_case == "phantom":
        files.extend(
            [
                "./r_GEN.in",
                "r_GEN.in",
            ]
        )
    elif gridpack_case == "mcfm":
        files.extend(
            [
                "./readInput.DAT",
                "readInput.DAT",
                "./JHUGen.input",
                "JHUGen.input",
            ]
        )

    # Select only those files that are present
    files_selected = []
    for afile in files:
        files_selected.extend(fnmatch.filter(files_all, afile))

    # Warn if there was no runcmsgrid or InputCards found for some cases
    if gridpack_case in ("amcatnlo", "madgraph"):
        if not "InputCards" in " ".join(files_selected):
            log(recid, "ERROR", f"InputCards not present in the tarball.")
        if not "runcmsgrid.sh" in " ".join(files_selected):
            log(recid, "ERROR", f"runcmsgrid.sh not present in the tarball.")

    # Warn if no interesting files were found at all
    if len(files_selected) == 0:
        log(recid, "ERROR", "Found no interesting files at all.")
    else:
        # Inform about which files are going to be extracted
        log(
            recid,
            "INFO",
            f"Found the following interesting files: {' '.join(files_selected)}",
        )
        # Prepare the tarball extraction command
        cmds = [
            f"mkdir -p {outfilepath}; cd {outfilepath}; tar -xf {path} {' '.join(files_selected)} -C {outfilepath}"
        ]
        log(recid, "INFO", f"Executing commands {cmds}")
        # Run the tarball extraction command
        cmd_run(cmds, recid)

    # Print full content of gridpack tarball for debugging purposes
    log(recid, "DEBUG", f"Full gridpack tarball content is:")
    for afile in files_all:
        log(recid, "DEBUG", f"- {afile}")


das_dir = "./inputs/das-json-store"
mcm_dir = "./inputs/mcm-store"
with open("./inputs/CMS-2016-mc-datasets.txt", "r") as file:
    dataset_full_names = file.readlines()

dataset_nanoaod = [
    name[:-1] for name in dataset_full_names if name[:-1].endswith("NANOAODSIM")
]

i = 1
l = len(dataset_nanoaod)

for dataset in dataset_nanoaod:
    recid = RECID_INFO[dataset]

    #print(f"Getting LHE {i}/{l}")
    log(recid, "INFO", f"Getting LHE {i}/{l}")
    log(recid, "INFO", f"Found record ID {recid}")
    log(recid, "INFO", f"Found dataset {dataset}")

    lhe_dir = get_lhe(dataset, mcm_dir)
    if not lhe_dir:
        log(recid, "WARNING", f"There is no LHE directory. Skipping.")
        continue

    log(recid, "INFO", f"Found LHE directory {lhe_dir}")

    t = threading.Thread(target=create_lhe_generator, args=(dataset, recid, lhe_dir))
    t.start()
    i += 1
    while threading.activeCount() >= 20:
        sleep(0.5)  # run 20 parallel
