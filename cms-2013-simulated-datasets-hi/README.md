# cms-2013-simulated-datasets-hi

This directory contains helper scripts used to prepare CMS 2013 HI simulated
datasets for the open data release.

The processes should run on LXLUS8 as "cernapcms".

First, create EOS file indexes (debug as "cernapcms", run as "simko"):

```console
$ python3 ./code/interface.py --create-eos-indexes ./inputs/CMS-2013-hi-mc-datasets.txt > log 2>&1
```
Second, create DAS cache:

```console
$ voms-proxy-init --voms cms --rfc --valid 190:00
$ python3 ./code/interface.py --create-das-json-store ./inputs/CMS-2013-hi-mc-datasets.txt
```

Third, create McM cache:

```
$ python3 ./code/interface.py --create-mcm-store ./inputs/CMS-2013-hi-mc-datasets.txt
```

Fourth, get configuration files:

```
$ python3 ./code/interface.py --get-conf-files ./inputs/CMS-2013-hi-mc-datasets.txt
```

Fifth, create records:

```
$ python3 ./code/interface.py --create-records ./inputs/CMS-2013-hi-mc-datasets.txt > ./outputs/cms-simulated-datasets-2013-hi.json
$ \cp ./outputs/cms-simulated-datasets-2013-hi.json ~o/cernopendata/modules/fixtures/data/records
```

Sixth, create configuration file helpers:

```
$ python3 ./code/interface.py --create-conffile-records ./inputs/CMS-2013-hi-mc-datasets.txt | jq > ./outputs/cms-configuration-files-2013-hi.json
```

Seventh, copy configuration files onto EOS whilst adding `.py` extension:

```
$ eos mkdir /eos/opendata/cms/configuration-files/MonteCarlo2013
$ cd inputs/config-store 
$ for file in *.configFile; do eos cp $file /eos/opendata/cms/configuration-files/MonteCarlo2013/$file.py; done
```
