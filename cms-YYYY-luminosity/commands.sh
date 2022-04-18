#!/bin/bash -l
# parameters: 
#   $1 certified run json
#   $2 output style csv or tab
#   $3 summary or byls (if not byls, no option taken)
#   $4 run range first
#   $5 run range last
# exit on error
set -e

cert=$1
style=$2
if [ "$3" == "byls" ]; then mode="--"$3; fi;

if [  -z "$4" ]
then
  brilcalc lumi -c web $mode -i /mnt/vol/$cert -u /fb --normtag /mnt/vol/normtag_PHYSICS.json --output-style $style
elif [ -z "$5" ]
then
  echo "Give maximum range" 
else
  runmin=$4
  runmax=$5
  brilcalc lumi -c web $mode --begin $runmin --end $runmax -i /mnt/vol/$cert -u /fb --normtag /mnt/vol/normtag_PHYSICS.json  --output-style $style
fi
