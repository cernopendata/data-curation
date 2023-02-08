import sys
infile=sys.argv[1]
outdir=sys.argv[2]
prefix = sys.argv[3]  # usually the stripping version
# stream = sys.argv[4]
import os
filename=os.path.basename(infile)
filename2=filename.replace(".html","_clean.html")
outfile=outdir+(filename2)

from config import streamsdirs

from bs4 import BeautifulSoup

with open(infile) as fp :
    soup= BeautifulSoup(fp,"html.parser")

import re

#fix links to commonparticles
for ancor2 in soup.find_all("a",href=re.compile("commonpart")) :
    ancor2['href']=ancor2['href'].replace("commonparticles/std",f"./{prefix}-std").removesuffix(".html")

#fix links to streams in indices 
for stream in streamsdirs: 
    for ancor2 in soup.find_all("a",href=re.compile(f"{stream}\/stripping")) :
        ancor2['href']=f"{prefix}-" + ancor2['href'].removeprefix(f"{stream}/stripping").removesuffix(".html").replace("_","-")

# Remove the links to stripping project homepage 
for ancor2 in soup.find_all("a",href=re.compile(f"http")) :
    soup.a.decompose() 

# Remove the links to stripping project homepage 
for ancor2 in soup.find_all("a",href=re.compile(f"http")) :
    soup.a.decompose() 

# write out cleaned up html
html = soup.prettify("utf-8")
with open(outfile, "wb") as file:
    file.write(html)    