=======
 utils
=======

This directory contains generally useful utilities independent of any specific data ingestion campaign.

- `aiadm-move-files.sh <aiadm-move-files.sh>`_ - move files from EOS staging area to EOS production area
- `create_eos_file_indexes.py <create_eos_file_indexes.py>`_ - create EOS file indexes for individual files
- `merge_delete_fixtures.py <merge_delete_fixtures.py>`_ - helper script to merge record fields
- `update_fixtures.py <update_fixtures.py>`_ - update some fields in JSON files based on other JSON files
- `update_checksums.py <update_checksums.py>`_ - update fixture file sizes and checksums based on EOS information
- `update_ondemand.py <update_ondemand.py>`_ - update fixture distribution.availability ondemand field for CMS MC datasets
