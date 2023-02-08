from os import listdir
from os.path import isfile, join
import os
import json

from config import streams, stripping_versions_dirs, stripping_versions_years, processeddir

directory = processeddir

def yearofstripping(strippingversion):
    for key in stripping_versions_years:
        if strippingversion in stripping_versions_years[key]:
            return key

for strippingversion in stripping_versions_dirs:

    ### Create a json for index page... 
    newfilename = f"{strippingversion}_index.md".replace("_", "-")

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
            },
            "slug": newfilename.removesuffix(".md"),
            "tags": [
                f"{strippingversion}"
            ],
            "title": "LHCb Stripping " + "V" + newfilename.split("-")[0].split("stripping")[1] + " Index",
            "type": {
                "primary": "Documentation",
                "secondary": [
                    "Stripping"
                ]
            }
        }
    ]

    onlyfiles = [f for f in listdir(directory + "/" + strippingversion) if isfile(
        join(directory + "/" + strippingversion, f))]
    
    ### If any _ in index filenames made it to here, this should replace them with - 
    for file in onlyfiles:
        if "_" in file:
            os.system(
                f"mv -u {directory + strippingversion}/{strippingversion}_index.md {directory + strippingversion}/{strippingversion}-index.md")

    with open(f"{directory + strippingversion}/" + newfilename.removesuffix(".md") + ".json", "w") as f:
        json.dump(jfile, f, indent=2, sort_keys=True)        

    ### Create records for stripping lines in every  
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
                            "slug": newfilename.removesuffix(".md"),
                            "tags": [
                                f"{stream}"
                            ],
                            "title": "LHCb Stripping " + "V" + newfilename.split("-")[0].split("stripping")[1] + " " + " ".join(newfilename.split("-")[1:]).removesuffix(".md"),
                            "type": {
                                "primary": "Documentation",
                                "secondary": [
                                    "Stripping"
                                ]
                            }
                        }
                    ]

                    with open(f"{directory + strippingversion}/{newstream}/" + newfilename.removesuffix(".md") + ".json", "w") as f:
                        json.dump(jfile, f, indent=2, sort_keys=True)

                if "_" in file:
                    os.system(
                        f"mv -u {directory + strippingversion}/{stream.lower()}/{file} {directory + strippingversion}/{newstream}/{newfilename}")