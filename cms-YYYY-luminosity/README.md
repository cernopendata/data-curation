# cms-YYYY-luminosity

This directory contains helper scripts to prepare CMS luminosity information records.

- subdirectory `code` contains the script to prepare the luminosity information record
- shell scripts `commands.sh` and `prescale.sh` are used in workflow `cms-luminosity-tables.yaml` in `.github/workflows` to build the luminosity information tables to be attached in the luminosity record 
- subdirectory `inputs` contains the "normtag" file needed for the luminosity calculation.

The inputs are given as GitHub workflow variables and are

- 2013 pPb: 1056 2013 HIRun2013 pPb
- 2013 ppref: 1057 2013 Run2013A pphiref
- 2015 ppref: 1058 2015 Run2015E pphiref
- 2015 pp: 1055 2015 Run2015D pp (not used to build the current record, but tested to produce the same files)
- 2016 pp: 1059 2016 Run2016G Run2016H pp