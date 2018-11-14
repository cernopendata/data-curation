datasets="lists/CMS-2010-mc-datasets.txt"
datasets="lists/CMS-2012-mc-released.txt"
datasets="lists/CMS-2012-mc-datasets.txt"

doi="./inputs/doi-cms-mc-2012-released.txt"
recid="./inputs/recid-cms-mc-2012-datasets.py"


echo "dataset:   " $datasets
echo "DOI:       " $doi
echo "Record ID: " $recid
echo -e "\n\n"


python cms-mc/interface.py --print-results --ignore-eos-store --recid-file $recid --doi-file $doi $datasets > bla

markdown -o html4 -x tables bla > bla.html
echo mv bla.html ~/www/tmp/$(basename $datasets .txt).html
mv bla.html ~/www/tmp/$(basename $dataset .txt).html