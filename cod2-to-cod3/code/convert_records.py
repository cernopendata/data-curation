#!/usr/bin/env python2

"""
Usage: convert_records.py somefile.xml
Usage: see ../run.sh
"""

import copy
import datetime
import json
import re
import os
import sys
import time

from invenio.bibrecord import create_records, \
    field_get_subfield_values, \
    filter_field_instances, \
    record_get_field_instances, \
    record_get_field_value, \
    record_get_field_values


from fft_file_cache_info import fft_file_cache_info


def convert_record(rec):
    "Convert single REC record to JSON."

    jrec = {}

    # recid / 001
    recid = record_get_field_value(rec, tag="001")
    if recid:
        jrec['recid'] = record_get_field_value(rec, tag="001")

    # doi / 0247 $2 DOI
    dois = filter_field_instances(record_get_field_instances(rec, tag="024", ind1="7"),
                                  "2", "DOI")
    if dois:
        jrec['doi'] = field_get_subfield_values(dois[0], "a")[0]

    # CMS ConfDB ID / 035
    cmsconfdbids = filter_field_instances(record_get_field_instances(rec, tag="035"),
                                  "9", "CMS-ConfDB")
    if cmsconfdbids:
        jrec['cms_confdb_id'] = field_get_subfield_values(cmsconfdbids[0], "a")[0]

    # report number / 037

    # authors / 100, 700
    authors = []
    for field_instance in record_get_field_instances(rec, tag="100") + record_get_field_instances(rec, tag="700"):
        author = {}
        author_names = field_get_subfield_values(field_instance, "a")
        if author_names:
            author['name'] = author_names[0]
        author_ccids = field_get_subfield_values(field_instance, "h")
        if author_ccids:
            author['ccid'] = author_ccids[0]
        author_inspireids = field_get_subfield_values(field_instance, "i")
        if author_inspireids:
            author['inspireid'] = author_inspireids[0]
        author_affiliations = field_get_subfield_values(field_instance, "u")
        if author_affiliations:
            author['affiliation'] = author_affiliations[0]
        authors.append(author)
    if authors:
        jrec['authors'] = authors

    # collaboration / 110, 710
    collaboration_name = record_get_field_value(rec, tag="110", code="a")
    collaboration_name_additionals = record_get_field_values(rec, tag="710", code="a")
    collaboration_group = record_get_field_value(rec, tag="110", code="g")
    collaboration_recid = record_get_field_value(rec, tag="110", code="w")
    if collaboration_name or collaboration_group or collaboration_recid:
        collaboration = {}
        if collaboration_name:
            for collaboration_name_additional in collaboration_name_additionals:
                collaboration_name += ' and ' + collaboration_name_additional
            collaboration['name'] = collaboration_name
        if collaboration_group:
            collaboration['group'] = collaboration_group
        if collaboration_recid:
            collaboration['recid'] = collaboration_recid
        jrec['collaboration'] = collaboration

    # title / 245 $a
    title = record_get_field_value(rec, tag="245", code="a")
    if title:
        jrec['title'] = title

    # title subtitle / 245 $b
    title_subtitle = record_get_field_value(rec, tag="245", code="b")
    if title_subtitle:
        jrec['title_subtitle'] = title_subtitle

    # title additional / 246 $a
    title_additional = record_get_field_value(rec, tag="246", code="a")
    if title_additional:
        jrec['title_additional'] = title_additional

    # title additional subtitle / 246 $b
    title_additional_subtitle = record_get_field_value(rec, tag="246", code="b")
    if title_additional_subtitle:
        jrec['title_additional_subtitle'] = title_additional_subtitle

    # publisher / 260
    publisher = record_get_field_value(rec, tag="260", code="b")
    if publisher:
        jrec['publisher'] = publisher

    # date_published / 260
    date_published = record_get_field_value(rec, tag="260", code="c")
    if date_published:
        jrec['date_published'] = date_published

    # date_created, date_reprocessed / 264
    date_created = record_get_field_value(rec, tag="264", ind2="0", code="c")
    if date_created:
        jrec['date_created'] = date_created

    # date_reprocessed / 960
    date_reprocessed = record_get_field_value(rec, tag="960", code="c")
    if date_reprocessed:
        jrec['date_reprocessed'] = date_reprocessed

    # prepublication with reportnumber / 269, 037
    prepublication = {}
    for field_instance in record_get_field_instances(rec, tag="269"):
        prepublication_places = field_get_subfield_values(field_instance, "a")
        if prepublication_places:
            prepublication['place'] = prepublication_places[0]
        prepublication_publishers = field_get_subfield_values(field_instance, "b")
        if prepublication_publishers:
            prepublication['publisher'] = prepublication_publishers[0]
        prepublication_dates = field_get_subfield_values(field_instance, "c")
        if prepublication_dates:
            prepublication_time = time.strptime(prepublication_dates[0], "%d %b %Y")
            prepublication['date'] = time.strftime("%Y-%m-%d", prepublication_time)
        prepublication_reportnumber = record_get_field_value(rec, tag="037", code="a")
        if prepublication_reportnumber:
            prepublication['report_number'] = prepublication_reportnumber
    if prepublication:
        jrec['prepublication'] = prepublication

    # pileup / 770
    pileup = {}
    pileup_description = record_get_field_value(rec, tag="770", code="i")
    if pileup_description:
        pileup = {'description': pileup_description}
        pileup_links = []
        for field_instance in record_get_field_instances(rec, tag="770"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_titles = field_get_subfield_values(field_instance, 'a')
            pileup_link = {}
            if field_instance_recids:
                pileup_link['recid'] = field_instance_recids[0]
            if field_instance_titles:
                pileup_link['title'] = field_instance_titles[0]
            if pileup_link:
                if pileup.has_key('links'):
                    pileup['links'].append(pileup_link)
                else:
                    pileup['links'] = [pileup_link, ]
        jrec['pileup'] = pileup

    # extent / 300
    extent = record_get_field_value(rec, tag="300", code="a")
    if extent and False:  # we decided not to retain extent field in COD3
        jrec['extent'] = extent

    # dataset_semantics / 505
    dataset_semantics = []
    for field_instance in record_get_field_instances(rec, tag="505"):
        entry = {}
        entry_variables = field_get_subfield_values(field_instance, "t")
        if entry_variables:
            entry['variable'] = entry_variables[0]
        entry_descriptions = field_get_subfield_values(field_instance, "g")
        if entry_descriptions:
            entry['description'] = entry_descriptions[0]
        if dataset_semantics:
            dataset_semantics.append(entry)
        else:
            dataset_semantics = [entry, ]
    if dataset_semantics:
        jrec['dataset_semantics'] = dataset_semantics

    # collections / 980
    collections = record_get_field_values(rec, tag="980", code="a")
    collections.extend(record_get_field_values(rec, tag="980", code="b"))
    collections.extend(record_get_field_values(rec, tag="980", code="c"))
    if 'DELETED' in collections:
        return {} # record was deleted
    if 'Education' in collections:
        collections.remove('Education')
    if 'Research' in collections:
        collections.remove('Research')
    if collections:
        jrec['collections'] = collections

    # distribution / 256
    distribution = {}
    distribution_number_events = sum([int(x) for x in record_get_field_values(rec, tag="256", code="e")])
    if distribution_number_events:
        distribution['number_events'] = distribution_number_events
    distribution_number_files = sum([int(x) for x in record_get_field_values(rec, tag="256", code="f")])
    if distribution_number_files:
        distribution['number_files'] = distribution_number_files
    distribution_size = sum([int(x) for x in record_get_field_values(rec, tag="256", code="b")])
    if distribution_size:
        distribution['size'] = distribution_size
    formats = []
    if '.root' in ' '.join(record_get_field_values(rec, tag="856", ind1="7", code="u")):
        formats.append('root')
    if '/AOD/' in ' '.join(record_get_field_values(rec, tag="856", ind1="7", code="u")):
        formats.append('aod')
    if '/AODSIM/' in ' '.join(record_get_field_values(rec, tag="856", ind1="7", code="u")):
        formats.append('aodsim')
    if '/RAW/' in ' '.join(record_get_field_values(rec, tag="856", ind1="7", code="u")):
        formats.append('raw')
    if 'OPERA' in ' '.join(collections):
        formats.append('csv')
    fft_extensions = []
    for fft in record_get_field_values(rec, tag="FFT", code="a"):
        fft_basename, fft_extension = os.path.splitext(fft)
        if 'file-indexes' in fft_basename:
            continue
        if fft_extension == '.configFile':
            fft_extension = '.py'
        if fft_extension not in fft_extensions:
            fft_extensions.append(fft_extension[1:])
    for fft_extension in fft_extensions:
        if fft_extension:
            if not fft_extension in formats:
                formats.append(fft_extension)
    if formats:
        distribution['formats'] = formats
    if distribution:
        jrec['distribution'] = distribution

    # system_details / 538
    system_details = {}
    system_details_release = record_get_field_value(rec, tag="538", code="a")
    if system_details_release:
        system_details_release = system_details_release.replace('Recommended release for analysis: ', '')
        system_details_release = system_details_release.replace('Recommended Software Release: ', '')
        system_details_release = system_details_release.replace('Software release: ', '')
        system_details_release = system_details_release.replace('Release: ', '')
        system_details['release'] = system_details_release
    system_details_global_tag = record_get_field_value(rec, tag="538", code="b")
    if system_details_global_tag:
        system_details_global_tag = system_details_global_tag.replace('Global tag: ', '')
        system_details['global_tag'] = system_details_global_tag
    system_details_description = record_get_field_value(rec, tag="538", code="i")
    if system_details_description:
        system_details['description'] = system_details_description
    system_details_url = record_get_field_value(rec, tag="538", code="u")
    if system_details_url:
        system_details['url'] = system_details_url
    system_details_recid = record_get_field_value(rec, tag="538", code="w")
    if system_details_recid:
        system_details['recid'] = system_details_recid
    if system_details:
        jrec['system_details'] = system_details

    # abstract / 520
    abstract_description = record_get_field_value(rec, tag="520", code="a")
    if abstract_description:
        abstract = {'description': abstract_description}
        abstract_links = []
        for field_instance in record_get_field_instances(rec, tag="520"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            abstract_link = {}
            if field_instance_recids:
                abstract_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                abstract_link['url'] = field_instance_urls[0]
            if abstract_link:
                if abstract.has_key('links'):
                    abstract['links'].append(abstract_link)
                else:
                    abstract['links'] = [abstract_link, ]
        jrec['abstract'] = abstract

    # methodology / 567
    methodology_description = record_get_field_value(rec, tag="567", code="a")
    if methodology_description:
        methodology = {'description': methodology_description}
        methodology_links = []
        for field_instance in record_get_field_instances(rec, tag="567"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            methodology_link = {}
            if field_instance_recids:
                methodology_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                methodology_link['url'] = field_instance_urls[0]
            if methodology_link:
                if methodology.has_key('links'):
                    methodology['links'].append(methodology_link)
                else:
                    methodology['links'] = [methodology_link, ]
        jrec['methodology'] = methodology

    # license / 540
    license_attribution = record_get_field_value(rec, tag="540", code="a")
    if license_attribution:
        license = {'attribution': license_attribution}
        jrec['license'] = license

    # validation / 583
    validation_description = record_get_field_value(rec, tag="583", code="a")
    if validation_description:
        validation = {'description': validation_description}
        validation_links = []
        for field_instance in record_get_field_instances(rec, tag="583"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            field_instance_descriptions = field_get_subfield_values(field_instance, 'y')
            validation_link = {}
            if field_instance_recids:
                validation_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                validation_link['url'] = field_instance_urls[0]
            if field_instance_descriptions:
                validation_link['description'] = field_instance_descriptions[0]
            if validation_link:
                if validation.has_key('links'):
                    validation['links'].append(validation_link)
                else:
                    validation['links'] = [validation_link, ]
        jrec['validation'] = validation

    # use_with / 516
    use_with_description = record_get_field_value(rec, tag="516", code="a")
    if use_with_description:
        use_with = {'description': use_with_description}
        use_with_links = []
        for field_instance in record_get_field_instances(rec, tag="516"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            field_instance_descriptions = field_get_subfield_values(field_instance, 'y')
            # workaround for one record:
            if not field_instance_recids and field_instance_urls and \
               field_instance_urls[0] == 'http://opendata.cern.ch/record/14':
                field_instance_recids = ["14", ]
            for field_instance_recid in field_instance_recids:
                use_with_link = {}
                use_with_link['recid'] = field_instance_recid
                if field_instance_urls:
                    use_with_link['url'] = field_instance_urls[0]
                if field_instance_descriptions:
                    use_with_link['description'] = field_instance_descriptions[0]
                if use_with_link:
                    if use_with.has_key('links'):
                        use_with['links'].append(use_with_link)
                    else:
                        use_with['links'] = [use_with_link, ]
        jrec['use_with'] = use_with

    # usage / 581
    usage_description = record_get_field_value(rec, tag="581", code="a")
    if usage_description:
        usage = {'description': usage_description}
        usage_links = []
        for field_instance in record_get_field_instances(rec, tag="581"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            field_instance_descriptions = field_get_subfield_values(field_instance, 'y')
            usage_link = {}
            if field_instance_recids:
                usage_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                field_instance_url = field_instance_urls[0]
                if field_instance_url.startswith('http://atlas-opendata.web.cern.ch/atlas-opendata/'):
                    field_instance_url = field_instance_url.replace('http://atlas-opendata.web.cern.ch/atlas-opendata/', 'http://opendata.atlas.cern/')
                usage_link['url'] = field_instance_url
            if field_instance_descriptions:
                usage_link['description'] = field_instance_descriptions[0]
            if usage_link:
                if usage.has_key('links'):
                    usage['links'].append(usage_link)
                else:
                    usage['links'] = [usage_link, ]
        jrec['usage'] = usage

    # note / 556
    note_description = record_get_field_value(rec, tag="556", code="a")
    if note_description:
        note = {'description': note_description}
        note_links = []
        for field_instance in record_get_field_instances(rec, tag="556"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            field_instance_titles = field_get_subfield_values(field_instance, 'y')
            note_link = {}
            if field_instance_recids:
                note_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                note_link['url'] = field_instance_urls[0]
            if field_instance_urls:
                note_link['title'] = field_instance_titles[0]
            if note_link:
                if note.has_key('links'):
                    note['links'].append(note_link)
                else:
                    note['links'] = [note_link, ]
        jrec['note'] = note

    # note / 500
    comment = record_get_field_value(rec, tag="500", code="a")
    if comment:
        if jrec.has_key('note'):
            raise StandardError('Sorry, cannot have both note/556 and note/500 fields.')
        else:
            jrec['note'] = {'description': comment}

    # generator / 593
    generator = {}
    generator_name = record_get_field_value(rec, tag="593", code="a")
    if generator_name:
        generator_name = generator_name.replace('Generators: ', '')
        generator_names = generator_name.split()
        generator['names'] = generator_names
    generator_global_tag = record_get_field_value(rec, tag="593", code="b")
    if generator_global_tag:
        generator_global_tag = generator_global_tag.replace('Global tag: ', '')
        generator['global_tag'] = generator_global_tag
    if generator:
        jrec['generator'] = generator

    # accelerator / 693
    accelerator = record_get_field_value(rec, tag="693", code="a")
    if accelerator:
        jrec['accelerator'] = accelerator

    # experiment / 693
    experiment = record_get_field_value(rec, tag="693", code="e")
    if not experiment and (recid == '60' or recid == '352'):
        experiment = 'ATLAS'
    if experiment:
        jrec['experiment'] = experiment

    # run_period / 964
    run_period = record_get_field_value(rec, tag="964", ind2="0", code="c")
    if run_period:
        jrec['run_period'] = run_period

    # generation / for simulated data
    # FIXME to be populated from DAS client? introduce structure inside methodology field

    # selection / for collision data
    # FIXME to be populated from DAS client? introduce structure inside methodology field

    # collision_information / 942
    collision_information_energy = record_get_field_value(rec, tag="942", code="e")
    collision_information_luminosity = record_get_field_value(rec, tag="942", code="l")
    collision_information_type = record_get_field_value(rec, tag="942", code="t")
    if collision_information_energy or collision_information_luminosity or collision_information_type:
        collision_information = {}
        if collision_information_energy:
            collision_information_energy = collision_information_energy.replace('Collision energy: ', '')
            collision_information_energy = collision_information_energy.replace('Collision energy:', '')
            collision_information['energy'] = collision_information_energy
        if collision_information_luminosity:
            collision_information['luminosity'] = collision_information_luminosity
        if collision_information_type:
            collision_information['type'] = collision_information_type
        else:
            if 'Data' in ' '.join(collections):
                if 'PbPb' in title:
                    collision_information['type'] = 'PbPb'
                else:
                    collision_information['type'] = 'pp'
        jrec['collision_information'] = collision_information

    # parent_dataset / 772
    parent_dataset_title = record_get_field_value(rec, tag="772", code="a")
    parent_dataset_doi = record_get_field_value(rec, tag="772", code="o")
    parent_dataset_recid = record_get_field_value(rec, tag="772", code="w")
    if parent_dataset_title or parent_dataset_doi or parent_dataset_recid:
        parent_dataset = {}
        parent_dataset['type'] = 'isChildOf'
        if parent_dataset_title:
            parent_dataset['title'] = parent_dataset_title
        if parent_dataset_doi:
            parent_dataset['doi'] = parent_dataset_doi
        if parent_dataset_recid:
            parent_dataset['recid'] = parent_dataset_recid
        if jrec.has_key('relations'):
            jrec['relations'].append(parent_dataset)
        else:
            jrec['relations'] = [parent_dataset, ]

    # code to produce files / 777
    code_to_produce_files_description = record_get_field_value(rec, tag="777", code="a")
    code_to_produce_files_recid = record_get_field_value(rec, tag="777", code="w")
    if code_to_produce_files_description or code_to_produce_files_recid:
        code_to_produce_files = {}
        code_to_produce_files['type'] = 'isProducedBy'
        if code_to_produce_files_description:
            code_to_produce_files['description'] = code_to_produce_files_description
        if code_to_produce_files_recid:
            code_to_produce_files['recid'] = code_to_produce_files_recid
        if jrec.has_key('relations'):
            jrec['relations'].append(code_to_produce_files)
        else:
            jrec['relations'] = [code_to_produce_files, ]

    # related dataset / 786
    for field_instance in record_get_field_instances(rec, tag="786"):
        related_dataset_descriptions = field_get_subfield_values(field_instance, "a")
        related_dataset_recids = field_get_subfield_values(field_instance, "w")
        if related_dataset_descriptions or related_dataset_recids:
            related_dataset = {}
            related_dataset['type'] = 'isPartOf'
            if related_dataset_descriptions:
                related_dataset['description'] = related_dataset_descriptions[0]
            if related_dataset_recids:
                related_dataset['recid'] = related_dataset_recids[0]
            if jrec.has_key('relations'):
                jrec['relations'].append(related_dataset)
            else:
                jrec['relations'] = [related_dataset, ]

    # related item / 787
    related_item_description = record_get_field_value(rec, tag="787", code="a")
    related_item_recids = record_get_field_values(rec, tag="787", code="w")
    related_item_note = record_get_field_value(rec, tag="787", code="n")
    related_item_url = record_get_field_value(rec, tag="787", code="u")
    related_item_label = record_get_field_value(rec, tag="787", code="y")
    if related_item_description and not related_item_recids:
        # workaround for a record
        if related_item_description == 'The default output of the code below is a ROOT file Mu00val.root':
            note = related_item_description
            if jrec.has_key('note') and jrec['note'].has_key('description'):
                jrec['note']['description'] += note
            else:
                jrec['note'] = {'description': note}
    if related_item_recids:
        for related_item_recid in related_item_recids:
            related_item = {}
            related_item['type'] = 'isRelatedTo'
            if related_item_description:
                related_item['description'] = related_item_description
            if related_item_recid:
                related_item['recid'] = related_item_recid
            if jrec.has_key('relations'):
                jrec['relations'].append(related_item)
            else:
                jrec['relations'] = [related_item, ]
    if related_item_url:
        link = {}
        if related_item_note:
            link['description'] = related_item_note
        if related_item_url:
            link['url'] = related_item_url
        if related_item_label:
            if related_item_label != related_item_url:
                link['comment'] = related_item_label
        if jrec.has_key('links'):
            jrec['links'].append(link)
        else:
            jrec['links'] = [link, ]

    # files / 8567
    files = []
    for file_instance in record_get_field_instances(rec, tag="856", ind1="7"):
        afile = {}
        file_type = field_get_subfield_values(file_instance, "2")[0]
        afile['type'] = file_type
        file_uri = field_get_subfield_values(file_instance, "u")[0]
        afile['uri'] = file_uri
        file_size = field_get_subfield_values(file_instance, "s")[0]
        afile['size'] = int(file_size)
        afile['checksum'] = 'sha1:0000000000000000000000000000000000000000'  # FIXME detect real SHA1 of files
        files.append(afile)
    if files:
        if jrec.has_key('files'):
            jrec['files'].extend(files)
        else:
            jrec['files'] = files

    # files / FFT
    files = []
    for file_instance in record_get_field_instances(rec, tag="FFT"):

        # read FFT file properties
        file_name = field_get_subfield_values(file_instance, "a")[0]
        file_name = os.path.basename(file_name)
        try:
            file_name_alias = field_get_subfield_values(file_instance, "n")[0]
            file_name_alias = re.sub(r'^(.*?)\.', file_name_alias + '.', file_name)
        except IndexError:
            file_name_alias = ''
        file_descriptions = field_get_subfield_values(file_instance, "z")
        if file_descriptions:
            file_description = file_descriptions[0]
        else:
            file_description = ''

        #  output location that will be populated below
        file_uri = ''
        file_type = 'xrootd'

        # CMS-Primary-Datasets, CMS-Simulated-Datasets
        if 'CMS-Primary-Datasets' in collections or \
           'CMS-Simulated-Datasets' in collections:
            match = re.search(r'(.*?)_(.*?)_(.*)_(AOD|RAW)_(.*)_([0-9]+)_file_index.txt$', file_name)
            if match:
                file_type = 'index'
                file_experiment, file_release, file_dataset, file_format, file_version, file_volume = match.groups()
                file_uri = 'root://eospublic.cern.ch//eos/opendata/' + \
                        file_experiment.lower() + '/' + \
                        file_release + '/' + \
                        file_dataset + '/' + \
                        file_format + '/' + \
                        file_version + '/' + \
                        'file-indexes/' + file_name
            else:
                match = re.search(r'(.*?)_(MonteCarlo[0-9]+)_(.*?)_(.*)_(AODSIM)_(.*)_([0-9]+)_file_index.txt$', file_name)
                if match:
                    file_type = 'index'
                    file_experiment, file_montecarlo, file_release, file_dataset, file_format, file_version, file_volume = match.groups()
                    file_uri = 'root://eospublic.cern.ch//eos/opendata/' + \
                            file_experiment.lower() + '/' + \
                            file_montecarlo + '/' + \
                            file_release + '/' + \
                            file_dataset + '/' + \
                            file_format + '/' + \
                            file_version + '/' + \
                            'file-indexes/' + file_name

        # cms-eventdisplay-files
        if int(recid) >= 600 and int(recid) <= 613:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/' + os.path.splitext(file_name)[0] + '/IG/Apr21ReReco-v1/' + file_name

        # cms-eventdisplay-files-Run2011A
        if int(recid) >= 614 and int(recid) <= 632:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/' + os.path.splitext(file_name)[0].replace('_Run2011A', '') + '/IG/12Oct2013-v1/' + file_name.replace('_Run2011A', '')

        # CMS-Configuration-Files
        if 'CMS-Configuration-Files' in collections:
            if file_name.endswith('configFile'):
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/configuration-files/2011/' + file_name + '.py'
            else:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/configuration-files/2011/' + file_name

        # LHCb-Derived-Datasets
        if 'LHCb-Derived-Datasets' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/lhcb/MasterclassDatasets/D0lifetime/2014/file-indexes/' + file_name
            file_type = 'index'

        # ALICE-Derived-Datasets
        if 'ALICE-Derived-Datasets' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/alice/' + file_name
            file_type = 'index'

        # ALICE-Reconstructed-Data
        if 'ALICE-Reconstructed-Data' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/alice/' + file_name
            file_type = 'index'

        # CMS-Validated-Runs
        if 'CMS-Validated-Runs' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/validated-runs/' + date_created + '/' + file_name

        # cms-derived-csv-Run2011A
        if int(recid) == 545:
            match = re.search(r'^(.*)_(.*)_Run2011A.csv$', file_name)
            file_name_filename, file_name_dataset = match.groups()
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/' + file_name_dataset + '/CSV/12Oct2013-v1/' + file_name_filename + '.csv'

        # cms-tools-vm-image.xml
        if int(recid) >= 249 and int(recid) <= 250:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/environment/2010/' + file_name

        # cms-tools-vm-image-Run2011A.xml
        if int(recid) >= 251 and int(recid) <= 252:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/environment/2011/' + file_name

        # CMS-Open-Data-Instructions
        if 'CMS-Open-Data-Instructions' in collections:
            if int(recid) == 55:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/documentation/outreach-exercise-2010/' + file_name
            if int(recid) == 72:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/documentation/hst-programme-2016/' + file_name

        # CMS-Luminosity-Information
        if 'CMS-Luminosity-Information' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/luminosity/' + date_created + '/' + file_name

        # CMS-Trigger-Information
        if 'CMS-Trigger-Information' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/trigger-information/' + date_created + '/' + file_name

        # cms-derived-pattuples-ana
        if int(recid) == 201:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/file-indexes/' + file_name
            file_type = 'index'
        if int(recid) == 202:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/file-indexes/' + file_name
            file_type = 'index'

        # cms-derived-pattuples-ana-Run2011A
        if int(recid) == 230:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/file-indexes/' + file_name
            file_type = 'index'
        if int(recid) == 231:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/file-indexes/' + file_name
            file_type = 'index'

        # cms-hamburg-files
        if int(recid) >= 203 and int(recid) <= 212:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/hep-tutorial-2012/' + file_name

        # CMS-Learning-Resources
        if 'CMS-Learning-Resources' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/hep-tutorial-2012/' + file_name

        # cms-tools-ana
        if int(recid) == 101:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/ayrodrig-OutreachExercise2010/' + file_name
        if int(recid) == 200:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/ayrodrig-pattuples2010/' + file_name

        # cms-tools-dimuon-spectrum-2010
        if int(recid) == 560:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/dimuon-spectrum-2010/' + file_name

        # cms-tools-dimuon-filter
        if int(recid) == 553:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/SUSYBSMAnalysis-RazorFilter/' + file_name
        if int(recid) == 552:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/dimuon-filter/' + file_name

        # cms-validation-code-Run2010B
        if int(recid) == 460:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/validation-2010-Mu/' + file_name
        if int(recid) == 461:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/validation-2010-Commissioning/' + file_name
        if int(recid) == 462:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/software/validation-2010-MinimumBias/' + file_name

        # cms-csv-files
        if int(recid) == 554:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MultiJet/CSV/Apr21ReReco-v1/' + file_name_alias
        if int(recid) == 700:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/CSV/Apr21ReReco-v1/' + file_name_alias

        # cms-masterclass-files
        if int(recid) >= 300 and int(recid) <= 310:
            if file_name_alias.startswith('masterclass.'):
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/masterclass-2014/' + file_name
            else:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/masterclass-2014/' + file_name_alias

        # atlas-derived-datasets
        if 'ATLAS-Derived-Datasets' in collections:
            if int(recid) == 3860:
                # atlas-all-samples
                file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2016-07-29/file-indexes/' + file_name
                file_type = 'index'
            elif int(recid) == 390 or int(recid) == 391:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2016-07-29/file-indexes/' + file_name
                file_type = 'index'
            else:
                match = re.search(r'ATLAS_MasterclassDatasets_(.*)_([0-9]+)_dataset_([0-9]+)_file_index.txt$', file_name)
                file_xpath, file_year, file_number = match.groups()
                file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/MasterclassDatasets/' + file_xpath + '/' + file_year + '/' + file_number + '/file-indexes/' + file_name
                file_type = 'index'

        # ATLAS-Tools
        if 'ATLAS-Tools' in collections:
            if int(recid) == 352:
                file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/MasterclassDatasets/WPath/2015/Software/' + file_name
                file_type = 'index'
            else:
                file_type = 'index'
                if int(recid) == 3851:
                    file_name = file_name.replace('size_M_', 'size_S_')
                file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2016-07-29/file-indexes/' + file_name
                file_type = 'index'

        # ATLAS-Simulated-Datasets
        if 'ATLAS-Simulated-Datasets' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2016-07-29/file-indexes/' + file_name
            file_type = 'index'

        # ATLAS-Higgs-Challenge-2014
        if 'ATLAS-Higgs-Challenge-2014' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/atlas/higgs-challenge-2014/' + file_name

        # ALICE-Learning-Resources
        if 'ALICE-Learning-Resources' in collections:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/alice/documentation/' + file_name

        # cms-condition-data-Run2011A
        if int(recid) >= 1801 and int(recid) <= 1802:
            file_uri = 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/db/file-indexes/' + file_name
            file_type = 'index'

        # OPERA
        if 'OPERA' in ' '.join(collections):
            match = re.search(r'^(.*).(csv|zip)$', file_name)
            if match:
                file_name_base, file_name_ext = match.groups()
                if file_name_ext == 'zip':
                    file_uri_base = 'root://eospublic.cern.ch//eos/opendata/opera/datasets/multiplicity'
                elif file_name_ext == 'csv':
                    file_uri_base = 'root://eospublic.cern.ch//eos/opendata/opera/events/multiplicity'
                else:
                    raise StandardError('Not expected.')
                file_uri = file_uri_base + '/' + file_name_base + '.' + file_name_ext

        # author lists
        if 'Author-Lists' in collections:
            match = re.search(r'^(.*)-author-list-(.*).pdf$', file_name)
            if match:
                file_name_exp, file_name_year = match.groups()
                file_uri = 'root://eospublic.cern.ch//eos/opendata/' + file_name_exp.lower() + '/documentation/' + file_name

        # data policies
        if 'Data-Policies' in collections:
            match = re.search(r'^(.*)-Data-Policy.pdf$', file_name)
            if match:
                file_name_exp, = match.groups()
                file_uri = 'root://eospublic.cern.ch//eos/opendata/' + file_name_exp.lower() + '/documentation/' + file_name

        # ok, recognised enough; now generate files output
        if file_uri:
            afile = {}
            afile['type'] = file_type
            afile['uri'] = file_uri
            afile['size'] = fft_file_cache_info[file_name]['size']
            if file_description:
                afile['description'] = file_description
            afile['checksum'] = 'sha1:' + fft_file_cache_info[file_name]['checksum']
            files.append(afile)
    if files:
        if jrec.has_key('files'):
            jrec['files'].extend(files)
        else:
            jrec['files'] = files

    # keywords / 653
    keywords = record_get_field_values(rec, tag="653", ind1="1", code="a")
    keywords = [keyword.lower() for keyword in keywords if keyword != experiment]
    if keywords:
        if jrec.has_key('keywords'):
            jrec['keywords'].extend(keywords)
        else:
            jrec['keywords'] = keywords

    # topic / 655
    topic = {}
    for field_instance in record_get_field_instances(rec, tag="655", ind2="7"):
        topic_categories = field_get_subfield_values(field_instance, "a")
        if topic_categories:
            topic['category'] = topic_categories[0]
        topic_sources = field_get_subfield_values(field_instance, "9")
        if topic_sources:
            topic['source'] = topic_sources[0]
    if topic:
        jrec['topic'] = topic

    # language / 041
    language = record_get_field_value(rec, tag="041", code="a")
    if language:
        if language == 'eng':
            language = 'English'
        jrec['language'] = language

    # links / 8564
    links = []
    for file_instance in record_get_field_instances(rec, tag="856", ind1="4"):
        link = {}
        link_hostname = field_get_subfield_values(file_instance, "a")
        if link_hostname:
            link['hostname'] = link_hostname[0]
        link_compression_information = field_get_subfield_values(file_instance, "c")
        if link_compression_information:
            link['compression_information'] = link_compression_information[0]
        link_size = field_get_subfield_values(file_instance, "s")
        if link_size:
            link['size'] = link_size[0]
        link_url = field_get_subfield_values(file_instance, "u")
        if link_url:
            link['url'] = link_url[0]
        link_description = field_get_subfield_values(file_instance, "y")
        if link_description:
            link['description'] = link_description[0]
        link_comment = field_get_subfield_values(file_instance, "z")
        if link_comment:
            link['comment'] = link_comment[0]
        links.append(link)
    if links:
        if jrec.has_key('links'):
            jrec['links'].extend(links)
        else:
            jrec['links'] = links

    # type, subtype / new
    jrec['type'] = {}
    if 'Primary-Dataset' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Collision', ]
    elif '-Detector-Datasets' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Derived', ]
    elif '-Detector-Events' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Derived', ]
    elif 'Derived-Dataset' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Derived', ]
    elif 'Reconstructed-Data' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Collision', ]
    elif 'Simulated-Dataset' in ' '.join(collections):
        jrec['type']['primary'] = 'Dataset'
        jrec['type']['secondary'] = ['Simulated', ]
    elif 'Tools' in ' '.join(collections):
        if 'virtual machine' in abstract_description.lower():
            jrec['type']['primary'] = 'Environment'
            jrec['type']['secondary'] = ['VM']
        else:
            jrec['type']['primary'] = 'Software'
            jrec['type']['secondary'] = []
    elif 'Validation-Utilities' in ' '.join(collections):
        jrec['type']['primary'] = 'Software'
        jrec['type']['secondary'] = ['Validation', ]
    elif 'Learning-Resources' in ' '.join(collections):
        jrec['type']['primary'] = 'Documentation'
        jrec['type']['secondary'] = []
    elif 'Configuration-Files' in ' '.join(collections):
        jrec['type']['primary'] = 'Supplementaries'
        jrec['type']['secondary'] = ['Configuration', ]
    elif 'Trigger-Information' in ' '.join(collections):
        jrec['type']['primary'] = 'Supplementaries'
        jrec['type']['secondary'] = ['Trigger', ]
    elif 'Luminosity-Information' in ' '.join(collections):
        jrec['type']['primary'] = 'Supplementaries'
        jrec['type']['secondary'] = ['Luminosity', ]
    elif 'Condition-Data' in ' '.join(collections):
        jrec['type']['primary'] = 'Environment'
        jrec['type']['secondary'] = ['Condition', ]
    elif 'Open-Data-Instructions' in ' '.join(collections):
        jrec['type']['primary'] = 'Documentation'
        jrec['type']['secondary'] = []
    elif 'Data-Policies' in ' '.join(collections):
        jrec['type']['primary'] = 'Documentation'
        jrec['type']['secondary'] = []
    elif 'Author-Lists' in ' '.join(collections):
        jrec['type']['primary'] = 'Documentation'
        jrec['type']['secondary'] = []
    elif 'ATLAS-Higgs-Challenge-2014' in ' '.join(collections):
        if 'Dataset' in title:
            jrec['type']['primary'] = 'Dataset'
            jrec['type']['secondary'] = ['Derived']
        elif 'Documentation' in title:
            jrec['type']['primary'] = 'Documentation'
            jrec['type']['secondary'] = []
        elif 'Video' in title:
            jrec['type']['primary'] = 'Documentation'
            jrec['type']['secondary'] = []
        elif 'Software' in title:
            jrec['type']['primary'] = 'Software'
            jrec['type']['secondary'] = ['Analysis']
        else:
            jrec['type']['primary'] = 'FIXME'
            jrec['type']['secondary'] = []
    else:
        jrec['type']['primary'] = 'FIXME'
        jrec['type']['secondary'] = ['FIXME', ]

    return jrec


def convert_records(marcxml):
    "Convert list of MARCXML records to JSON."
    records = create_records(marcxml)
    print '['
    for (idx, (rec, status, error)) in enumerate(records):
        jrec = convert_record(rec)
        print json.dumps(jrec, indent=2, sort_keys=True)
        if idx == len(records) - 1:
            pass
        else:
            print ','
    print ']'


def main():
    "Do the job."
    marcxml = open(sys.argv[1], 'r').read()
    convert_records(marcxml)


if __name__ == '__main__':
    main()
