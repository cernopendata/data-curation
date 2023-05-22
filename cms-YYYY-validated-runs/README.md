# cms-YYYY-validated-runs

This directory contains a helper script to prepare CMS validated runs records.

The python3 script `vali_records.py` can be used to build the records for standard pp data taking and HI-related runs. 

Inputs arguments:

- recid (May 2023, the last used recid was 14210 for 2015 pp)
- year to be released
- run era (for pp, give one of the released eras, it is needed to get the collision energy, stored per era)
- type (pp, pPb, pphiref, PbPb)

Input values:

- 2013 pPb: 14216 2013 HIRun2013 pPb
- 2013 ppref: 14218 2013 Run2013A pphiref
- 2015 ppref: 14212 2015 Run2015E pphiref
- 2015 pp:  14210 2015 Run2015D pp (not used to build the current record, but tested to produce the same files)


The script does not require CMSSW release area and it can be run with python3, e.g.:

```
python3 vali_records.py 14212 2015 Run2015E pphiref > output.json
```

The script gets the information needed for the records from the [CMS release info API server](http://api-server-cms-release-info.app.cern.ch/).

The record description text is based on the collision type (pphiref, pPb, PbPb, pp).

For the standard pp data taking, the script lists run ranges of all released run eras in the description (i.e. "released": "yes" in the [release info](http://api-server-cms-release-info.app.cern.ch/runeras/)). The validated data listing covers also non-released run eras.

The HI-related data taking has so far been one run era at the time. 
 




