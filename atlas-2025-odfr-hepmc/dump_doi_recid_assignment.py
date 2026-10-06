#!/usr/bin/env python3

# Simple helper to print the current record assignments
# Handy to cross-check what the script did by eye
# And to see if we are close to out of DOIs
import json
with open('doi_recid_assignment.json','r') as f:
    d = json.load(f)
    for a in d:
        print(a)
