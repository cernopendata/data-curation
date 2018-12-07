=======
 cms-mc
=======

This directory contains helper scripts used to prepare CMS MC Open Data
release:

- `cms-mc/` folder contains the python code.
- `lists/` folder contain text files with the list of datasets for each year.
- `inputs/` folder contain files with extra information for the datasets, such
  as `DOI` identifier and `RECID`.

Every step necessary to produce the final `*.json` files is handled by the
`cmc-mc/interface.py` script. Details about it can be queried with the command:

.. code-block:: console

   python cms-mc/interface.py --help

The bash scrips in the current directory handle all the parameters of the
interface:

- `make_local_cache.sh`: creates a local cache of all information needed.
- `print_results.sh`: creates a set of markdown and HTML pages with all the
  information available.
- `run_categorisation.sh`: creates a set of markdown and HTML pages with the
  datasets splitted in their categories.
- `create_records.sh`: create the final .json files:
  - one for the MC records
  - one for the configuration files

The steps to follow are:

.. code-block:: console

   voms-proxy-init --voms cms --rfc --valid 190:00
   sh make_local_cache.sh
   sh create_records.sh

Warning: creating a local cache takes a long time!


Issues
------

2011
~~~~

The AODSIM files and metadata disappeared from McM. But the GEN-SIM are still
there. The scripts do not handle this. It should be modified to get the oldest
parent, find its prepId and then query McM. This way it should get the
dictionary (cmsDriver script) and genFragment.

General
~~~~~~~

Record json not tested with jsonschema.