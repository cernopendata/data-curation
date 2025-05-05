#!/usr/bin/env python3

# For iterating over multiple files worth of text
import fileinput

# For checking for file existence
import os

# For writing csv files
import csv

# Cross sections are stored in nanobarns
xsecs = {'15':{},'16':{},'23':{}}
lumi = {'15':140000., '16':140000., '23':175000.}

# Max events in a sample to be released
sample_cap = 10e6

# Read the cross sections from the PMG text files
for campaign in xsecs:
    with open(f'/cvmfs/atlas.cern.ch/repo/sw/database/GroupData/dev/PMGTools/PMGxsecDB_mc{campaign}.txt','r') as infile:
        for line in infile:
            if 'dataset_number' in line:
                continue
            my_DSID = line.split()[0]
            my_xsec = [ float(line.split()[2]), float(line.split()[3]), float(line.split()[4]) ]
            xsecs[campaign][my_DSID] = my_xsec

# MC20 == MC16
lumi['20'] = lumi['16']
xsecs['20'] = xsecs['16']

try:
    import pyAMI.client
    import pyAMI.atlas.api as AtlasAPI
    client = pyAMI.client.Client('atlas')
    AtlasAPI.init()
except:
    print('Please make sure you have set up AMI tools (`lsetup pyami`)')
    import sys
    sys.exit(1)

# Keep sums of events
event_sum = 0
possible_events = 0

# Helper function to round to the nearest 10,000 events. Our EVNT samples are normally 10k events, and are always multiples of 10k events.
def EVNT_round(x):
    from math import ceil
    return ceil(round(x*0.0001))*10000.

# In some cases the keywords aren't correctly retrieved from AMI below.
# There is a chance that they can be retrieved from the job options themselves.
# This function tries to get them from the job options repository on cvmfs
def get_keywords_from_JO(set_name):
    did = set_name.split('.')[1]
    # See if the MC15 job options name we expect exists
    mc15jo = '/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID'+did[:3]+'xxx/MC15.'+did+'.'+set_name.split('.')[2]+'.py'
    if os.access(mc15jo,os.R_OK):
        with open(mc15jo,'r') as mc15jo_file:
            for aline in mc15jo_file:
                if 'evgenConfig.keywords' in aline.split('#')[0]:
                    exec( aline.replace('evgenConfig.','') )
                    return keywords
        print(f'For MC15 JO for {set_name} no keywords found')
    else:
        # Otherwise it had better be MC16
        from glob import glob
        mc16jo = '/cvmfs/atlas.cern.ch/repo/sw/Generators/MC16JobOptions/'+did[:3]+'xxx/'+did+'/*.py'
        for afile in glob(mc16jo):
            with open(afile,'r') as jo_file:
                for aline in jo_file:
                    if 'evgenConfig.keywords' in aline.split('#')[0]:
                        exec( aline.replace('evgenConfig.','') )
                        return keywords
        print(f'For MC(16/23) JO for {set_name} no keywords found')
    return ''

# Check what datasets have already been processed, so they are excluded from the production spreadsheets
# We will still include them in the metadata files, though!
# Keep a list of pairs of scopes and DIDs (so we have the com energy separately)
hepmc_ready = []
if os.access('HEPMC_datasets.txt',os.R_OK):
    with open('HEPMC_datasets.txt','r') as hepmc_input:
        for aline in hepmc_input:
            hepmc_ready += [ (aline.split('.')[0],aline.split('.')[1]) ]

# Read the list of EVNT and output events; keep statistics as well
with open('EVNT_metadata.csv','w') as evgen_meta_file, open('EVNT_prod_request15.csv','w') as prod_sheet15_file, open('EVNT_prod_request23.csv','w') as prod_sheet23_file, open('EVNT_empty_datasets.txt','w') as empty_sets:
    # Set up csv writers and headers for all the csv files that we're writing. Consistent formatting please.
    evgen_meta = csv.writer(evgen_meta_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    prod_sheet15 = csv.writer(prod_sheet15_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    prod_sheet23 = csv.writer(prod_sheet23_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')

    evgen_meta.writerow(['DSID','PhysicsShort','CoMEnergy','XSec','FiltEff','kFactor','Events','GenEvents','GenName','GenTune','PDF','Keywords','PhysComment','Release','Filters','JobOptions'])
    prod_sheet15.writerow(['DSID','Event input for evgen (optional)','E_CoM [GeV]','Output events','Type (Evgen, FullSim, AF2, LHE, FCSv2, FastChain, ...)','Priority','Output formats','Evgen Release','Comments','Evgen tag','Evgen merge tag','Simul tag','Merge tag','Digi tag','Reco tag','Rec Merge tag','Deriv tag','Deriv merge tag','Rivet routines'])
    prod_sheet23.writerow(['DSID','Event input for evgen (optional)','E_CoM [GeV]','Output events','Type (Evgen, FullSim, AF2, LHE, FCSv2, FastChain, ...)','Priority','Output formats','Evgen Release','Comments','Evgen tag','Evgen merge tag','Simul tag','Merge tag','Digi tag','Reco tag','Rec Merge tag','Deriv tag','Deriv merge tag','Rivet routines'])

    # Iterate over our input list
    for aset_number,aset_line in enumerate(fileinput.input(files=('EVNT_list_Baseline.txt','EVNT_list_Systematic.txt','EVNT_list_Alternative.txt','EVNT_list_Specialised.txt','EVNT_exotics_datasets.txt'))):
        # Keep folks posted on how we're doing here
        if (aset_number+1)%100==0:
            print(f'Processing dataset {aset_number+1}')
        # Grab the information we can directly from the dataset name
        aset = aset_line.strip()
        campaign = aset.split('_')[0].replace('mc','')
        com = float(aset.split('_')[1].split('.')[0].replace('p','.').replace('TeV',''))*1000.
        dsid = aset.split('.')[1]
        phys_short = aset.split('.')[2]
        # Check for the metadata in the pre-digested PMG databases
        my_xsec = 0
        my_kfact = 1
        my_filteff = 1
        # For MC23 we do the obvious thing
        if campaign=='23':
            if dsid in xsecs[campaign]:
                my_xsec = xsecs[campaign][dsid][0]
                my_filteff = xsecs[campaign][dsid][1]
                my_kfact = xsecs[campaign][dsid][2]
        # For MC15/16 we favor the MC16 file
        elif campaign=='15' or campaign=='16':
            if dsid in xsecs['16']:
                my_xsec = xsecs['16'][dsid][0]
                my_filteff = xsecs['16'][dsid][1]
                my_kfact = xsecs['16'][dsid][2]
            elif dsid in xsecs['15']:
                my_xsec = xsecs['15'][dsid][0]
                my_filteff = xsecs['15'][dsid][1]
                my_kfact = xsecs['15'][dsid][2]

        # Get all the metadata from AMI
        metadata = AtlasAPI.get_dataset_info(client, aset)[0]
        max_events = int(metadata['totalEvents'])
        # In case AMI reports no events - this should not happen
        if max_events==0:
            print(f'No events found for {dsid=}: {aset} - skipping')
            empty_sets.write(f'{aset}\n')
            continue
        # Only ask AMI if we didn't find cross section / filter efficiency / k-factor in the text files
        if my_xsec==0:
            if 'crossSection@PMG' in metadata:
                my_xsec = float(metadata['crossSection@PMG'])
            elif 'crossSection@MCGN' in metadata:
                my_xsec = float(metadata['crossSection@MCGN'])
            elif 'crossSection_mean' in metadata and metadata['crossSection_mean'] not in ['No cross section values were found','Calculation impossible']:
                my_xsec = float(metadata['crossSection_mean'])
            elif 'crossSection' in metadata and metadata['crossSection'] not in ['NULL']:
                my_xsec = float(metadata['crossSection'])
            if 'crossSection_unit' in metadata:
                if metadata['crossSection_unit'] == 'nano barn':
                    my_xsec *= 1000.
            if 'genFiltEff@PMG' in metadata:
                my_filteff = float(metadata['genFiltEff@PMG'])
            elif 'genFiltEff@MCGN' in metadata:
                my_filteff = float(metadata['genFiltEff@MCGN'])
            elif 'GenFiltEff_mean' in metdata:
                my_filteff = float(metadata['GenFiltEff_mean'])
            elif 'genFiltEff' in metadata:
                my_filteff = float(metadata['genFiltEff'])
        # Calculate the final thing
        final_xsec = my_xsec * my_kfact * my_filteff
        if final_xsec<1e-12 or my_filteff<=0:
            # Very small cross sections can happen for some samples; that's not fatal
            # Identically zero cross sections can happen for signal samples when they are meant to be
            # reweighted. These samples require some special care, so we will need to document their use.
            print(f'Warning: DSID {dsid} has values {final_xsec=} {my_xsec=} {my_kfact=} {my_filteff=}')
        # Check the number of events per file in case we need a warning
        nFiles = int(metadata['nFiles'])
        warning = ''
        if max_events / nFiles < 100:
            warning = f'Only {max_events/nFiles} events per file, '
            print(f'Warning, for {dsid=} {aset} {warning}')

        # Calculate how many events we'd want in principle
        estimate = EVNT_round( int(final_xsec * lumi[campaign] * 2.) )
        # In all cases, never less than 10k
        events = int(max(10e3,min([estimate,max_events,sample_cap])))

        # Get some other useful metadata
        genName = metadata['generatorName'] if 'generatorName' in metadata else ''
        genTune = metadata['generatorTune'] if 'generatorTune' in metadata else ''
        # There is a "generator" piece of metadata that appears in all cases to be less complete
        # and less helpful than generatorName. Let's omit it.
        #generator = metadata['generator'] if 'generator' in metadata else ''

        keywords = metadata['keywords'] if 'keywords' in metadata else ''
        # Check if we have empty keywords. See if we can get them from the JO if so.
        if keywords.strip()=='':
            keywords = get_keywords_from_JO(aset)
        # Last resort: Add something that seems sensible based on the sample name.
        # Convenient list of ATLAS allowed keywords:
        #  https://gitlab.cern.ch/atlas-physics/pmg/infrastructure/mc15joboptions/-/blob/master/common/evgenkeywords.txt
        if keywords.strip()=='':
            if '_jets_JZ' in aset or '_jetjet_JZ' in aset:
                keywords = 'jets, qcd, sm, dijet'
            elif '_ttW_' in aset:
                keywords = 'ttw, sm'
                if '_2Lfilter' in aset or '_2LFilter' in aset:
                    keywords += 'multilepton'
            elif '_yyALP' in aset:
                keywords = 'bsm, ALP, exotic, diphoton'
            elif '_ttll_' in aset:
                keywords = 'ttz, multilepton, sm'
            elif '_ttbar_' in aset:
                keywords = 'top, ttbar, sm'
                if 'nonallhad' in aset:
                    keywords += ', lepton'
                else:
                    keywords += ', allhadronic'
            elif '_tWZ_' in aset:
                keywords = 'top, sm'
            elif '_tllq_' in aset:
                keywords = 'lepton, singletop, tz, sm'
            elif '_eegammagamma_' in aset:
                keywords = 'lo, 2electron, sm, 2photon'
            elif '_bbA_' in aset or ('_bbH_' in aset and '_tanb10' in aset):
                keywords = 'ttbb, higgs, exotic, bsm, bsmhiggs'
            elif '_ggH400' in aset:
                keywords = 'bsm, higgs, 2electron, exotic, bsmhiggs'
            elif '346601' in aset:
                keywords = 'ttbar, higgs, ttHiggs, sm'
            elif '346602' in aset:
                keywords = 'tHiggs, higgs, sm'
        # Add to the keywords the type of file we are processing
        for atype in ['Baseline','Systematic','Alternative','Specialised']:
            if fileinput.filename() == f'EVNT_list_{atype}.txt':
                keywords += f', {atype}'
        # Add some additional keywords based on the sample name
        if 'monoSbbRelic' in aset:
            keywords += ', monoSbbRelic'
        if '_ALPs_' in aset:
            keywords += ', ALP'
        if '_SVJLschan_' in aset or '_SVJSChan2j_' in aset:
            keywords += ', SVJ'
        if '_enugamma_' in aset and 'electron' not in keywords:
            keywords += ', electron, photon'
        if '_munugamma_' in aset and 'muon' not in keywords:
            keywords += ', muon, photon'
        if '_taunugamma_' in aset and 'tau' not in keywords:
            keywords += ', tau, photon'
        if '801974' in aset:
            # This is an exotics sample used to study pileup jets
            keywords += ', Baseline'
        # Last keyword manipulation: let's sort them so they're a little prettier in the spreadsheets
        keywords = ', '.join(sorted([ x.strip() for x in keywords.split(',') ]))

        # More AMI metadata
        physComment = metadata['physicsComment'] if 'physicsComment' in metadata else ''
        PDF = metadata['PDF'] if 'PDF' in metadata else ''
        release = metadata['AtlasRelease'] if 'AtlasRelease' in metadata else ''
        filterNames = metadata['genFilterNames'] if 'genFilterNames' in metadata else ''

        # New MC Job Options repo, or old?
        if int(dsid)>500000:
            link = f'https://gitlab.cern.ch/atlas-physics/pmg/mcjoboptions/-/blob/master/{dsid[:3]}xxx/{dsid}/mc.{phys_short}.py'
        else:
            link = f'https://gitlab.cern.ch/atlas-physics/pmg/infrastructure/mc15joboptions/-/blob/master/share/DSID{dsid[:3]}xxx/MC15.{dsid}.{phys_short}.py'

        # Record the metadata to the output file
        evgen_meta.writerow([dsid,phys_short,com,my_xsec,my_filteff,my_kfact,events,max_events,genName,genTune,PDF,keywords,physComment,release,filterNames,link])

        # Add to our sums
        event_sum += events
        possible_events += max_events

        # Now a tweak for the production system. If we are producing all events from a sample, we should just set -1 as the number of events
        if events == max_events:
            events = -1

        # Add a line to the production request if the HEPMC datasets aren't already ready
        if (aset.split('.')[0],aset.split('.')[1]) not in hepmc_ready:
            if campaign == '15' or campaign=='16':
                prod_sheet15.writerow([dsid,aset,com,events,'HEPMC','3','HEPMC','23.6.45',warning+'EVNTtoHEPMC conversion'])
            elif campaign == '23':
                prod_sheet23.writerow([dsid,aset,com,events,'HEPMC','3','HEPMC','23.6.45',warning+'EVNTtoHEPMC conversion'])

# Print some summary statistics; useful for seeing how things are evolving (usually not too rapidly)
print(f'Expecting to release {event_sum:,} of {possible_events:,} events ({round(event_sum/possible_events*100.,1)}%)')

# All done!
