import os, sys, time
import string

os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')

from mcm.rest import McM

def query_for_key_values(campaign_name):
  mcm = McM(dev=False, debug=True)
  page = 0
  res = mcm.get('requests',query='member_of_campaign=' + campaign_name, page=page)
  print("Total datasets in page: " + str(len(res)))

   
  while len(res) !=0:
    for r in res:
      output_dataset = r['output_dataset']
      prep_id = r['prepid']
      config_id = r['config_id']
      cross_section = r['generator_parameters']

      print("\n")
      print("output_dataset: " + str(output_dataset))
      print("prep_id: " + str(prep_id))
      print("config_id: " + str(config_id))
      print("cross_section: " + str(cross_section))

      # Getting cmsdriver script
      query_for_cms_driver_script(prep_id)
      query_for_config_files(config_id) 

    # Go to next page, and repeat procedure of extraction
    page += 1
    res = mcm.get('requests',query=campaign_name, page=page)
  

def query_for_config_files(configs):
  mcm = McM(dev=False)
  
  r_configs = []
  for config_id in configs:
    r_configs.append(mcm.get_raw(config_id, web=True))

 
def query_for_cms_driver_script(prep_id):
  mcm = McM(dev=False, debug=True)
  script = mcm.get_cms_driver_script(prep_id)

