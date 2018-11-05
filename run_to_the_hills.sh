datasets="lists/10.txt"
datasets="lists/CMS-2012-mc-released.txt"
datasets="lists/CMS-2012-mc-datasets.txt"

# step 1
export EOS_MGM_URL=root://eospublic.cern.ch
python code/interface.py --create-eos-indexes $datasets 2>eos-indexes.err

# step 2
# you should have voms-proxy here!
# voms-proxy-init -voms cms -rfc
python code/interface.py --create-das-json-store --ignore-eos-store $datasets 2>das-store.err

# step 3
python code/interface.py --create-mcm-store --ignore-eos-store $datasets 2>mcm-store.err

# step 4
python code/interface.py --get-conf-files --ignore-eos-store $datasets 2>confs.err
