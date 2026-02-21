===============
 data-curation
===============

.. image:: https://github.com/cernopendata/data-curation/workflows/CI/badge.svg
   :target: https://github.com/cernopendata/data-curation/actions

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/cernopendata/opendata.cern.ch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

.. image:: https://img.shields.io/badge/licence-GPL_2-green.svg?style=flat
   :target: https://raw.githubusercontent.com/cernopendata/data-curation/master/LICENSE

About
-----

This repository contains a collection of data ingestion and curation tools used
to prepare the datasets, software and any accompanying material for public open
data releases on the `CERN Open Data <http://opendata.cern.ch/>`_ portal.

Generic utilities
-----------------

- `utils <utils>`_ - various helper scripts


Specific utilities
------------------

Specific data ingestion and curation campaigns:

- `atlas-2016-masterclasses <atlas-2016-masterclasses>`_ -- helper scripts for the ATLAS 2016 masterclasses release
- `atlas-2016-outreach <atlas-2016-outreach>`_ -- helper scripts for the ATLAS 2016 outreach release
- `atlas-2024-odfr <atlas-2024-odfr>`_ -- helper scripts for the ATLAS 2024 Open Data For Research release
- `atlas-2024-odfr-hi <atlas-2024-odfr-hi>`_ -- helper scripts for the ATLAS 2024 Open Data For Research heavy ion release
- `cms-2010-collision-datasets <cms-2010-collision-datasets>`_ -- helper scripts for the CMS 2010 open data release (collision datasets)
- `cms-2010-simulated-datasets <cms-2010-simulated-datasets>`_ -- helper scripts for the CMS 2010 open data release (simulated datasets)
- `cms-2011-collision-datasets <cms-2011-collision-datasets>`_ -- helper scripts for the CMS 2011 open data release (collision datasets)
- `cms-2011-collision-datasets-runb-update <cms-2011-collision-datasets-runb-update>`_ -- helper scripts for the CMS 2011 RunB open data release (collision datasets)
- `cms-2011-hlt-triggers <cms-2011-hlt-triggers>`_ -- helper scripts for the CMS 2011 open data release (HLT triggers)
- `cms-2011-l1-triggers <cms-2011-l1-triggers>`_ -- helper scripts for the CMS 2011 open data release (L1 triggers)
- `cms-2011-simulated-datasets <cms-2011-simulated-datasets>`_ -- helper scripts for the CMS 2011 open data release (simulated datasets)
- `cms-2012-collision-datasets <cms-2012-collision-datasets>`_ -- helper scripts for the CMS 2012 RunB RunC open data release (collision datasets)
- `cms-2012-collision-datasets-update <cms-2012-collision-datasets-update>`_ -- helper scripts for the CMS 2012 RunA RunD open data release (collision datasets)
- `cms-2012-event-display-files <cms-2012-event-display-files>`_ -- helper scripts for the CMS 2012 open data release (event display files)
- `cms-2012-simulated-datasets <cms-2012-simulated-datasets>`_ -- helper scripts for the CMS 2012 open data release (simulated datasets)
- `cms-2013-collision-datasets-hi <cms-2013-collision-datasets-hi>`_ - helper scripts for CMS 2013 heavy ion release (lead collision datasets)
- `cms-2013-collision-datasets-hi-ppref <cms-2013-collision-datasets-hi-ppref>`_ - helper scripts for CMS 2013 heavy ion release (proton-proton reference collision datasets)
- `cms-2013-hlt-triggers <cms-2013-hlt-triggers>`_ - helper scripts for CMS 2013 trigger information
- `cms-2013-simulated-datasets-hi <cms-2013-simulated-datasets-hi>`_ -- helper scripts for the CMS 2013 HI open data release (simulated datasets)
- `cms-2015-collision-datasets <cms-2015-collision-datasets>`_ -- helper scripts for the CMS 2015 open data release (collision datasets)
- `cms-2015-collision-datasets-hi-ppref <cms-2015-collision-datasets-hi-ppref>`_ - helper scripts for CMS 2015 heavy ion release (proton-proton reference collision datasets)
- `cms-2015-simulated-datasets <cms-2015-simulated-datasets>`_ -- helper scripts for the CMS 2015 open data release (simulated datasets)
- `cms-2016-collision-datasets <cms-2016-collision-datasets>`_ -- helper scripts for the CMS 2016 open data release (collision datasets)
- `cms-2016-pileup-dataset <cms-2016-pileup-dataset>`_ -- helper scripts for the CMS 2016 open data release (pileup dataset)
- `cms-2016-simulated-datasets <cms-2016-simulated-datasets>`_ -- helper scripts for the CMS 2016 open data release (simulated datasets)
- `cms-YYYY-luminosity <cms-YYYY-luminosity>`_ -- helper scripts for the CMS luminosity information records (any year)
- `cms-YYYY-run-numbers <cms-YYYY-run-numbers>`_ -- helper scripts for enriching CMS dataset run numbers (any year)
- `cms-YYYY-simulated-datasets <cms-YYYY-simulated-datasets>`_ -- helper scripts for CMS simulated dataset records (any year)
- `cms-YYYY-validated-runs <cms-YYYY-validated-runs>`_ -- helper scripts for the CMS validated runs records (any year)
- `cms-derived-data <cms-derived-data>`_ -- helper scripts for the CMS derived datasets (NanoAODRun1, PFNano, POET)
- `cms-release-info <cms-release-info>`_ -- CMS year-specific and run-era-specific information
- `cms-run2-hlt-triggers <cms-run2-hlt-triggers>`_ -- helper scripts for the CMS Run2 data release (HLT triggers)
- `cms-run2-ultra-legacy-production <cms-run2-ultra-legacy-production>`_ - helper scripts for CMS Run2 ultra-legacy production
- `cod2-to-cod3 <cod2-to-cod3>`_ - record migration from version 2 to version 3
- `jade-2023-raw-datasets <jade-2023-raw-datasets>`_ - helper scripts for the initial release of JADE data
- `opera-2017-multiplicity-studies <opera-2017-multiplicity-studies>`_ - helper scripts for the release of OPERA multiplicity studies
- `opera-2019-electron-neutrinos <opera-2019-electron-neutrinos>`_ - helper scripts for the release of OPERA electron neutrino events
- `opera-2019-neutrino-induced-charm <opera-2019-neutrino-induced-charm>`_ - helper scripts for the release of OPERA charm events

Related links
-------------

See also:

- `CERN Open Data <http://opendata.cern.ch>`_ portal
- its `source code <https://github.com/cernopendata/opendata.cern.ch>`_
- its `record fixtures <https://github.com/cernopendata/opendata.cern.ch/tree/master/cernopendata/modules/fixtures/data/records>`_

Contributors
------------

The list of contributors in alphabetical order:

- `Anna Trzcinska <https://github.com/annatrz>`_
- `Artemis Lavasa <https://orcid.org/0000-0001-5633-2459>`_
- `Audrius Mecionis <https://orcid.org/0000-0002-3759-1663>`_
- `Heitor de Bittencourt <https://linkedin.com/in/heitorpb>`_
- `Dana Alsharif <danaalsharif03@gmail.com>`_
- `Jan Okraska <https://orcid.org/0000-0002-1416-3244>`_
- `Julie Hogan <https://orcid.org/0000-0002-8604-3452>`_
- `Joud Masoud <joud003@gmail.com>`_
- `Kati Lassila-Perini <https://orcid.org/0000-0002-5502-1795>`_
- `Mantas Savaniakas <https://github.com/mantasavas>`_
- `Miko Piitsalo <https://github.com/mokotus>`_
- `Nancy Hamdan <nancyehamdan@gmail.com>`_
- `Osama Sh. Almomani <https://github.com/OsamaMomani>`_
- `Tibor Šimko <https://orcid.org/0000-0001-7202-5803>`_
- `Xiaohe Shen <https://github.com/Ari-mu-l>`_
- `Zach Marshall <https://github.com/zlmarshall>`_
