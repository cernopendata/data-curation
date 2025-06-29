#!/usr/bin/env bash

# You should have access to the open data account to be able to do this...
export RUCIO_ACCOUNT=opendata

# Location of the skim datasets
SKIM_LOCATION=/eos/user/e/egramsta/OpenData/FEB2025/
VERSION=v1

# First deal with the updated b-jet skims
echo "Working on updated b-jet skims"
for datamc in data mc
do
  # Create the dataset in rucio. It is an empty dataset at this stage
  if [ -z "`rucio list-dids --short opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION}`" ]
    then
      rucio add-dataset opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION}
    else
      echo "Seems like opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION} already exists"
    fi
    # Now we need to attach the files, and then we can move it with a rule
    for afile in `grep $datamc updated_bjet_skims.txt`
    do
      if [ -z "`rucio list-files opendata:opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION} 2>&1 | grep ${afile}`" ]
      then
        rucio attach opendata:opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION} ${afile}
      else
        echo "Looks like ${afile} is already in the dataset"
      fi
    done # End of loop over files
    echo "Done uploading and attaching files. Final dataset:"
    rucio list-files opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION}
    echo "Transferring to its final resting place..."

    if [ -z "`rucio list-rules opendata:opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION} | grep 'CERN-PROD_OPENDATA'`" ]
    then
      rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates opendata:opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION} 1 CERN-PROD_OPENDATA
    else
      echo "Seems that the rule already exists for opendata:opendata.ODEO_FEB2025_2bjets_${datamc}_${VERSION}"
    fi
done # End of loop over data / MC

# Now deal with the jet data
echo "Working on the QCD skims"
for datamc in data mc
do
  # Create the dataset in rucio. It is an empty dataset at this stage
  if [ -z "`rucio list-dids --short opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION}`" ]
    then
      rucio add-dataset opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION}
    else
      echo "Seems like opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION} already exists"
    fi
    # Now we need to attach the files, and then we can move it with a rule
    for afile in `grep $datamc qcd_skims.txt`
    do
      if [ -z "`rucio list-files opendata:opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION} 2>&1 | grep ${afile}`" ]
      then
        rucio attach opendata:opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION} ${afile}
      else
        echo "Looks like ${afile} is already in the dataset"
      fi
    done # End of loop over files
    echo "Done uploading and attaching files. Final dataset:"
    rucio list-files opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION}
    echo "Transferring to its final resting place..."

    if [ -z "`rucio list-rules opendata:opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION} | grep 'CERN-PROD_OPENDATA'`" ]
    then
      rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates opendata:opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION} 1 CERN-PROD_OPENDATA
    else
      echo "Seems that the rule already exists for opendata:opendata.ODEO_FEB2025_qcdjet_${datamc}_${VERSION}"
    fi
done # End of loop over data / MC
