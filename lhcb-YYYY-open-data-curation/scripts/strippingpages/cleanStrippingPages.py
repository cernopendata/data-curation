import sys
infile = sys.argv[1]
outdir = sys.argv[2]
prefix = sys.argv[3]
stream = sys.argv[4]
import os
filename  = os.path.basename(infile)
filename2 = filename.replace(".html","_clean.html").replace("stripping","")
outfile   = outdir+(prefix+"_"+filename2)

from bs4 import BeautifulSoup

with open(infile) as fp :
    soup= BeautifulSoup(fp,"html.parser")

import re

# Remove the links to stripping project homepage 
for ancor2 in soup.find_all("a",href=re.compile(f"http")) :
    soup.a.decompose() 
    
#replace index.html with <stream>.html
for ancor in soup.find_all(href="../index.html") :
    ancor['href']=(f"./{prefix}-index")

#fix links to commonparticles
for ancor2 in soup.find_all("a",href=re.compile("commonpart")) :
    ancor2['href']=ancor2['href'].replace("../commonparticles/std",f"./{prefix}-std").removesuffix(".html")

# remove main properties headline
for mp in soup.find_all("b",text=re.compile("operties")) :
    mp.extract()

# Remove OtherProperties
for otherInfo in soup.find_all(id=re.compile(r"^div\d+o")):
    otherInfo.clear()
    prev=otherInfo.previous_sibling.previous_sibling
    otherInfo.extract()
    prev.clear()
    prev.extract()

# Remove remaining javascript
for c in soup.find_all("script") :
    c.clear()
    c.extract()

for indentInfo in soup.find_all(id=re.compile(r"^indent"), class_='hidden'):
    indentInfo.clear()
    indentInfo.extract()

for indent in soup.find_all(align="right"):
    indent.clear()
    indent.extract()

# unhide all remaining fields
for hiddenInfo in soup.find_all(class_='hidden'):
    hiddenInfo.unwrap()

# unhide all remaining fields
for hiddenInfo in soup.find_all(class_='unhidden'):
    hiddenInfo.unwrap()

for jsc in soup.find_all(href=re.compile(r"^javascript")):
    newtag=soup.new_tag("b")
    newtag.contents=jsc.contents
    jsc.replace_with(newtag)

# write out cleaned up html
html = soup.prettify("utf-8")
with open(outfile, "wb") as file:
    file.write(html)

    