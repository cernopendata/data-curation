import datetime
from webbrowser import get 

AuthorsDict ={
    "authors": [],
    "collaboration": {
        "name": "LHCb collaboration"
    },
    "collections": [
        "Author-Lists"
    ],
    "date_created": [
        ""
    ],
    "date_published": str(datetime.datetime.now().year),
    "experiment": "LHCb",
    "publisher": "CERN Open Data Portal",
    "recid": "",
    "title": "",
    "type": {
        "primary": "Documentation",
        "secondary": [
            "Authors"
        ]
    }
}

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inputfile", required = True, help = "Input file lhcb authors list (xml)")

args = parser.parse_args()

with open(args.inputfile) as json_file:
    data = json.load(json_file)

### Parse institutes data, create a mapping {"ID" : "NameOfTheInstitute"}
institutes    = data["collaborationauthorlist"]["cal:organizations"]
InstitutesIndexDict = {}

for institute in range(len(institutes["foaf:Organization"])):
    if "cal:orgName" not in institutes["foaf:Organization"][institute].keys():
        InstitutesIndexDict[institutes["foaf:Organization"][institute]["@id"]] = institutes["foaf:Organization"][institute]["foaf:name"]
    else: 
        InstitutesIndexDict[institutes["foaf:Organization"][institute]["@id"]] = institutes["foaf:Organization"][institute]["cal:orgName"]["#text"]

### GetInstituteName          
def get_institute_name(organisationID):
    return InstitutesIndexDict[organisationID]

### GetINSPIREID
def get_INSPIRE_ID(Person):
    if "cal:authorids" not in data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person].keys():
        return ""
    if type(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"]) == list:     
        for item in range(len(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"])):
            for key in data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"][item].keys():
                if data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"][item]["@source"] == "INSPIRE":
                    return(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"][item]["#text"])
    else:
        if data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"]["@source"] == "INSPIRE":
            return(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorids"]["cal:authorid"]["#text"])

     
### Fill the Date Created

AuthorsDict["date_created"] = [data["collaborationauthorlist"]["cal:creationDate"].split("-")[-1]]

### Fill RECID 

if AuthorsDict["date_created"][0] == "2011":
    AuthorsDict["recid"] = "455"  
elif AuthorsDict["date_created"][0] == "2012":
    AuthorsDict["recid"] = "456"  
else: 
    "Don't have RECID for this year"

### Fill Title 

AuthorsDict["title"] = "LHCb author list for the LHCb " + AuthorsDict["date_created"][0] + " open data release"

### Fill Person specific fields 
for Person in range(len(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"])):
    FirstName      = data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["foaf:givenName"]
    LastName       = data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["foaf:familyName"]
    
    fullname      = LastName + ", " + FirstName
    
    if type(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorAffiliations"]["cal:authorAffiliation"]) == list: 
        affiliations = []
        
        for i in range(len(data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorAffiliations"]["cal:authorAffiliation"])):
            OrganisationID = data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorAffiliations"]["cal:authorAffiliation"][i]["@organizationid"]
            affiliations.append(get_institute_name(OrganisationID))
        affiliation = "; ".join(affiliations)
    else:
            OrganisationID = data["collaborationauthorlist"]["cal:authors"]["foaf:Person"][Person]["cal:authorAffiliations"]["cal:authorAffiliation"]["@organizationid"]
            affiliation    = get_institute_name(OrganisationID)
    
    inspireID = get_INSPIRE_ID(Person)
        
    if inspireID != "":        
        AuthorsDict["authors"].append({
                    "affiliation": f"{affiliation}",
                    "name"       : f"{fullname}",
                    "inspireid"  : f"{inspireID}",                
                })
    else: 
        AuthorsDict["authors"].append({
                    "affiliation": f"{affiliation}",
                    "name"       : f"{fullname}",
                })
        
with open("ODP_LHCb_Authors_" + data["collaborationauthorlist"]["cal:creationDate"].split("-")[-1] + ".json", "w") as f:
    f.write("[")    # Each JSON file must be a list 
    json.dump(AuthorsDict, f, indent=2, sort_keys=True)
    f.write("]")