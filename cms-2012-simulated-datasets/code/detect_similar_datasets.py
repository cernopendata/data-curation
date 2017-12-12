#!/usr/bin/env python3

"""
Detect similar datasets.

Useful to send to Kati to see which version we want to take for 2012 open data release.
"""


from create_dataset_records import get_dataset


def get_dataset_version_first_part(dataset):
    "Return version part of the dataset name."
    return dataset[0:dataset.rfind('-')]


def similar_datasets(func):
    "Return similar datasets based on FUNC based comparisons."
    datasets = {}
    for line in open('./inputs/mc-datasets.txt', 'r').readlines():
        dataset = line.strip()
        d = func(dataset)
        try:
            datasets[d].append(dataset)
        except KeyError:
            datasets[d] = [dataset, ]
    return datasets


def print_similar_datasets(datasets):
    "Print similar datasets found in the structure."
    for d in datasets.keys():
        if len(datasets[d]) > 1:
            print(d)
            for e in datasets[d]:
                print("   -", e)


def main():
    "Do the job."

    print('* Important list (version differences only)')
    print('')
    datasets = similar_datasets(get_dataset_version_first_part)
    print_similar_datasets(datasets)

    print('')
    print('')
    print('* Full list (for casual view)')
    print('')
    datasets = similar_datasets(get_dataset)
    print_similar_datasets(datasets)


if __name__ == '__main__':
    main()
