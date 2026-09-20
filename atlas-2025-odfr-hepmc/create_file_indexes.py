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
    "test/atlas-hepmc-13tev-specialised-sm-z-boson.json",
    "test/atlas-hepmc-13tev-summary.json",
]:

    with open(AFIXTUREFILE, "r") as fdesc:
        records = json.loads(fdesc.read())

        for record in records:

            # fix relations
            if record["recid"] == "160000":  # summary record
                record["relations"].append({"recid": "160002", "type": "isParentOf"})
            elif record["recid"] == "160002":  # daugther record
                new_relations = []
                for arelation in record["relations"]:
                    if "doi" in arelation:
                        del arelation["doi"]
                        arelation["recid"] = "160000"
                    new_relations.append(arelation)
                record["relations"] = new_relations

            # fix the file information
            files_new = []
            for afile in record.get("files", []):
                afilename = afile["filename"]

                basename = os.path.basename(afilename)
                basename = basename.replace("_filelist.json", "")

                prefixes = []

                with open(f"test/{afilename}", "r") as fdr:
                    rootfileinfos = json.loads(fdr.read())

                    for rootfileinfo in rootfileinfos:
                        prefix = (
                            rootfileinfo["uri_root"].rsplit("/", 1)[0].rsplit("/", 1)[1]
                        )
                        if prefix not in prefixes:
                            prefixes.append(prefix)
                        del rootfileinfo["events"]
                        del rootfileinfo["type"]
                        rootfileinfo["uri"] = rootfileinfo["uri_root"].replace(
                            ":1094//eos/opendata", "//eos/opendata"
                        )
                        del rootfileinfo["uri_root"]

                if len(prefixes) > 1:
                    print(f"[ERROR] Several prefixes found: {prefixes}")
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
