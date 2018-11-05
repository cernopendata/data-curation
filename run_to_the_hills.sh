datasets="lists/CMS-2012-mc-released.txt"

# step 2
python code/interface.py --create-das-json-store $datasets > das-store.log 2>das-store.err