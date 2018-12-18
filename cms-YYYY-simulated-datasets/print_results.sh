#!/bin/bash

# Run categorisation script for all dataset lists in inputs/ and generate a
# nice looking html page :)
# run make_local_cache.sh first!


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


today="$(date +"%Y-%m-%d")-results"
now=$(date)
if [ ! -d $today ];
then
	mkdir $today
fi


summary="$today/summary.md"
index="$today/index.html"
echo "# Categorisation Rich Results" > $summary
echo "" >> $summary
echo "Page generated on $now" >> $summary
echo "" >> $summary

years=(2010 2011 2012 2015 2016)
for year in ${years[*]}
do
	list="inputs/CMS-"$year"-mc-datasets.txt"
	doi="./inputs/doi-cms-mc-2012-released.txt"
	recid="./inputs/recid-cms-mc-2012-datasets.py"

	echo "Categorising $list"
	listname=$(basename $list .txt)
	md="$today/$listname.md"
	html="$today/$listname.html"

	python code/interface.py --print-results \
	                           --eos-dir  ./cache/$year/eos-file-indexes/ \
	                           --das-dir  ./cache/$year/das-json-store/ \
	                           --mcm-dir  ./cache/$year/mcm-store/ \
	                           --conf-dir ./cache/$year/config-store/ \
	                           --doi-file $doi \
	                           --recid-file $recid \
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
