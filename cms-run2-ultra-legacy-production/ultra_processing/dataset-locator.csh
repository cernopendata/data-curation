#!/bin/tcsh

set inputds=$1


#voms-proxy-init -voms cms

foreach i (`cat $inputds`)
 echo Working on $i
 set firstfilesites=`dasgoclient -query "site dataset=$i" | grep -E '.*(T2|Disk).*'|head -1 `
 #echo print $firstfilesites
 if ($firstfilesites == "") then
   echo  ===== Datase $i is not on disk!
 else
   set afile = `dasgoclient --query "file dataset=$i site=$firstfilesites" |head -1`
   echo File $afile is on $firstfilesites
 endif

