# cms-2016-pileup-dataset

This directory contains helper scripts used to prepare CMS 2016 open data
release regarding pile-up dataset.

- `code/` folder contains the python code;
- `inputs/` folder contains input text files with the list of datasets for each
  year and input files;
- `outputs/` folder contains generated JSON records to be included as the CERN
  Open Data portal fixtures.

Every step necessary to produce the final `*.json` files is handled by the
`code/interface.py` script. Details about it can be queried with the command:

```console
$ python3 code/interface.py --help
```

Please make sure to get the VOMS proxy file before running these scripts:

```console
$ voms-proxy-init --voms cms --rfc --valid 190:00
```

Please make sure to set the EOS instance to EOSPUBLIC before running these scripts:

```console
$ export EOS_MGM_URL=root://eospublic.cern.ch
```
Please make sure to have a valid `userkey.nodes.pem` certificate present in
`$HOME/.globus`. If not, you have to run the following on top of the regular
CMS certificate documentation:

```console
$ cd $HOME/.globus
$ ls userkey.nodes.pem
$ openssl pkcs12 -in myCert.p12 -nocerts -nodes -out userkey.nodes.pem  # if not present
$ cd -
```

First step is to create EOS file index cache:

```console
$ python3 ./code/interface.py --create-eos-indexes inputs/CMS-2016-premix.txt
```

This requires the index data files to be placed in their final location. However, for
early testing on LXPLUS, all steps can be run without the EOS file index cache
by means of adding the command-line option `--ignore-eos-store` to the commands below.

We can now build sample records by doing:

```console
$ python3 ./code/interface.py --create-das-json-store --ignore-eos-store inputs/CMS-2016-pileup-dataset.txt

$ auth-get-sso-cookie -u  https://cms-pdmv.cern.ch/mcm -o cookies.txt
$ python3 ./code/interface.py --create-mcm-store --ignore-eos-store inputs/CMS-2016-pileup-dataset.txt

$ python3 ./code/interface.py --get-conf-files --ignore-eos-store inputs/CMS-2016-pileup-dataset.txt

$ python3 ./code/interface.py --create-records --ignore-eos-store inputs/CMS-2016-premix.txt
```

Each step builds a subdirectory with a cache (`das-json-store`, `mcm-store` and
`config-store`). They are large, do not upload them to the repository, respect
the `.gitignore`.

The output JSON files for the dataset records will be generated in the
`outputs` directory.

The three configuration files from `./inputs/config-store` are to be copied to
`/eos/opendata/cms/configuration-files/MonteCarlo2016/`. Don't forget to add
the `*.py` extension.
