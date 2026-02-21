from os import listdir
from os.path import isfile, join
import os
import json
import yaml 
import argparse

with open("../../config.yaml", "r") as f:
    conf = yaml.safe_load(f)

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", default=conf["release_dir"] + "stripping_pages/processed/")
parser.add_argument("--version")
parser.add_argument("--stream")
args = parser.parse_args()

def year_of_stripping(stripping_version):
    """
    Assign a year according to the stripping version. 
    """
    for key in conf["stripping_versions_year"]:
        if stripping_version in conf["stripping_versions_year"][key]:
            return key

jfile = [
    {
        "body": {
            "content": f"{args.version}-index.md",
            "format": "md"
        },
        "collections": [
            {
                "experiment": "LHCb"
            }
        ],
        "experiment": "LHCb",
        "date_created": [
            year_of_stripping(args.version)
        ],
        "short_description": {
            "content": " "
        },
        "stripping": {
            "version": args.version,
        },
        "slug": f"{args.version}-index",
        "tags": [
            f"{args.version}"
        ],
        "title": "LHCb Stripping " + "v" + args.version.removeprefix("stripping") + " Index",
        "type": {
            "primary": "Documentation",
            "secondary": [
                "Stripping"
            ]
        }
    }
]

if not os.path.exists(args.input_path + "/" + args.version):
    os.makedirs(args.input_path + "/" + args.version)

only_files = [f for f in listdir(args.input_path + "/" + args.version) if isfile(
join(args.input_path + "/" + args.version, f))]

with open(f"{args.input_path}" + "/" + f"{args.version}/" + f"{args.version}-index.json", "w") as f:
    json.dump(jfile, f, indent=2, sort_keys=True)        

### Create records for stripping lines in every  
only_files = [f for f in listdir(os.path.join(args.input_path, args.version, args.stream)) if 
            isfile(os.path.join(args.input_path, args.version, args.stream, f))]

for file in only_files:

    steam = args.stream.replace("_", "-")
    file  = file.replace("_", "-")

    if ".md" in file:
        jfile = [
            {
                "body": {
                    "content": file,
                    "format": "md"
                },
                "collections": [
                    {
                        "experiment": "LHCb"
                    }
                ],
                "experiment": "LHCb",
                "date_created": [
                    year_of_stripping(args.version)
                ],
                "short_description": {
                    "content": " "
                },
                "stripping": {
                    "version": args.version,
                    "stream":  args.stream
                },
                "slug": file.removesuffix(".md"),
                "tags": [
                    f"{args.stream.upper()}"
                ],
                # Create a title. Catch the edge cases where a line name has "line" in the name etc. 
                "title": "LHCb Stripping " + "V" + 
                args.version.removeprefix("stripping") + " " + 
                args.stream.upper() + " Stream " + 
                file.removesuffix(".md").removeprefix(args.version).removeprefix("-" + args.stream + "-").removesuffix("-line").removesuffix("line").upper() + " Line",
                "type": {
                    "primary": "Documentation",
                    "secondary": [
                        "Stripping"
                    ]
                }
            }
        ]

        with open(os.path.join(args.input_path, args.version, args.stream, file.removesuffix(".md").removesuffix(".html") + ".json"), "w") as f:
            json.dump(jfile, f, indent=2, sort_keys=True)
        print("Writing:" + f"{args.input_path}" +"/"+ f"{args.version}/{args.stream}/" + file.removesuffix(".md").removesuffix(".html") + ".json")