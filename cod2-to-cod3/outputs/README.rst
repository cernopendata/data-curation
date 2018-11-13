This directory contains the resulting JSON files that are committed to the main
CERN Open Data repository as record fixtures.

The final file list snapshot:

.. code-block:: console

    $ ls -l outputs/*.json
    -rw-r--r-- 1 simko 48    6746 Dec 12  2017 alice-analysis-modules.json
    -rw-r--r-- 1 simko 48     995 Dec 12  2017 alice-derived-datasets.json
    -rw-r--r-- 1 simko 48    1523 Dec 12  2017 alice-learning-resources.json
    -rw-r--r-- 1 simko 48   22902 Dec 12  2017 alice-reconstructed-data.json
    -rw-r--r-- 1 simko 48     794 Dec 12  2017 alice-vm-image.json
    -rw-r--r-- 1 simko 48    2096 Dec 12  2017 atlas-all-samples.json
    -rw-r--r-- 1 simko 48  115177 Dec 12  2017 atlas-derived-datasets.json
    -rw-r--r-- 1 simko 48   16524 Dec 12  2017 atlas-higgs-challenge-2014.json
    -rw-r--r-- 1 simko 48    1184 Dec 12  2017 atlas-learning-resources.json
    -rw-r--r-- 1 simko 48  113090 Dec 12  2017 atlas-simulated-datasets.json
    -rw-r--r-- 1 simko 48   12937 Dec 12  2017 atlas-tools.json
    -rw-r--r-- 1 simko 48  494661 Dec 12  2017 cms-author-list.json
    -rw-r--r-- 1 simko 48  516061 Dec 12  2017 cms-author-list-Run2011A.json
    -rw-r--r-- 1 simko 48     708 Dec 12  2017 cms-condition-data-Run2010B.json
    -rw-r--r-- 1 simko 48    2980 Dec 12  2017 cms-condition-data-Run2011A.json
    -rw-r--r-- 1 simko 48  681558 Dec 12  2017 cms-configuration-files-Run2011A.json
    -rw-r--r-- 1 simko 48    7489 Dec 12  2017 cms-csv-files.json
    -rw-r--r-- 1 simko 48    8098 Dec 12  2017 cms-derived-csv-Run2011A.json
    -rw-r--r-- 1 simko 48    4992 Dec 12  2017 cms-derived-pattuples-ana.json
    -rw-r--r-- 1 simko 48    5152 Dec 12  2017 cms-derived-pattuples-ana-Run2011A.json
    -rw-r--r-- 1 simko 48   29700 Dec 12  2017 cms-eventdisplay-files.json
    -rw-r--r-- 1 simko 48   40132 Dec 12  2017 cms-eventdisplay-files-Run2011A.json
    -rw-r--r-- 1 simko 48   12804 Dec 12  2017 cms-hamburg-files.json
    -rw-r--r-- 1 simko 48  143326 Dec 12  2017 cms-hlt-2011-configuration-files.json
    -rw-r--r-- 1 simko 48  135503 Dec 12  2017 cms-l1-trigger-information-Run2011A.json
    -rw-r--r-- 1 simko 48    9953 Dec 12  2017 cms-learning-resources.json
    -rw-r--r-- 1 simko 48    5055 Dec 12  2017 cms-luminosity-information.json
    -rw-r--r-- 1 simko 48   60459 Dec 12  2017 cms-masterclass-files.json
    -rw-r--r-- 1 simko 48    9583 Dec 12  2017 cms-open-data-instructions.json
    -rw-r--r-- 1 simko 48    1461 Dec 12  2017 cms-pileup-configuration-files.json
    -rw-r--r-- 1 simko 48   83115 Dec 12  2017 cms-primary-datasets.json
    -rw-r--r-- 1 simko 48  180267 Dec 12  2017 cms-primary-datasets-Run2011A.json
    -rw-r--r-- 1 simko 48 2177893 Dec 12  2017 cms-simulated-datasets-Run2011A.json
    -rw-r--r-- 1 simko 48    8032 Dec 12  2017 cms-tools-ana.json
    -rw-r--r-- 1 simko 48    7056 Dec 12  2017 cms-tools-ana-Run2011A.json
    -rw-r--r-- 1 simko 48    1884 Dec 12  2017 cms-tools-cmssw.json
    -rw-r--r-- 1 simko 48    1889 Dec 12  2017 cms-tools-cmssw-Run2011A.json
    -rw-r--r-- 1 simko 48    4583 Dec 12  2017 cms-tools-dimuon-filter.json
    -rw-r--r-- 1 simko 48    5204 Dec 12  2017 cms-tools-dimuon-spectrum-2010.json
    -rw-r--r-- 1 simko 48    3359 Dec 12  2017 cms-tools-ispy.json
    -rw-r--r-- 1 simko 48    2199 Dec 12  2017 cms-tools-ispy-Run2011A.json
    -rw-r--r-- 1 simko 48    4386 Dec 12  2017 cms-tools-vm-image.json
    -rw-r--r-- 1 simko 48    4551 Dec 12  2017 cms-tools-vm-image-Run2011A.json
    -rw-r--r-- 1 simko 48   13746 Dec 12  2017 cms-trigger-information-Run2011A.json
    -rw-r--r-- 1 simko 48 1266459 Dec 12  2017 cms-trigger-path-Run2011A.json
    -rw-r--r-- 1 simko 48    6475 Dec 12  2017 cms-validated-runs.json
    -rw-r--r-- 1 simko 48   15306 Dec 12  2017 cms-validation-code-Run2010B.json
    -rw-r--r-- 1 simko 48    4087 Dec 12  2017 data-policies.json
    -rw-r--r-- 1 simko 48    2920 Dec 12  2017 lhcb-derived-datasets.json
    -rw-r--r-- 1 simko 48    1019 Dec 12  2017 lhcb-learning-resources.json
    -rw-r--r-- 1 simko 48     897 Dec 12  2017 lhcb-tools.json
    -rw-r--r-- 1 simko 48   11755 Dec 12  2017 opera-author-list.json
    -rw-r--r-- 1 simko 48 6290266 Dec 12  2017 opera-detector-events.json
    -rw-r--r-- 1 simko 48    5699 Dec 12  2017 opera-ecc-datasets.json
    -rw-r--r-- 1 simko 48    5870 Dec 12  2017 opera-ed-datasets.json
