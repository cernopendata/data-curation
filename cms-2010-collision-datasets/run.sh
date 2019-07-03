#!/usr/bin/env zsh

# Create EOS file indexes for Run2010A datasets:
# (we can reuse 2012 code)
 
#(cd inputs; ln -sf ./cms-Run2010A-collision-datasets.txt ./cms-2012-collision-datasets.txt)
#python ../cms-2012-collision-datasets/code/create_eos_file_indexes.py
#rm -f ./inputs/cms-2012-collision-datasets.txt

(cd inputs; ln -sf ./cms-Commissioning10-collision-datasets.txt ./cms-2012-collision-datasets.txt)
python ../cms-2012-collision-datasets/code/create_eos_file_indexes.py
rm -f ./inputs/cms-2012-collision-datasets.txt
