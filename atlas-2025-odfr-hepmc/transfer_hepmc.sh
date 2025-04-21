#!/usr/bin/env bash

# You should have access to the open data account to be able to do this
export RUCIO_ACCOUNT=opendata

# Loop over all the identified HEPMC datasets
for adid in `cat HEPMC_datasets.txt`
do
  echo "Working on HEPMC dataset ${adid}"
  # See if we already have a transfer rule. If we do, skip it. If not, add it
  if [ -z "`rucio list-rules ${adid} | grep 'CERN-PROD_OPENDATA'`" ]
  then
    rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for EO Open Data' --account opendata --skip-duplicates ${adid} 1 CERN-PROD_OPENDATA
  else
    echo "Seems that the rule already exists for ${adid}"
  fi

done # End of loop over HEPMC datasets
