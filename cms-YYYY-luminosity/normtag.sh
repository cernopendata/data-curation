#!/bin/bash -l
# parameters: 
# 

# exit on error
set -e

cert=$(cat cert.txt)
runmin=$(echo "$cert" | jq -c -r '. | keys[]' | head -1)
runmax=$(echo "$cert" | jq -c -r '. | keys[]' | tail -1)

tags=$(cat normtag_PHYSICS.json)

arr=()
echo "["
for row in $(echo "${tags}" | jq -c '.[]'); do
   run=$(echo "${row}" | jq -c -r '.[1] | keys[]')
   if [ "$run" -ge "$runmin" ] && [ "$run" -le "$runmax" ]
   then
     myrow=$(echo "${row}" | jq -c -r) 
     arr+=("$myrow"",")
   elif [ "$run" -gt "$runmax" ]
   then
     break
   fi
done

# remove the comma after the last element
arr[-1]=${arr[-1]%?}

for i in "${arr[@]}"
do
   echo "$i"
done

echo "]"