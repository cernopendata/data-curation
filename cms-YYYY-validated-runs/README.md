# cms-YYYY-validated-runs

This directory contains a helper script to prepare CMS validated runs records.

The python3 script `vali_records.py` can be used to build the records for standard pp data taking and HI-related runs. 

Inputs are in the beginning of the file e.g.

```
### input for 2013 PbPb
#
RECID_START = 14218
YEAR_RELEASED = 2013
RUN_ERA = "Run2013A"
TYPE = "pphiref"
```

The script does not require CMSSW release area and it can be run with python3:

```
python3 vali_records.py > output.json
```

The script gets the information needed for the records from the [CMS release info API server](http://api-server-cms-release-info.app.cern.ch/).

The record description text is based on the collsion type (pphiref, pPb, PbPb, pp).

For the standard pp data taking, the script lists run ranges of all released run eras in the description (i.e. "released": "yes" in the [release info](http://api-server-cms-release-info.app.cern.ch/runeras/)). The validated data listing covers also non-released run eras.

The HI-related data taking has so far been one run era at the time. 




