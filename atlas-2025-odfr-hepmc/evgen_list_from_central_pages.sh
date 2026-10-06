#!/usr/bin/bash

#lsetup centralpage

# For problematic datasets
rm EVNT_to_report.txt

# All baseline, centrally recommended systematic variations, alternative, and specialised samples
for atype in Baseline Systematic Alternative Specialised
do
  # Remove the file if it already exists
  rm EVNT_list_${atype}.txt
  # Add the 13 TeV and 13.6 TeV samples to it
  centralpage --scope=mc23_13p6TeV --single_level=3 ${atype} >> EVNT_list_${atype}.txt
  centralpage --scope=mc20_13TeV --single_level=3 ${atype} >> EVNT_list_${atype}.txt
  # Grab problematic datasets and put them where they belong
  grep -e "_LHE" EVNT_list_${atype}.txt >> EVNT_to_report.txt
  # Remove the problematic ones, sort, remove duplicates, and move into place
  sort EVNT_list_${atype}.txt | grep -ve "_LHE" | uniq > final_EVNT_list_${atype}.txt
  mv final_EVNT_list_${atype}.txt EVNT_list_${atype}.txt
done
