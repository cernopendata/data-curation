# cms-YYYY-luminosity

This directory contains helper scripts to prepare CMS luminosity information records.

- subdirectory `code` contains the script to prepare the luminosity information record
- shell scripts `commands.sh` and `prescale.sh` are used in workflow `cms-luminosity-tables.yaml` in `.github/workflows` to build the luminosity information tables to be attached in the luminosity record 
- subdirectory `inputs` contains the "normtag" file needed for the luminosity calculation.