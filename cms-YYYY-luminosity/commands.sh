#!/bin/bash -l
# parameters: 
#   $1 certified run json
#   $2 output style csv or tab
#   $3 use normtag file or pxl
#   $4 summary or byls (if not byls, no option taken)
#   $5 run range first
#   $6 run range last
# exit on error
set -e

cert=$1
style=$2

#echo "# cert file:"
#cat /mnt/vol/$cert
if [ "$3" == "normtag" ]
then 
  option="--normtag /mnt/vol/normtag_PHYSICS.json"
  #echo "# normtag file:"
  #cat /mnt/vol/normtag_PHYSICS.json
else
  option="--type $3"
fi
#echo "#from commands: value of options is $option, value of input is $3" 

if [ "$4" == "byls" ]; then mode="--"$4; fi;

if [  -z "$5" ]
then
  echo "#Brilcalc command:  brilcalc lumi -c web $mode -i /mnt/vol/$cert -u /fb $option --output-style $style"
  brilcalc lumi -c web $mode -i /mnt/vol/$cert -u /fb $option --output-style $style
elif [ -z "$6" ]
then
  echo "Give maximum range" 
else
  runmin=$5
  runmax=$6
  echo "#Brilcalc command:  brilcalc lumi -c web $mode --begin $runmin --end $runmax -i /mnt/vol/$cert -u /fb $option  --output-style $style"
  brilcalc lumi -c web $mode --begin $runmin --end $runmax -i /mnt/vol/$cert -u /fb $option  --output-style $style
fi
