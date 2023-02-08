# How to prepare the metadata for an LHCb OD release

## Steps:
- Make sure DIRAC is available on your platform (either cvmfs is mounted or work on lxplus)
- GRID proxy is required. run `lhcb-proxy-init`, enter the password for your GRID certificate. 
- To write metadata for a single DIRAC Bookkeeping path, run: 
  ``` lb-dirac python MetadataWriter.py --BK="<your bookkeepinng path>"```
  - Available flags are:
    - `--verbose` - provides various interim output while running the script.
    - `--staging` which writes out a file with `pfns` used to stage the files on open data portal. 
  This will create a `.JSON` file with metadata for the specified path conforming to OpenData Portal schema. 
- To write metadata for all paths being released, run the shell script `run1_stripping.sh` like this:
 `source ./run1_stripping.sh`

## Converting the Stripping pages into Markdown files

- Download the html files from `/eos/project/l/lhcbwebsites/www/projects/stripping/config/strippingXXX`
- Add the streams you want to convert to `sanitizeStripping.sh` and `config.py`.
- Run `sanitizeStripping.sh`
- The main index pages for each stream have to be created manually.
  - For each stream make a copy of `index.html` and delet all other streams.
- Lines, which have not been released have to be cleaned by hand. 
- The conversion to markdown then is simple:

```
pandoc ew.html --from html --to markdown-simple_tables --wrap=none --o ../MD/stripping21/stripping21_ew.md
```

## Working with authors lists 

- Go to `https://lbfence.cern.ch/membership/authorship/for-given-date
- Select end of year (xxxx-12-31) of a year of data taking
- Download List in inSpire xml format
- Convert this to json with 
	```
	cat LHCb_Authorship_xxxx-Dec-31.xml | xq . | tee author.json	
	```
	note: you have to have `yq installed` (`pip install yq`)
- Use the newly acquired json as an --inputfile for MakeAuthorRecords.py script. 