#!/usr/bin/env python3

import json
import os
import sys
import zlib

os.makedirs("test/eos-file-indexes", exist_ok=True)
os.makedirs("test/records", exist_ok=True)


def get_file_size(afile):
    "Return file size of a file."
    return os.path.getsize(afile)


def get_file_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    checksum = zlib.adler32(open(afile, "rb").read(), 1) & 0xFFFFFFFF
    checksum = "{:#010x}".format(checksum).split("0x")[1]
    return checksum


for AFIXTUREFILE in [
    "test/atlas-hi-2024-hi-2015-data.json",
    "test/atlas-hi-2024-mc-hi-minbias.json",
    "test/atlas-hi-2024-summary.json",
]:

    with open(AFIXTUREFILE, "r") as fdesc:
        records = json.loads(fdesc.read())

        for record in records:

            # first, fix the license information
            record["license"]["attribution"] = "CC0"

            # second, fix the file information
            files_new = []
            for afile in record.get("files", []):
                afilename = afile["filename"]

                basename = os.path.basename(afilename)
                basename = basename.replace("_filelist.json", "")

                prefixes = []

                with open(f"test/{afilename}", "r") as fdr:
                    rootfileinfos = json.loads(fdr.read())

                    for rootfileinfo in rootfileinfos:
                        rootfileinfo["checksum"] = rootfileinfo["checksum"].replace(
                            "adler32", "adler32:"
                        )
                        prefix = rootfileinfo["filename"].split(":", 1)[0]
                        if prefix not in prefixes:
                            prefixes.append(prefix)
                        del rootfileinfo["events"]
                        del rootfileinfo["type"]
                        rootfileinfo["uri"] = rootfileinfo["uri_root"].replace(
                            ":1094//eos/opendata", "//eos/opendata"
                        )
                        del rootfileinfo["uri_root"]

                if len(prefixes) > 1:
                    print("[ERROR] Several prefixes found: {prefixes}")
                    sys.exit(1)

                prefix = prefixes[0]

                with open(
                    f"test/eos-file-indexes/{prefix}_{basename}_file_index.txt", "w"
                ) as fdw:
                    for rootfileinfo in rootfileinfos:
                        fdw.write(rootfileinfo["uri"] + "\n")

                with open(
                    f"test/eos-file-indexes/{prefix}_{basename}_file_index.json", "w"
                ) as fdw:
                    new_content = json.dumps(
                        rootfileinfos,
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=False,
                        separators=(",", ": "),
                    )
                    fdw.write(new_content + "\n")

                files_new.append(
                    {
                        "checksum": f"adler32:{get_file_checksum(f'test/eos-file-indexes/{prefix}_{basename}_file_index.json')}",
                        "size": get_file_size(
                            f"test/eos-file-indexes/{prefix}_{basename}_file_index.json"
                        ),
                        "type": "index.json",
                        "uri": f"root://eospublic.cern.ch//eos/opendata/atlas/rucio/{prefix}/file-indexes/{prefix}_{basename}_file_index.json",
                    }
                )
                files_new.append(
                    {
                        "checksum": f"adler32:{get_file_checksum(f'test/eos-file-indexes/{prefix}_{basename}_file_index.json')}",
                        "size": get_file_size(
                            f"test/eos-file-indexes/{prefix}_{basename}_file_index.json"
                        ),
                        "type": "index.txt",
                        "uri": f"root://eospublic.cern.ch//eos/opendata/atlas/rucio/{prefix}/file-indexes/{prefix}_{basename}_file_index.txt",
                    }
                )
                record["files"] = files_new

                # print EOS copy command statements
                print(f"eos mkdir -p /eos/opendata/atlas/rucio/{prefix}/file-indexes")
                print(
                    f"eos cp eos-file-indexes/{prefix}_{basename}_file_index.json /eos/opendata/atlas/rucio/{prefix}/file-indexes"
                )
                print(
                    f"eos cp eos-file-indexes/{prefix}_{basename}_file_index.txt /eos/opendata/atlas/rucio/{prefix}/file-indexes"
                )

        new_content = json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )

        with open(f"test/records/{os.path.basename(AFIXTUREFILE)}", "w") as fdesc:
            fdesc.write(new_content + "\n")
