#!/usr/bin/env python3

# Load the existing list of dictionaries
# Each dictionary has a doi and a recid
# We assign a record to it in the dictionary
# The original is from
# https://github.com/cernopendata/opendata.cern.ch/pull/3737
with open('doi_recid_assignment.json','r') as f:
    doirecid_list = json.load(f)

# Add extra dois / record IDs here as needed!
doirecid_list += [
#  {
#    "doi": "10.7483/OPENDATA.ATLAS.3I7V.FNQQ",
#    "recid": "160002"
#  },
                 ]

# Finally, record a new DOI + Record ID list
with open('doi_recid_assignment.json','w') as f:
    json.dump( obj=doirecid_list, fp=f )

