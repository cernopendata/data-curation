#!/usr/bin/env python2

"""Classify CMS MC November 2015 datasets into topical categories."""

import re


def read_titles(filename='./inputs/cms-mc-nov-2015.txt'):
    """Read dataset titles from filename."""
    return [line.strip() for line in open(filename).readlines()]


def categorise_titles(titles):
    """Categorise titles."""
    categories = {
        'B-physics': [],
        'BSM Higgs': [],
        'SM Systematic Variations': [],
        'SM Higgs': [],
        'SM Exclusive': [],
        'SM Inclusive': [],
    }
    for title in titles:
        categories[guess_title_category(title)].append(title)
    return categories


def guess_title_category(title):
    """Guess category for the title."""
    title_lower = title.lower()

    if 'lambda' in title_lower or \
       'Bu' in title or \
       'Bd' in title or \
       'jpsi' in title_lower or \
       'upsilon' in title_lower:
        return 'B-physics'

    elif 'higgs2p' in title_lower or \
         'bsm' in title_lower or \
         'graviton2' in title_lower or \
         'higgs0' in title_lower:
        return 'BSM Higgs'

    elif 'matchingup' in title_lower or \
         'matchingdown' in title_lower or \
         'scaleup' in title_lower or \
         'scaledown' in title_lower or \
         re.search(r'tt_weights.*auet2', title_lower) or \
         '_mt' in title_lower or \
         '_mass' in title_lower:
        return 'SM Systematic Variations'

    elif 'higgs' in title_lower or \
         'hto' in title_lower or \
         '_hcontin' in title_lower or \
         '_smhcontin' in title_lower or \
         'h_m' in title_lower:
        return 'SM Higgs'

    elif 'HT' in title or \
         'Pt' in title or \
         'enriched' in title_lower or \
         re.search(r'[0-9]jet', title_lower):
        return 'SM Exclusive'

    return 'SM Inclusive'


def print_results(categories):
    """Print category statistics."""
    for category, titles in categories.iteritems():
        print "* %s (%d)" % (category, len(titles))
        titles.sort()
        for title in titles:
            print title


def main():
    """Do the main job."""
    print_results(categorise_titles(read_titles('./inputs/cms-mc-nov-2015.txt')))


if __name__ == '__main__':
    main()
