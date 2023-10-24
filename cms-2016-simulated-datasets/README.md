# cms-2016-simulated-datasets

This directory contains helper scripts used to prepare CMS 2016 open data
release regarding MC simulated datasets.


- `code/` folder contains the python code.
- `inputs/` folder contains input text files with the list of datasets for each
  year and input files.

Every step necessary to produce the final `*.json` files is handled by the
`cmc-mc/interface.py` script. Details about it can be queried with the command:

```console
$ python3 code/interface.py --help
```

Make sure to start voms-proxy before creating cache 
```console
$ voms-proxy-init --voms cms --rfc --valid 190:00
```

Set the eos path with

```console
$ export EOS_MGM_URL=root://eospublic.cern.ch
```

Warning: creating the full local cache might take a long time!

First step is to create EOS file index cache:

```console
$ python3 ./code/interface.py --create-eos-indexes ../cms-YYYY-simulated-datasets/inputs/CMS-2016-mc-datasets.txt
```

This requires the file to be in place in their final location.

For early testing, on lxplus, all steps can be run without the EOS file index cache with the flag `--ignore-eos-store`.

To build sample records (with a limited number of datasets in the input file) do the following:


```console
$ python3 ./code/interface.py --create-das-json-store --ignore-eos-store DATASET_LIST

$ auth-get-sso-cookie -u  https://cms-pdmv.cern.ch/mcm -o cookies.txt
$ python3 ./code/interface.py --create-mcm-store --ignore-eos-store DATASET_LIST

$ openssl pkcs12 -in myCert.p12 -nocerts -nodes -out userkey.nodes.pem # if not present
$ python3 ./code/interface.py --get-conf-files --ignore-eos-store DATASET_LIST

$ python3 code/lhe_generators.py

$ python3 ./code/interface.py --create-records --ignore-eos-store DATASET_LIST
$ python3 ./code/interface.py --create-conffiles-records --ignore-eos-store DATASET_LIST
```

Note that to build the test records an (empty) input file for DOI's and a recid info file must be present in the inputs directory.
Each step builds a subdirectory with a cache (`das-json-store`, `mcm-store` and `config-store`). They are large, do not upload them to the repository.

The output json file for dataset records go to the `outputs` directory.


## lhe_generators


```console
python3 code/lhe_generators.py 2> errors > output &
```
- This will get lhe generator parameters from gridpacks for datasets listed in `./inputs/CMS-2016-mc-datasets.txt`
- It works on lxplus or with mounted EOS
- number of threads is set to 20 which is ideal for lxplus

> :warning:  There are many cases with various steps to get generator parameters for LHE -see [#97](https://github.com/cernopendata/data-curation/issues/97)-. Thus, in some few cases, the script MIGHT not work as expected so make sure to read it, check errors, and make any necessary tweaks 
