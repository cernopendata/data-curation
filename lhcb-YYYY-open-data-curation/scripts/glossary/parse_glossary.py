import json
import html2text 

gloss = []
i=0
with open("./loki.json", 'r') as origfile:
    origdict = json.load(origfile)

    for key in origdict.keys():

        if "<" or ">" in origdict[key]["documentation"].split("</p>")[0].removeprefix("<div class=\"memdoc\">\n<p>"):
            shortdef = ""
        else:
            shortdef = html2text.html2text(origdict[key]["documentation"].split("</p>")[0].removeprefix("<div class=\"memdoc\">\n<p>").strip())
            
        gloss.append({
            "anchor": f"{key}",
            "category": "generic",
            "definition" : origdict[key]["documentation"],
            "short_definition" : shortdef,
            "term" : [f"{key}"],
            "type": {
            "primary": "Glossary"
            }            
        },)
        i += 1
    
    print(i)
    with open("glossfromnwizz.json", "w") as f:
        json.dump(gloss, f, indent=2, sort_keys=True)
