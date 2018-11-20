#!/bin/bash

# Run categorisation script for all dataset lists in lists/ and generate a
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

for list in lists/*.txt;
do
	echo "Categorising $list"
	listname=$(basename $list .txt)
	md="$today/$listname.md"
	html="$today/$listname.html"

	python cms-mc/interface.py --print-categorisation $list > $md || exit $?
	my_markdown $md > $html

	echo "## $listname" >> $summary
	head $md -n 41 | tail -n 32 >> $summary
	echo "" >> $summary
	echo "**Details** [here]($listname.html)" >> $summary
	echo "" >> $summary
done

echo "Making $index"
my_markdown $summary > $index