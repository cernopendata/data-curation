#!/usr/bin/env python

import json
import jsonschema
import os

schema_str = open('./cernopendata/jsonschemas/records/record-v1.0.0.json', 'r').read()
schema = json.loads(schema_str)

for filename in os.listdir('./cernopendata/modules/fixtures/data/records'):
    records_str = open(os.path.join('./cernopendata/modules/fixtures/data/records', filename), 'r').read()
    print(filename)
    records = json.loads(records_str)
    for record in records:
        jsonschema.validate(record, schema)
print('OK')
