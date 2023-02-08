import argparse
from config import stripping_versions_dirs

parser = argparse.ArgumentParser()
parser.add_argument("--inputfile",  help = "index.html")
parser.add_argument("--outputfile", help = "newindex.html")

args = parser.parse_args()

with open(args.inputfile, "r") as f :
    lines = f.readlines()
    
    
with open(args.outputfile, "w") as newfile:
    for line in lines:
        if "href=\"bhadron"               in line or \
           "href=\"bhadroncompleteevent"  in line or \
           "href=\"calibration"           in line or \
           "href=\"charm"                 in line or \
           "href=\"charmcompleteevent"    in line or \
           "href=\"charmtobeswum"         in line or \
           "href=\"dimuon"                in line or \
           "href=\"minibias"              in line or \
           "href=\"pid"                   in line or \
           "href=\"semileptonic"          in line or \
           "href=\"mdst"                  in line or \
           "href=\"#bhadron"              in line or \
           "href=\"#bhadroncompleteevent" in line or \
           "href=\"#calibration"          in line or \
           "href=\"#charm"                in line or \
           "href=\"#charmcompleteevent"   in line or \
           "href=\"#charmtobeswum"        in line or \
           "href=\"#dimuon"               in line or \
           "href=\"#minibias"             in line or \
           "href=\"#pid"                  in line or \
           "href=\"#semileptonic"         in line or \
           "href=\"#mdst"                 in line or \
           "name=\"bhadron"               in line or \
           "name=\"bhadroncompleteevent"  in line or \
           "name=\"calibration"           in line or \
           "name=\"charm"                 in line or \
           "name=\"charmcompleteevent"    in line or \
           "name=\"charmtobeswum"         in line or \
           "name=\"dimuon"                in line or \
           "name=\"minibias"              in line or \
           "name=\"pid"                   in line or \
           "name=\"semileptonic"          in line or \
           "name=\"mdst"                  in line:
            continue
        else:                
            newfile.write(line)