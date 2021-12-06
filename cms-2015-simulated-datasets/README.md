# cms-2015-simulated-datasets

This directory contains helper scripts used to prepare CMS 2015 open data
release regarding MC simulated datasets.


- `code/` folder contains the python code.
- `inputs/` folder contains input text files with the list of datasets for each
  year and input files.

Every step necessary to produce the final `*.json` files is handled by the
`cmc-mc/interface.py` script. Details about it can be queried with the command:

```console
python code/interface.py --help
```

Make sure to start voms-proxy before creating cache 
```console
voms-proxy-init --voms cms --rfc --valid 190:00
```
Warning: creating a local cache might take a long time!

Here is how to run the record creation.

First, create EOS file index cache:

```console
$ python3 ./code/interface.py --create-eos-indexes ../cms-YYYY-simulated-datasets/inputs/CMS-2015-mc-datasets.txt
```
