import json
import re
from collections import defaultdict

import click
from bs4 import BeautifulSoup


def convert_description_string_to_json(methodology):
    LINK_INFO = {}
    exec(open('../outputs/config_files_link_info.py', 'r').read())
    LINK_INFO_REV = {v: k for k, v in LINK_INFO.items()}
    description = methodology['description']
    soup = BeautifulSoup(description)
    step_titles = soup.find_all('strong', string=re.compile("Step*"))
    steps_data = []
    for step_title in step_titles:
        step_name = step_title.text.split(' ', 1)[-1].strip()
        step_element = step_title.next_siblings
        elements = [element for element in step_element if element.string]
        step = {
            'type': step_name,
            'configuration_files': []
        }
        # only for LHE step, add additional description
        if step['type'] == 'LHE':
            step['note'] = '''To get the exact LHE and generator's parameters, see <a href=\"/docs/cms-mc-production-overview#finding-the-generator-parameters\"> CMS Monte Carlo production overview</a>.'''
        for element_tag in elements:
            element = element_tag.string
            conf_files_string = 'Configuration file'
            if conf_files_string in element:
                recid = element_tag.get('href').split('/')[-1].strip()
                conf_file_data = {}
                conf_file_data['recid'] = recid
                if recid in LINK_INFO_REV:
                    conf_file_data['cms_confdb_id'] = LINK_INFO_REV[int(recid)]
                # discovering the process name
                if 'HLT' in element:
                    conf_file_data['process'] = 'HLT'
                elif 'RECO' in element:
                    conf_file_data['process'] = 'RECO'
                else:
                    conf_file_data['process'] = step_name

                conf_file_data['title'] = 'Configuration file for {process_name} step {file_name}'.format(
                    process_name=conf_file_data['process'],
                    file_name=element.split(' ')[-1].strip())

                step['configuration_files'].append(conf_file_data)
            else:
                k, v = element.split(':', 1)
                k = k.lower().replace(' ', '_')
                step[k] = v.strip()
        steps_data.append(step)

    new_methodology = {
        'steps' : steps_data,
        'description' : '<p>These data were generated in several steps (see also <a href=\"/docs/cms-mc-production-overview\">CMS Monte Carlo Production Overview</a>):</p>\n'
    }
    return new_methodology


@click.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def convert_descriptions_in_file(input_file, output_file):
    """
    Script originaly used for files:
        - input_file: ~/cod/opendata.cern.ch/cernopendata/modules/fixtures/data/records/cms-simulated-datasets-Run2011A.json
        - output_file: ~/cod//Users/data-curation/cms-2011-simulated-datasets/outputs/cms-simulated-datasets-Run2011A_new_methodology_format.json

        and then the changes were applied to original file with a script: ~/cod/data-curation/utils/update_fixtures.py
    """
    data = json.load(input_file)
    output = []
    for dataset in data:
        if 'methodology' in dataset and 'description' in dataset['methodology']:
            methodology = dataset['methodology']
            new_dataset = defaultdict(dict)
            new_dataset['recid'] = dataset['recid']
            new_dataset['title'] = dataset['title']
            new_dataset['methodology'] = convert_description_string_to_json(methodology)
            output.append(new_dataset)

    json.dump(output, output_file)
