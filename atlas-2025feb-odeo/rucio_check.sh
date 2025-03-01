#!/usr/bin/env bash

# Location of the skim datasets
SKIM_LOCATION=/eos/user/e/egramsta/OpenData/FEB2025/

# Automatic version - check all the skims in the area
for askim in `ls /eos/user/e/egramsta/OpenData/FEB2025`
do
  echo "Working on skim ${askim} from area ${SKIM_LOCATION}"
  # Go over all the directories in there - basically just data and MC
  for datamc in `ls ${SKIM_LOCATION}/${askim}`
  do
    echo "Working on sub-directory ${datamc}"
    # Compare the list of files in rucio to the list of files on disk to check for missing files or failures
    rucio list-files opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_v0 | grep "opendata" | gawk '{print $2}' | sed "s/opendata:ODEO_FEB2025_v0_${askim}_//g" | sort > rucio_list.txt
    ls -1 ${SKIM_LOCATION}/${askim}/${datamc} | sort > disk_list.txt
    diff rucio_list.txt disk_list.txt
    # Now check for replication to CERN open data endpoint
    rucio list-files opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_v0 | grep "Total files"
    rucio list-dataset-replicas opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_v0 | grep "CERN-PROD_OPENDATA"
  done
done
# Clean up our temporary files
rm rucio_list.txt disk_list.txt

# Now do the comparison for the unskimmed data
echo "Unskimmed data: " `grep "data" unskimmed_data.txt | wc -l`
rucio list-files opendata:opendata.ODEO_FEB2025_noskim_Data_v0 | grep "Total files"
rucio list-dataset-replicas opendata:opendata.ODEO_FEB2025_noskim_Data_v0 | grep "CERN-PROD_OPENDATA"

# And the unskimmed MC
echo "Unskimmed MC: " `grep "mc_" unskimmed_data.txt | wc -l`
rucio list-files opendata:opendata.ODEO_FEB2025_noskim_MC_v0 | grep "Total files"
rucio list-dataset-replicas opendata:opendata.ODEO_FEB2025_noskim_MC_v0 | grep "CERN-PROD_OPENDATA"
