#!/usr/bin/env bash

# You should have access to the open data account to be able to do this...
export RUCIO_ACCOUNT=opendata

# Location of the skim datasets
VERSION=v0

echo "Working on umskimmed data from rucio"
# Check to see if the dataset itself has already been added
if [ -z "`rucio list-dids --short opendata.ODEO_FEB2025_noskim_Data_${VERSION}`" ] 
then
  rucio add-dataset opendata.ODEO_FEB2025_noskim_Data_${VERSION}
else
  echo "Seems like opendata.ODEO_FEB2025_noskim_Data_${VERSION} already exists"
fi

echo "Moving files over..."
for afile in `grep -e "data" unskimmed_data.txt`
do
  if [ -z "`rucio list-files opendata:opendata.ODEO_FEB2025_noskim_Data_${VERSION} 2>&1 | grep ${afile}`" ]
  then
    # Attach the new file to the dataset
    rucio attach opendata:opendata.ODEO_FEB2025_noskim_Data_${VERSION} ${afile}
  else
    echo "Seems like ${afile} has already been attached"
  fi
done

echo "Done uploading and attaching files. Final dataset:"
rucio list-files opendata.ODEO_FEB2025_noskim_Data_${VERSION}
echo "Transferring to its final resting place..."
if [ -z "`rucio list-rules opendata:opendata.ODEO_FEB2025_noskim_Data_${VERSION} | grep 'CERN-PROD_OPENDATA'`" ]
then
  rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates opendata:opendata.ODEO_FEB2025_noskim_Data_${VERSION} 1 CERN-PROD_OPENDATA
else
  echo "Seems that the rule already exists for opendata:opendata.ODEO_FEB2025_noskim_Data_${VERSION}"
fi


# Now go through the MC
echo "Working on umskimmed MC from rucio"
# Check to see if the dataset itself has already been added
if [ -z "`rucio list-dids --short opendata.ODEO_FEB2025_noskim_MC_${VERSION}`" ]     
then
  rucio add-dataset opendata.ODEO_FEB2025_noskim_MC_${VERSION}
else
  echo "Seems like opendata.ODEO_FEB2025_noskim_MC_${VERSION} already exists"
fi

echo "Moving files over..."
for afile in `grep -e "mc_" unskimmed_data.txt`
do
  if [ -z "`rucio list-files opendata:opendata.ODEO_FEB2025_noskim_MC_${VERSION} 2>&1 | grep ${afile}`" ]
  then
    # Attach the new file to the dataset
    rucio attach opendata:opendata.ODEO_FEB2025_noskim_MC_${VERSION} ${afile}
  else
    echo "Seems like ${afile} has already been attached"
  fi
done

echo "Done uploading and attaching files. Final dataset:"
rucio list-files opendata.ODEO_FEB2025_noskim_MC_${VERSION}
echo "Transferring to its final resting place..."
if [ -z "`rucio list-rules opendata:opendata.ODEO_FEB2025_noskim_MC_${VERSION} | grep 'CERN-PROD_OPENDATA'`" ]
then
  rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates opendata:opendata.ODEO_FEB2025_noskim_MC_${VERSION} 1 CERN-PROD_OPENDATA
else
  echo "Seems that the rule already exists for opendata:opendata.ODEO_FEB2025_noskim_MC_${VERSION}"
fi
