=======
 cms-mc
=======

This directory contains helper scripts used to prepare CMS MC open data
release.


To run the cms-mc you need a text file with the list of datasets (one per
line). Some lists are available in the directory `lists`.

.. cms-mc-block:: console

   export EOS_MGM_URL=root://eospublic.cern.ch
   voms-proxy-init --voms cms --rfc
   python cms-mc/interface.py --create-eos-indexes \
                              --create-das-json-store \
                              --create-mcm-store \
                              --get-conf-files \
                              lists/CMS-2012-mc-datasets.txt

To run for the categorisation only:

.. cms-mc-block:: console

   python cms-mc/interface.py --print-categorisation \
                              lists/CMS-2012-mc-datasets.txt > categories.md

This will create a markdown file with the results.

For details, see ``python cms-mc/interface.py --help``.

You can also use the bash scrips:

- `make_local_cache.sh`
- `print_results.sh`
- `run_categorisation.sh`