#!/bin/bash -l
# Output prescales for all runs in /mnt/vol/run_numbers.txt
# exit on error
set -e

echo "# run,cmsls,prescidx"
while read -r r; do brilcalc trg -c web --prescale -r "$r" --output-style csv | grep -v "#"; done < /mnt/vol/run_numbers.txt


