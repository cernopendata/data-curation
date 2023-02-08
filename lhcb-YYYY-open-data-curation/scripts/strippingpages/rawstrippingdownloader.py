import os 

from config import streamsdirs, stripping_versions_dirs  

outdir = "./raw"
if not os.path.exists(outdir):
    string = f"mkdir -p {outdir}"
    os.system(string)
    
for strippingversion in stripping_versions_dirs:
    
    for stream in streamsdirs:
        if not os.path.exists("raw/" + strippingversion + "/" + stream.lower()):
            os.system(f"mkdir -p raw/{strippingversion}/{stream}") 
    
        string = f"scp -r lxplus.cern.ch:/eos/project/l/lhcbwebsites/www/projects/stripping/config/{strippingversion}/{stream.lower()} raw/{strippingversion}"
        os.system(string)
    string = f"scp -r lxplus.cern.ch:/eos/project/l/lhcbwebsites/www/projects/stripping/config/{strippingversion}/index.html raw/{strippingversion}"
    os.system(string)
