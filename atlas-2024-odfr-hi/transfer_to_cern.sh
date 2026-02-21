#!/usr/bin/bash

# Transfer all the datasets in the p6026 GRL file to CERN-PROD_OPENDATA. We take the entire datasets. No lifetime is set for the transfers - they should be there forever.
for adataset in `cat dataset_list.txt`
do
  rucio add-rule --activity 'Data Consolidation' --notify N --comment 'Transfer for HI Open Data' --account opendata --skip-duplicates ${adataset} 1 CERN-PROD_OPENDATA
done

# Or --activity "User Subscriptions"
# 
# 
# usage: rucio add-rule [-h] [--weight WEIGHT] [--lifetime LIFETIME] [--grouping {DATASET,ALL,NONE}] [--locked] [--source-replica-expression SOURCE_REPLICA_EXPRESSION] [--notify NOTIFY] [--activity ACTIVITY]
#                       [--comment COMMENT] [--ask-approval] [--asynchronous] [--delay-injection DELAY_INJECTION] [--account RULE_ACCOUNT] [--skip-duplicates]
#                       dids [dids ...] copies rse_expression
# 
# positional arguments:
#   dids                  DID(s) to apply the rule to
#   copies                Number of copies
#   rse_expression        RSE Expression
# 
# optional arguments:
#   -h, --help            show this help message and exit
#   --weight WEIGHT       RSE Weight
#   --lifetime LIFETIME   Rule lifetime (in seconds)
#   --grouping {DATASET,ALL,NONE}
#                         Rule grouping
#   --locked              Rule locking
#   --source-replica-expression SOURCE_REPLICA_EXPRESSION
#                         RSE Expression for RSEs to be considered for source replicas
#   --notify NOTIFY       Notification strategy : Y (Yes), N (No), C (Close)
#   --activity ACTIVITY   Activity to be used (e.g. User, Data Consolidation)
#   --comment COMMENT     Comment about the replication rule
#   --ask-approval        Ask for rule approval
#   --asynchronous        Create rule asynchronously
#   --delay-injection DELAY_INJECTION
#                         Delay (in seconds) to wait before starting applying the rule. This option implies --asynchronous.
#   --account RULE_ACCOUNT
#                         The account owning the rule
#   --skip-duplicates     Skip duplicate rules
# 
