#!/usr/bin/env python


"""
Allocate reccord IDs for CMS 2012 open data release simulated datasets.

Some will be not used if they have not been transferred to EOS final
destination yet.
"""

RECID_START = 7200


def main():
    "Do the job."
    fdesc = open('./outputs/recid_info.py', 'w')
    fdesc.write('RECID_INFO = {\n')
    recid = RECID_START
    for line in open('./inputs/mc-datasets.txt', 'r').readlines():
        dataset_full_name = line.strip()
        fdesc.write("  '%s': %d,\n" % (dataset_full_name, recid))
        recid += 1
    fdesc.write('}\n')
    fdesc.close()


if __name__ == '__main__':
    main()
