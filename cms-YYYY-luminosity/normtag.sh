#!/bin/bash -l
# parameters: 
# 

# exit on error
set -e

cert=$(cat cert.txt)
runmin=$(echo "$cert" | jq -c -r '. | keys[]' | head -1)
runmax=$(echo "$cert" | jq -c -r '. | keys[]' | tail -1)

tags=$(cat normtag_PHYSICS.json)

echo "["
for row in $(echo "${tags}" | jq -c '.[]'); do
   run=$(echo "${row}" | jq -c -r '.[1] | keys[]')
   if [ "$run" -ge "$runmin" ] && [ "$run" -lt "$runmax" ]
   then
     myrow=$(echo "${row}" | jq -c -r) 
     echo "$myrow"","
   elif [ "$run" -eq "$runmax" ]
   then
     echo "${row}" | jq -c -r
   elif [ "$run" -gt "$runmax" ]
   then
     break
   fi
done
echo "]"