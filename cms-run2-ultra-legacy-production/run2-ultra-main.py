#!/usr/bin/env python

""" A helper script which finds all related datasets for one specified campaign

Extracts all important provenance metadata, which later gets stored on DPOA
storage like cmsdriver scripts, configuration files, cross section and lastly
(but hopefully not the least one) edmProvDump.py and edmLHCHeader.py output.

"""

import ultra_processing.click as click
import json
from ultra_processing.mcm_campaign_list import query_for_key_values

@click.command()
@click.option('--campaign', '-c', required=True,
              help='Specify campaign name for metadata extraction')
def main(campaign):
    """Downloads from McM and stores all metadata information on DPOA
    Steps it takes sequentially:
    1) Downloads for ech parent dataset from McM service metadata like: 
    cmsdriver scripts, configuration files, cross section.
    2) Stores all this metada information on DPOA storage.
    3) If root files are available on DAS service, finds location using global
    locator and runs scripts: edmDumpProv.py and if exists LHC also 
    edmLHCheader.py
    """
    
    query_for_key_values(campaign)

if __name__ == '__main__':
    main()
