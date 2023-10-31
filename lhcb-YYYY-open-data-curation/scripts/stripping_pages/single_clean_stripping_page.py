import argparse
import yaml 
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input_path")
parser.add_argument("--output_path")
parser.add_argument("--temp_path")
parser.add_argument("--version")
parser.add_argument("--stream")
args = parser.parse_args()

# List all files in the folder
file_list = os.listdir(args.input_path)

def filter_func(tag):
    return tag.name == 'div' and tag.get('id', '').endswith('t')

def filter_func2(tag):
    return tag.name == 'div' and tag.get('id', '').endswith('o')

# Iterate over the files
for filename in file_list:

    # Check if the item is a file (not a subdirectory)
    if os.path.isfile(os.path.join(args.input_path, filename)):
    
        with open(os.path.join(args.input_path, filename)) as infile :
            soup =  BeautifulSoup(infile,"html.parser")

        # Remove the links to stripping project homepage 
        for ancor2 in soup.find_all("a",href=re.compile(f"http")) :
            soup.a.decompose() 

        #fix links to commonparticles
        for a in soup.find_all("a",href=re.compile("commonparticles")) :
            a['href'] = a['href'].replace("../commonparticles/std",f"./{args.version}-commonparticles-std").removesuffix(".html")

        #fix links to stripping lines
        for a in soup.find_all("a",href=re.compile("stripping")) :
            a['href'] = a['href'].replace("../stripping",f"./{args.version}-{args.stream}").removesuffix(".html")

        #replace index.html with <stream>.html
        for a in soup.find_all(href="../index.html") :
            a['href']= a['href'].replace("../index.html",f"./{args.version}-index")
        
        # remove main properties headline
        for mp in soup.find_all("b",string=re.compile("operties")) :
            mp.extract()

        # remove other properties
        for element in soup.find_all(filter_func2):
            element.extract()

        # Find all divs that satisfy the custom function
        for div in  soup.find_all(filter_func):
            div.extract()

        regex = re.compile(r'div1[0-9]t[0-9]')

        # Find and remove all matching div tags
        for div in soup.find_all('div', {'class': regex}):
            div.extract()

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

        # Remove various unwaned fields
        for a in soup.find_all("a",href=re.compile("properties")):
            a.extract()

        for p in soup.find_all("p", string = "Members:"):
            p.extract()

        for p in soup.find_all("p", string = "Tools:"):
            p.extract()

        for b in soup.find_all("b", "Main properties"):
            b.extract()

        for b in soup.find_all("b", "Other properties"):
            b.extract()

        # Remove java artefact from expanded fiels 
        for tag in soup.find_all("a",href=re.compile(r"^java")):
            if tag.string is not None:
                tag.replace_with(tag.string)  # a.string is the text content of the 'a' element
            else: 
                tag.extract()

        os.makedirs(args.temp_path, exist_ok=True)

        if os.path.exists(args.temp_path):
            with open(os.path.join(args.temp_path, filename), "wt") as file:
                file.write(str(soup))

        # Process the file here
        os.makedirs(args.output_path, exist_ok=True)
        md_filename = args.version + "-" + args.stream + "-" + filename.removeprefix("stripping").removesuffix(".html").replace("_","-") + ".md"

        print(f"Writing file: {os.path.join(args.output_path, md_filename)}")

        command = f"pandoc {os.path.join(args.temp_path, filename)} --from html --to gfm --lua-filter=extension_change_html_md.lua > {os.path.join(args.output_path, md_filename)};"
        os.system(command)

        modified_lines = []
        with open(os.path.join(args.output_path, md_filename), "r") as f:
            for line in f.readlines():
                modified_line = line.replace(r"\[", "[")
                modified_line = modified_line.replace(r"\]", "]")
                modified_lines.append(modified_line)

        # Writing the modified content back to the file
        with open(os.path.join(args.output_path, md_filename), "w") as f:
            f.writelines(modified_lines)
