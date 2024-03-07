import json
import numpy as np
import time
import regex as re

with open("./inputs/ComputingNotes.txt", "r") as f:
    datalist = f.read().split("\n\n")
namelist = datalist[0:-3]
authorlist = datalist[-3]
fileinfo = datalist[-1].split("\n")
authorlist = re.split(r'",\s*"', authorlist.strip("[]"))
datelist = datalist[-2].strip("[]").split(", ")
namelist, authorlist, datelist = np.array(
    sorted(list(zip(namelist, authorlist, datelist)))
).T
for item, i in zip(datelist, np.arange(0, len(datelist))):  # formatting the dates
    try:
        datelist[i] = item[0:2] + " " + item[2] + item[3]
        datelist[i] = datelist[i] + " " + item[4] + item[5]
        datelist[i] = time.strftime("%b %d %Y", time.strptime(datelist[i], "%d %m %y"))
    except IndexError:
        if len(datelist[i]) == 5:
            datelist[i] = time.strftime("%b %Y", time.strptime(datelist[i], "%m %y"))
        else:
            pass

cndict = []
recid = 26150
for name, authors, file, date in zip(namelist, authorlist, fileinfo, datelist):
    path, size, checksum = re.findall(r"=(\S*)", file)
    fields = list(filter(None, re.split(r"^(Note.\S*)\s", name)))
    entry = {
        "abstract": {"description": fields[1]},
        "accelerator": "DESY-PETRA",
        "collaboration": {"name": "JADE collaboration", "recid": "26050"},
        "collections": ["JADE-Computing-Notes"],
        "date_created": [date[-4:]],
        "date_published": "2024",
        "distribution": {"formats": ["pdf"], "number_files": 1, "size": int(size)},
        "experiment": ["JADE"],
        "files": [
            {
                "checksum": "adler32:" + checksum,
                "size": int(size),
                "uri": "root://eospublic.cern.ch/" + path,
            }
        ],
        "license": {"attribution": "CC0"},
        "publisher": "CERN Open Data Portal",
        "recid": str(recid),
        "title": "JADE Computing " + fields[0],
        "type": {"primary": "Supplementaries", "secondary": ["Computing Note"]},
    }
    if authors:
        formatauthor = []
        for author in authors.split(", "):
            formatauthor.append({"name": str(author)})
        entry["authors"] = formatauthor
    entry = dict(sorted(entry.items()))
    cndict.append(entry)
    recid += 1

with open("./outputs/jade-computing-notes.json", "w", encoding="utf-8") as f:
    json.dump(cndict, f, ensure_ascii=False, indent=2)
