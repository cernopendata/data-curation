from os import listdir
from os.path import isfile, join
import os
import json

from config import streams, stripping_versions_dirs, stripping_versions_years

directory = "/home/misarpis/Work/lhcb-opendata-curation/lhcb-runI/StrippingLines/Processed/"


def yearofstripping(strippingversion):
    for key in stripping_versions_years:
        if strippingversion in stripping_versions_years[key]:
            return key


for strippingversion in stripping_versions_dirs:

    for stream in streams:

        if os.path.exists(directory + "/" + strippingversion + "/" + stream.lower()):

            onlyfiles = [f for f in listdir(directory + "/" + strippingversion + "/" + stream.lower()) if isfile(
                join(directory + "/" + strippingversion + "/" + stream.lower(), f))]

            for file in onlyfiles:

                newstream = stream.replace("_", "-").lower()
                newfilename = file.replace("_", "-")

                if ".md" in file:
                    jfile = [
                        {
                            "body": {
                                "content": newfilename,
                                "format": "md"
                            },
                            "collections": [
                                {
                                    "experiment": "LHCb"
                                }
                            ],
                            "experiment": "LHCb",
                            "date_created": [
                                yearofstripping(strippingversion)
                            ],
                            "short_description": {
                                "content": " "
                            },
                            "stripping": {
                                "version": strippingversion,
                                "stream":  stream
                            },
                            "slug": newfilename.strip(".md"),
                            "tags": [
                                f"{stream}"
                            ],
                            "title": "LHCb Stripping " + "V" + newfilename.split("-")[0].split("stripping")[1] + " " + " ".join(newfilename.split("-")[1:]).strip(".md"),
                            "type": {
                                "primary": "Documentation",
                                "secondary": [
                                    "Stripping"
                                ]
                            }
                        }
                    ]

                    with open(f"{directory + strippingversion}/{newstream}/" + newfilename.strip(".md") + ".json", "w") as f:
                        json.dump(jfile, f, indent=2, sort_keys=True)

                if "_" in file:
                    os.system(
                        f"mv -u {directory + strippingversion}/{stream.lower()}/{file} {directory + strippingversion}/{newstream}/{newfilename}")
