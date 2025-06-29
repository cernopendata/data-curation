# Scripts for the Feb 2025 upload of ATLAS Open Data for Education and Outreach

The scripts and files in the repository are as follows:

* `rucio_reformat.sh` transfers files from Eirik's eos space into central rucio
open data space, defining open-ended rules for keeping the datasets there. Two
datasets are created per skim: one for MC, and one for data.

* `unskimmed_data.txt` is the list of unskimmed data and MC files available on
rucio. Some of the files are quite large, so this had to be handled separately.

* `updated_bjet_skims.txt` is a special list of files for updating the b-jet
skims, which needed a second round of updates following further validation.

* `qcd_skims.txt` contains a list of QCD jet datasets that are provided for
validation purposes for the beta release, and will be made available publicly
with the full release.

* `rucio_jetskim_specialhandling.sh` is a script for special handling of the
b-jet skim updates and QCD jet skim files.

* `rucio_reformat_unskimmed.sh` moves the unskimmed data into the appropriate
places and renames the datasets as needed.

* `rucio_check.sh` checks for any inconsistencies between the files in rucio and
those on eos, and checks to make sure that things have been transferred to the
main open data endpoint (ie they aren't still only on scratch space)

* `dataset_list.txt` is a list of the datasets created in rucio for this release

* `create_metadata.py` creates a metadata json file containing all the datasets
to be released (those in `dataset_list.txt`), and for each dataset it includes
a dictionary of files. For each file, it contains the following metadata:
   * adler32 check-sum
   * size in bytes
   * number of events
   * type (root)
   * uri (file location on the rucio endpoint)

* `odeo_file_mapping_ODEO_v0_FEB2025_2025-06-30.json` is the output from the
most recent run of `create_metadata.py`

* `make_odeo_json.py` creates all of the json files for the CERN open data
portal records. One record is created per rucio dataset.

* `build_full_metadata_json.py` is a script for building json-formatted
metadata files for the data and MC following the running of all of the above
scripts, for injection of the metadata into the atlasopenmagic database. It
requires the csv file available from
`https://opendata.atlas.cern/docs/data/for_education/13TeV25_metadata` and
produces files named `data_database_metadata_2025e.json` and
`mc_database_metadata_2025e.json`
