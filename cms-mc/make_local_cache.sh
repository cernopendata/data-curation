# this script makes a local cache of a list of CMS MC datasets

year=2010
datasets="lists/CMS-"$year"-mc-datasets.txt"


# step 1
export EOS_MGM_URL=root://eospublic.cern.ch
python cms-mc/interface.py --create-eos-indexes \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           $datasets 2>eos-indexes.err || exit $?

# step 2
# you should have voms-proxy here!
# voms-proxy-init --voms cms --rfc --valid 190:00
python cms-mc/interface.py --create-das-json-store \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           $datasets 2>das-store.err || exit $?

# step 3
python cms-mc/interface.py --create-mcm-store \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           --mcm-dir ./cache/$year/mcm-store/ \
                           $datasets 2>mcm-store.err || exit $?

# step 4
python cms-mc/interface.py --get-conf-files \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           --mcm-dir ./cache/$year/mcm-store/ \
                           --conf-dir ./cache/$year/config-store/ \
                           $datasets 2>conffiles.err || exit $?