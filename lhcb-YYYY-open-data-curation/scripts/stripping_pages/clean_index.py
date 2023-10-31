import argparse
import yaml 
from bs4 import BeautifulSoup
import re

parser = argparse.ArgumentParser()
parser.add_argument("--inputfile",  help = "index.html")
parser.add_argument("--outputfile", help = "newindex.html")

args = parser.parse_args()

with open("../../config.yaml", "r") as f:
    conf = yaml.safe_load(f)

# Get all streams from config.yaml, transform the strings to how they appear in index.html and add commonparticles, stdbasic and stdintermediate 
if conf["stream"] != None: 
    streams = [x.split(".")[0].lower() for x in conf["stream"]] + ["commonparticles", "stdbasic", "stdintermediate"]
else: 
    streams = ["commonparticles", "stdbasic", "stdintermediate"]

with open(args.inputfile) as infile :
    soup = BeautifulSoup(infile,"html.parser")

# Remove the html header
for tag in soup.find_all("head"):
    soup.head.extract() 

# Remove the links to stripping project homepage 
for ancor2 in soup.find_all("a",href=re.compile(f"http")) :
    soup.a.decompose() 

# Remove tes location and production factor (not needed for open data)
for tr in soup.find_all("tr"):
    for td in tr.find_all("td")[1:]:
        td.extract()

# If releasing a subset of streams, remove the headers for other ones
for h2 in soup.find_all("h2"):
    for a in h2.find_all("a"):
        if a.get("name") not in streams:
            h2.extract()

# If releasing a subset of streams, remove the other ones
for table in soup.find_all("table"):
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            for stream in streams:
                for a in td.find_all("a"):
                    if a.get("href").split("/")[0] not in streams:
                        table.extract()

# Remove contents which are not being released
for ul in soup.find_all("ul")[:2]:
    for li in ul.find_all("li", recursive=False):
        for a in li.find_all("a"):
            if (a.get("href").lower().removeprefix("#")) not in streams:
                a.decompose()

# Due to a bug in stripping pages, rewrap all li elements
li_elements = soup.find_all('li')

for li in li_elements:
    li.unwrap()

for ul in soup.find_all("ul"):
    for a in ul.find_all("a"):
        a.wrap(soup.new_tag("li"))

stripping_version = soup.find("h1").text.strip()

# Fix links to streams in indices 
for stream in streams: 
    for a in soup.find_all("a",href=re.compile(rf"\b{stream}\b\/stripping")):
        a['href'] = stripping_version + "-" + stream + "-" + a['href'].removeprefix(f"{stream}/stripping").removesuffix(".html").replace("_","-")

# Fix links to commonparticles
for a in soup.find_all("a",href=re.compile("commonparticles")) :
    a['href'] = a['href'].replace("commonparticles/std",f"./{stripping_version}-commonparticles-std").removesuffix(".html")

with open(args.outputfile, "w") as newfile:
    newfile.write(str(soup))