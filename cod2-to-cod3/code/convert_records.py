#!/usr/bin/env python2

"""
Usage: convert_records.py somefile.xml
Usage: see ../run.sh
"""

import copy
import json
import os
import sys

from invenio.bibrecord import create_records, \
    field_get_subfield_values, \
    filter_field_instances, \
    record_get_field_instances, \
    record_get_field_value, \
    record_get_field_values


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

    # collaboration / 110
    collaboration_name = record_get_field_value(rec, tag="110", code="a")
    collaboration_group = record_get_field_value(rec, tag="110", code="g")
    collaboration_recid = record_get_field_value(rec, tag="110", code="w")
    if collaboration_name or collaboration_group or collaboration_recid:
        collaboration = {}
        if collaboration_name:
            collaboration['name'] = collaboration_name
        if collaboration_group:
            collaboration['group'] = collaboration_group
        if collaboration_recid:
            collaboration['recid'] = collaboration_recid
        jrec['collaboration'] = collaboration

    # title / 245
    title = record_get_field_value(rec, tag="245", code="a")
    if title:
        jrec['title'] = title

    # additional title / 246
    additional_title = record_get_field_value(rec, tag="246", code="a")
    if additional_title:
        jrec['additional_title'] = additional_title

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
    if title.endswith('/AOD'):
        formats.append('aod')
    if formats:
        distribution['formats'] = formats
    if distribution:
        jrec['distribution'] = distribution

    # collections / 980
    collections = record_get_field_values(rec, tag="980", code="a")
    collections.extend(record_get_field_values(rec, tag="980", code="b"))
    if 'Education' in collections:
        collections.remove('Education')
    if 'Research' in collections:
        collections.remove('Research')
    if collections:
        jrec['collections'] = collections

    # type, subtype / new
    if 'Primary-Dataset' in ' '.join(collections):
        maintype = 'Dataset'
        subtype = 'Collision Data'
    elif 'Validation-Utilities' in ' '.join(collections):
        maintype = 'Software'
        subtype = 'Validation'
    else:
        maintype = 'FIXME'
        subtype = 'FIXME'
    if maintype:
        jrec['type'] = maintype
    if subtype:
        jrec['subtype'] = subtype

    # system_details / 538
    system_details = {}
    system_details_release = record_get_field_value(rec, tag="538", code="a")
    if system_details_release:
        system_details['release'] = system_details_release
    system_details_global_tag = record_get_field_value(rec, tag="538", code="b")
    if system_details_global_tag:
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
            use_with_link = {}
            if field_instance_recids:
                use_with_link['recid'] = field_instance_recids[0]
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
                usage_link['url'] = field_instance_urls[0]
            if field_instance_descriptions:
                usage_link['description'] = field_instance_descriptions[0]
            if usage_link:
                if usage.has_key('links'):
                    usage['links'].append(usage_link)
                else:
                    usage['links'] = [usage_link, ]
        jrec['usage'] = usage

    # note / 787
    note_description = record_get_field_value(rec, tag="787", code="a")
    if note_description:
        note = {'description': note_description}
        jrec['note'] = note

    # documentation / 556
    documentation_description = record_get_field_value(rec, tag="556", code="a")
    if documentation_description:
        documentation = {'description': documentation_description}
        documentation_links = []
        for field_instance in record_get_field_instances(rec, tag="556"):
            field_instance_recids = field_get_subfield_values(field_instance, 'w')
            field_instance_urls = field_get_subfield_values(field_instance, 'u')
            field_instance_titles = field_get_subfield_values(field_instance, 'y')
            documentation_link = {}
            if field_instance_recids:
                documentation_link['recid'] = field_instance_recids[0]
            if field_instance_urls:
                documentation_link['url'] = field_instance_urls[0]
            if field_instance_urls:
                documentation_link['title'] = field_instance_titles[0]
            if documentation_link:
                if documentation.has_key('links'):
                    documentation['links'].append(documentation_link)
                else:
                    documentation['links'] = [documentation_link, ]
        jrec['documentation'] = documentation

    # accelerator / 693
    accelerator = record_get_field_value(rec, tag="693", code="a")
    if accelerator:
        jrec['accelerator'] = accelerator

    # experiment / 693
    experiment = record_get_field_value(rec, tag="693", code="e")
    if experiment:
        jrec['experiment'] = experiment

    # run_period / 964
    run_period = record_get_field_value(rec, tag="964", ind2="0", code="c")
    if run_period:
        jrec['run_period'] = run_period

    # generation
    # FIXME to be populated from DAS client

    # collision_information / 942
    collision_information_energy = record_get_field_value(rec, tag="942", code="e")
    collision_information_luminosity = record_get_field_value(rec, tag="942", code="l")
    collision_information_type = record_get_field_value(rec, tag="942", code="t")
    if collision_information_energy or collision_information_luminosity or collision_information_type:
        collision_information = {}
        if collision_information_energy:
            collision_information['energy'] = collision_information_energy
        if collision_information_luminosity:
            collision_information['luminosity'] = collision_information_luminosity
        if collision_information_type:
            collision_information['type'] = collision_information_type
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
            jrec['relations'].extend(parent_dataset)
        else:
            jrec['relations'] = [parent_dataset,]

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
        files.append(afile)
    if files:
        if jrec.has_key('files'):
            jrec['files'].extend(files)
        else:
            jrec['files'] = files

    # keywords / 653
    keywords = record_get_field_values(rec, tag="653", ind1="1", code="a")
    if keywords:
        if jrec.has_key('keywords'):
            jrec['keywords'].extend(keywords)
        else:
            jrec['keywords'] = keywords

    # files / FFT
    # FIXME need to put files onto EOS in respective directories

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
