from dataset_records import *
from os import listdir
from os.path import isfile, join
from requests.packages.urllib3.exceptions import InsecureRequestWarning


exec(open('inputs/recid_info.py', 'r').read())  # import RECID_INFO
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get LHE Parent or False
def get_lhe(dataset, mcm_dir):
    path = mcm_dir + '/chain/' + dataset.replace('/', '@')
    step_dirs = os.listdir(path)
    for step in step_dirs:
        step_dir = path + '/' + step
        datatier = get_from_deep_json(get_mcm_dict(dataset,step_dir),'datatier')
        if "LHE" in datatier:       
            return step_dir

    return False


def cmd_run(cmds, dataset):
    for cmd in cmds:
        err = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE).stderr.decode()
        if err:
            print("<pserr>\n[Error] in " + dataset + "\n==>\t" +
                  err + "<==\n</pserr>", file=sys.stderr)
            return False
    return True


def create_lhe_generator(dataset, recid, mcm_dir, gen_store='./lhe_generators/2016-sim'):
# mcm_dir is the directory of the LHE step
        fragment_url = get_genfragment_url(dataset, mcm_dir)
        if fragment_url:
            fragment_url = fragment_url[0]
            fragment = requests.get(fragment_url, verify=False).text
            if not fragment:
                fragment = get_from_deep_json(
                    get_mcm_dict(dataset, mcm_dir), "fragment")
        else:
            fragment = get_from_deep_json(
                get_mcm_dict(dataset, mcm_dir), "fragment")
        if not fragment:
            print("<emp>\n[Error] in" + dataset +
                  "\n==>\t No fragment URL and Empty fragment in mcm dict, Skipping\n</emp>", file=sys.stderr)
            return

        path = re.search(r"cms.vstring\('(.*?)'", fragment)
 
        if not path:
            print("<vstring>\n[Warning] in" + dataset +
                  "\n==>\t 'cms.vstring' not found in fragment , Skipping\n</vstring>", file=sys.stderr)
            return
        path = path.group(1)
        # print("found path: " + str(path) )
        outfilepath = "{gen_store}/gridpacks/{recid}".format(
            gen_store=gen_store, recid=recid)

        if os.path.exists(outfilepath) and len(os.listdir(outfilepath)) != 0:
            print(str(recid) + ' recid gridpack Exist, Skipping')
            return

        if 'amcatnlo' in path or 'amcatnlo' in dataset:
            print(dataset + '\n' + str(recid) +
                  "amcatnlo gridpack!!! path:" + path)
            files = [
                'process/Cards/run_card.dat',
                'process/Cards/proc_card*.dat',
                'process/Cards/param_card.dat',
            ]
            mv_cmd = "mv process/Cards/*dat .; rmdir -p process/Cards"
        elif 'madgraph' in path:
            files = [
                'process/madevent/Cards/run_card.dat',
                'process/madevent/Cards/proc_card*.dat',
                'process/madevent/Cards/param_card.dat',
            ]
            mv_cmd = "mv process/madevent/Cards/*dat .; rmdir -p process/madevent/Cards"
        elif 'powheg' in path:
            files = [
                '*.input',
            ]
            mv_cmd = ""
        else:
            print("<path>\n[Error] Unknown path:('" + path +
                  "')\nDataset: " + dataset + '\n</path>', file=sys.stderr)
            return

        files = "'" + "' '".join(files) + "'"
        cmds = [
            "mkdir -p {out}; cd {out};\
            tar -xf {path} {files} -C {out}; {mv}".format(out=outfilepath, path=path, files=files, mv=mv_cmd)
        ]
        # print("Prepared commands: " + str(cmds))
        cmd_run(cmds, dataset)


das_dir = "./inputs/das-json-store"
mcm_dir = "./inputs/mcm-store"
with open("./inputs/CMS-2016-mc-datasets.txt", 'r') as file:
    dataset_full_names = file.readlines()

dataset_nanoaod = [name[:-1] for name in dataset_full_names if name[:-1].endswith('NANOAODSIM')]
i = 1
l = len(dataset_nanoaod)
for dataset in dataset_nanoaod:

    #dataset = dataset[:-1]

    lhe_dir = get_lhe(dataset, mcm_dir)
    if not lhe_dir:
        continue

    recid = RECID_INFO[dataset]

    print("Getting ({i}/{l}): {ds}".format(
        i=i, l=l, ds=lhe_dir or 'No LHE parent for this record'))

    t = threading.Thread(target=create_lhe_generator,
                         args=(dataset, recid, lhe_dir))
    t.start()
    i += 1
    while threading.activeCount() >= 20:
        sleep(0.5)  # run 20 parallel
