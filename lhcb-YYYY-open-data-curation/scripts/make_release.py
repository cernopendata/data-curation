import yaml
import subprocess 

# Read in the configuration file 
with open("../config.yaml", "r") as f: 
    conf = yaml.safe_load(f)

# Run the metadata_writer on each directory+stream combination 
for dir in conf["directory"]:
	for stream in conf["stream"]:
		    processes = [subprocess.Popen(f'lb-dirac python metadata_writer.py --BK=\"{dir+stream}\" --staging &', shell=True)]

# Wait for all processes to finish
for p in processes:
	p.wait()
	
print(f'Metadata to be written to {conf["release_dir"]}')