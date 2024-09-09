# How to prepare the metadata for an LHCb OD release

## Configuration: 
    Various parameters are configurable from `config.yaml`. Uncomment the relevant paths and streams, change values of the parameters.  
  - `directory` + `stream` directive is used for DIRAC related activities, to construct a bookkeeping path.
  - `stripping_version` is used for documentation pages (the paths here are slightly different from those on DIRAC). 
  - `release_dir` - output directory.
  - `stripping_input_dir` - stripping pages input directory. 


## Steps:
- Make sure DIRAC is available on your platform (either cvmfs is mounted or work on lxplus)
- GRID proxy is required. Run `lhcb-proxy-init`, enter the password for your GRID certificate. 
- To write metadata for a single DIRAC Bookkeeping path, run: 
  ``` lb-dirac python MetadataWriter.py --BK="<your bookkeepinng path>"```
  - Available flags are:
    - `--verbose` - provides various interim output while running the script.
    - `--staging` which writes out a file with `pfns` used to stage the files on open data portal. 
  This will create a `.JSON` file with metadata for the specified path conforming to OpenData Portal schema. 
- To write metadata for all paths being released, run the script `make_release.py`.

## Converting the Stripping pages into Markdown files
- Download the html files from `/eos/project/l/lhcbwebsites/www/projects/stripping/config/strippingXXX`
- Set the `stripping_input_dir` to the path where the files are downloaded.  
  - This can be done manually with `xrdcp`, `scp`, `eos cp` commands.
- Run `snakemake --cores all` in the `scripts/stripping_pages` directory. 