#!/bin/bash

# Run categorisation script for all dataset lists in inputs/ and generate a
# nice looking html page :)
# there is no need to have a local cache for this script

function my_markdown()
{
	dir="../markdownpy-spytoc-template/"
	if [ -d $dir ]
	then
		python $dir/spytoc.py $1
	elif which markdown_py &> /dev/null
	then
		markdown_py -x tables $1
	else
		python -m markdown -x tables -o html $1
	fi
}


today="$(date +"%Y-%m-%d")-categorisation"
now=$(date)
if [ ! -d $today ];
then
	mkdir $today
fi


summary="$today/summary.md"
index="$today/index.html"
echo "# Categorisation Results" > $summary
echo "" >> $summary
echo "Page generated on $now" >> $summary
echo "" >> $summary

years=(2010 2011 2012 2015 2016)
for year in ${years[*]}
do
	list="inputs/CMS-"$year"-mc-datasets.txt"

	listname=$(basename $list .txt)
	md="$today/$listname.md"
	html="$today/$listname.html"

	echo "Categorising $list"

	python code/interface.py --print-categorisation \
	                           --eos-dir  ./cache/$year/eos-file-indexes/ \
	                           --das-dir  ./cache/$year/das-json-store/ \
	                           --mcm-dir  ./cache/$year/mcm-store/ \
	                           --conf-dir ./cache/$year/config-store/ \
	                           $list > $md || exit $?
	my_markdown $md > $html

	echo "## $listname" >> $summary
	head $md -n 41 | tail -n 32 >> $summary
	echo "" >> $summary
	echo "**Details** [here]($listname.html)" >> $summary
	echo "" >> $summary
done

echo "Making $index"
my_markdown $summary > $index
