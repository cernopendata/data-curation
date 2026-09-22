#!/usr/bin/env python3

# Gather exotics datasets to be released

# Get our rucio client ready
try:
    from rucio.client.client import Client
    rc = Client()
except ImportError:
    print('Do not forget to set up rucio first!')
    print('lsetup rucio')
    print('And then voms proxy init')
    import sys
    sys.exit(1)

# Possible 13 TeV and 13.6 TeV dataset scopes to check
possible_13_scopes = ['mc15_13TeV','mc16_13TeV','mc20_13TeV']
possible_13p6_scopes = ['mc23_13p6TeV']

# Keep a list of sets that we've already found, so that we don't have to look again
already_parsed = []
with open('EVNT_exotics_datasets.txt','r') as exo_datasets:
    for aline in exo_datasets:
        already_parsed += [ (aline.split('.')[0].split('_')[1] , aline.split('.')[1] , aline.split('.')[2]) ]

# Loop through all the exotics dataset inputs
# Because we pre-checked what was there, we are only appending to the file
with open('EVNT_exotics.data','r') as exo_input, open('EVNT_exotics_datasets.txt','a') as exo_output:
    # Iterate through the file
    for n,aline in enumerate(exo_input):
        # Skip the header
        if 'DSName' in aline:
            continue
        # Let folks know how we're doing
        if n%100==0:
            print(f'Working on dataset {n}, DSID {aline.split()[0]}')

        # 13 TeV datasets first. See if we can find ones in any scope. Skip task ID datasets.
        found13 = ('13TeV',aline.split()[0],aline.split()[1]) in already_parsed
        dids_13 = []
        if not found13:
            for ascope in possible_13_scopes:
                dsname = ascope+'.'+aline.split()[0]+'.'+aline.split()[1]+'.evgen.EVNT.e*'
                dids_13 += [ did for did in rc.list_dids(scope=ascope,filters={'name':dsname}) if '_tid' not in did ]
            # Warn in case we have multiple options. We'll take the last one.
            if len(dids_13)>1:
                print(f'For DID {aline.split()[0]} found: {dids_13}. Will take {dids_13[-1]}')
            # Write the results to the output file
            if len(dids_13)>0:
                exo_output.write(dids_13[-1]+'\n')

        # Now 13.6 TeV datasets. See if we can find ones in any scope. Skip task ID datasets.
        found13p6 = ('13p6TeV',aline.split()[0],aline.split()[1]) in already_parsed
        dids_13p6 = []
        if not found13p6:
            for ascope in possible_13p6_scopes:
                dsname = ascope+'.'+aline.split()[0]+'.'+aline.split()[1]+'.evgen.EVNT.e*'
                dids_13p6 += [ did for did in rc.list_dids(scope=ascope,filters={'name':dsname}) if '_tid' not in did ]
            if len(dids_13p6)>1:
                print(f'For DID {aline.split()[0]} found: {dids_13p6}. Will take {dids_13p6[-1]}')
            # Write the results to the output file
            if len(dids_13p6)>0:
                exo_output.write(dids_13p6[-1]+'\n')

        # Warn if we really didn't find anything
        if len(dids_13+dids_13p6)==0 and not found13 and not found13p6:
            print(f'Warning: for DID {aline.split()[0]} did not find any EVNT datasets.')

    # Now just add some simple extras
    with open('EVNT_exotics_extras.txt','r') as extra_datasets:
        for aline in extra_datasets:
            exo_output.write(aline.strip()+'\n')
