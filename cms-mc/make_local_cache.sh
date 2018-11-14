# this script makes a local cache of a list of CMS MC datasets

datasets="lists/CMS-2016-mc-datasets.txt"
datasets="lists/CMS-2015-mc-datasets.txt"
datasets="lists/CMS-2012-mc-datasets.txt"
datasets="lists/CMS-2011-mc-datasets.txt"
datasets="lists/CMS-2012-mc-released.txt"
datasets="lists/CMS-2010-mc-datasets.txt"

doi="./inputs/doi-cms-mc-2012-released.txt"
recid="./inputs/recid-cms-mc-2012-datasets.py"


echo "dataset:   " $datasets
echo "DOI:       " $doi
echo "Record ID: " $recid
echo -e "\n\n"


# step 1
export EOS_MGM_URL=root://eospublic.cern.ch
python cms-mc/interface.py --create-eos-indexes $datasets 2>eos-indexes.err

# step 2
# you should have voms-proxy here!
# voms-proxy-init --voms cms --rfc --valid 190:00
python cms-mc/interface.py --create-das-json-store --ignore-eos-store $datasets 2>das-store.err

# step 3
python cms-mc/interface.py --create-mcm-store --ignore-eos-store $datasets 2>mcm-store.err

# step 4
python cms-mc/interface.py --get-conf-files --ignore-eos-store $datasets 2>confs.err