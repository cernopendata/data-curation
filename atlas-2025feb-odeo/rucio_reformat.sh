#!/usr/bin/env bash

# You should have access to the open data account to be able to do this...
export RUCIO_ACCOUNT=opendata

# Location of the skim datasets
SKIM_LOCATION=/eos/user/e/egramsta/OpenData/FEB2025/
VERSION=v0

# Automatic version - grab all the skims
for askim in `ls /eos/user/e/egramsta/OpenData/FEB2025`
do
  echo "Working on skim ${askim} from area ${SKIM_LOCATION}"
  # Go over all the directories in there - basically just data and MC
  for datamc in `ls ${SKIM_LOCATION}/${askim}`
  do
    echo "Working on sub-directory ${datamc} - creating a dataset first"
    # Create the dataset in rucio. It is an empty dataset at this stage

    if [ -z "`rucio list-dids --short opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION}`" ]
    then
      rucio add-dataset opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION}
    else
      echo "Seems like opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION} already exists"
    fi

    # Go over all the files in our directory
    echo "Uploading files..."
    for afile in `ls ${SKIM_LOCATION}/${askim}/${datamc}`
    do
      # Note that 'data' or 'mc' is already a part of the file name
      # Upload the file via rucio to the a scratch disk endpoint. Set the name in rucio to something unique
      # Slightly awkward juggling because the open data endpoint isn't accessible to this operation, so we
      # have to transfer it to a scratchdisk endpoint and then move it over afterwards with a rule.
      if [ -z "`rucio list-files opendata:ODEO_FEB2025_${VERSION}_${askim}_${afile} 2>&1 | grep '| open'`" ]
      then
        rucio upload --scope opendata --register-after-upload --rse CERN-PROD_SCRATCHDISK --name ODEO_FEB2025_${VERSION}_${askim}_${afile} ${SKIM_LOCATION}/${askim}/${datamc}/${afile}
        # Attach the new file to the dataset
        rucio attach opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION} opendata:ODEO_FEB2025_${VERSION}_${askim}_${afile}
      else
        echo "Seems like opendata:ODEO_FEB2025_${VERSION}_${askim}_${afile} already exists"
      fi
    done # End of loop over files
    echo "Done uploading and attaching files. Final dataset:"
    rucio list-files opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION}
    echo "Transferring to its final resting place..."

    if [ -z "`rucio list-rules opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION} | grep 'CERN-PROD_OPENDATA'`" ]
    then
      rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION} 1 CERN-PROD_OPENDATA
    else
      echo "Seems that the rule already exists for opendata:opendata.ODEO_FEB2025_${askim}_${datamc}_${VERSION}"
    fi
  done # End of loop over directories
done # End of loop over skims
