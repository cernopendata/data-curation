#!/usr/bin/env python

import subprocess
import os


def get_root_file_names(dataset_name):
  # Get all the disk names and filter out by picking the first one in the list
  cmd_dataset_site = ['dasgoclient -query "site dataset=' + dataset_name + '" | grep -E \'.*(T2|Disk).*\'|head -1']

  ## call date command ##
  p = subprocess.Popen(cmd_dataset_site, stdout=subprocess.PIPE, shell=True)
 
  ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
  ## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
  ## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
  ## or None, if no data should be sent to the child.
  (output, err) = p.communicate()
 
  ## Wait for date to terminate. Get return returncode ##
  p_status = p.wait()
  print "Command output : ", output
  print "Command exit status/return code : ", p_status

  if (p_status == 0 and len(output) >= 1):
    cmd_dataset_path =  ['dasgoclient --query "file dataset=' + dataset_name + ' site=' + output.strip() + '" |head -1']
    print cmd_dataset_path
    p = subprocess.Popen(cmd_dataset_path, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print "Command output : ", output
    print "Command exit status/return code : ", p_status
    return output
  else:
    print("We couldn't find files on the disk! No prov and lhc header dumped...")
    return None
  

def dump_provenance_lhc(dataset_names):
  locations = []
  cmd_dump_prov = "edmProvDump"
  for name in dataset_names:
    location = get_root_file_names(name)
    if location is not None:
      print(location)
      locations.append(location)

  for location in locations:
    f_cmd_address = "cmsenv && " + cmd_dump_prov + " root://cms-xrd-global.cern.ch/" + location
    # f_cmd_address = "pwd"
    print(f_cmd_address)
    # edmProvDump root://cms-xrd-global.cern.ch//store/mc/PhaseIIMTDTDRAutumn18GS/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM/103X_upgrade2023_realistic_v2-v1/80000/B58CD7D3-E622-AB43-A613-25AB9AD01153.root
    cwd = os.path.dirname(os.path.realpath(__file__)) 
    p = subprocess.Popen(f_cmd_address, stdout=subprocess.PIPE, shell=True, cwd=cwd)
    (output, err) = p.communicate()
    p_status = p.wait()
  
    with open("file.dat","a+") as f:
      f.write(output)

  

dump_provenance_lhc(["/MinBias_TuneCP5_14TeV-pythia8/PhaseIIMTDTDRAutumn18GS-103X_upgrade2023_realistic_v2-v1/GEN-SIM", "/RSGluonToTT_M-3000_Tune4C_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM"])



