from dataset_records import *
from os import listdir
from os.path import isfile, join
from requests.packages.urllib3.exceptions import InsecureRequestWarning


exec(open('inputs/recid_info.py', 'r').read())  # import RECID_INFO
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get LHE Parent or False
def get_lhe(dataset, das_dir, mcm_dir):
    input_dataset = dataset
    while input_dataset:
        # find parent dataset, first via DAS, then via McM
        input_dataset_das = get_parent_dataset(input_dataset, das_dir)
        input_dataset_mcm = get_parent_dataset_from_mcm(
            input_dataset, das_dir, mcm_dir)

        if input_dataset.endswith('/SIM') or input_dataset.endswith('RAW') or input_dataset.endswith('/GEN-SIM'):
            datatier = get_from_deep_json(get_mcm_dict(input_dataset,mcm_dir),'datatier')
            if datatier ==  ["GEN-SIM", "LHE"]:
                return input_dataset # We need to get its LHE generator paramters (i.e. Its gridpacks or mcdb headers)

        if input_dataset[-4:] == '/LHE':
            return input_dataset

        if input_dataset_mcm == 'Default':  # workaround McM bugs
            input_dataset_mcm = ''
        if input_dataset_das:
            input_dataset = input_dataset_das
        else:
            input_dataset = input_dataset_mcm

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


def create_lhe_generator(dataset, recid, das_dir, mcm_dir, gen_store='./lhe_generators/2015-sim'):
    mcdb_id = get_from_deep_json(
        get_mcm_dict(dataset, mcm_dir), "mcdb_id") or 0
    if mcdb_id > 1:

        filepath = "{gen_store}/mcdb/{mcdb_id}".format(
            mcdb_id=mcdb_id, gen_store=gen_store)
        if os.path.exists(filepath + "_header.txt"):
            size = get_file_size('{filepath}_header.txt'.format(filepath=filepath))
            if size > 1024:
                print(str(mcdb_id) + ' mcdb Exist, Skipping')
                return

        files = [f for f in listdir(
            '/eos/cms/store/lhe/'+str(mcdb_id)) if isfile(join('/eos/cms/store/lhe/'+str(mcdb_id), f))]

        exts = []
        for file in files:
            ext = file[file.rfind('.'):]
            if ext not in exts:
                exts.append(ext)

        if len(exts) != 1 or exts[0] != '.xz' and exts[0] != '.lhe':
            print('<exterr>\n' + str(exts) + '\nInvalid extentions in ' +
                  dataset + '\n==>\t mcdb_id: ' + str(mcdb_id) + '\nSkipping...\n</exterr>', file=sys.stderr)
            return

        generators = get_from_deep_json(
            get_mcm_dict(dataset, mcm_dir), "generators") or 0

        cmds = [
            "xz -d -c /eos/cms/store/lhe/{mcdb_id}/* > {filepath} ".format(
                mcdb_id=mcdb_id, filepath=filepath) if exts[0] == '.xz'
            else "cp /eos/cms/store/lhe/{mcdb_id}/*  {filepath} ".format(
                mcdb_id=mcdb_id, filepath=filepath),
            "awk '/<!--/,/-->/' {filepath} > {filepath}_header.txt".format(
                mcdb_id=mcdb_id, filepath=filepath) if generators == ["MCFM701"]
            else "awk '/<header>/,/<\/header>/' {filepath} > {filepath}_header.txt".format(
                mcdb_id=mcdb_id, filepath=filepath)
        ]
        if cmd_run(cmds, dataset):
            size = get_file_size('{filepath}_header.txt'.format(filepath=filepath))
            if size <= 1024:
                # if empty, take comments (assume it is a MCFM701)
                cmd_run(["awk '/<!--/,/-->/' {filepath} > {filepath}_header.txt; \
                           awk '/<init>/,/<\/init>/' {filepath} >> {filepath}_header.txt;".format(
                    mcdb_id=mcdb_id, filepath=filepath)], dataset)
                size = get_file_size(
                    '{filepath}_header.txt'.format(filepath=filepath))

                if size <= 1024:
                    print("<size>\n[Warning] in " + dataset + "\n mcdb_id: " + str(mcdb_id) +
                          "\n==>\t Header file size is only " + str(size) + ' Bytes\n</size>', file=sys.stderr)

            # if we got the _header.txt file then, there is no need to keep original files
            cmd_run(['rm -rf {filepath}'.format(filepath=filepath)], dataset)

    else:
        fragment_url = get_genfragment_url(dataset, mcm_dir, das_dir)
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
        outfilepath = "{gen_store}/gridpacks/{recid}".format(  # FIXME
            gen_store=gen_store, recid=recid)

        if os.path.exists(outfilepath) and len(os.listdir(outfilepath)) != 0:
            print(str(recid) + ' recid gridpack Exist, Skipping')
            return

        if 'amcatnlo' in path or 'amcatnlo' in dataset:
            print(dataset + '\n' + str(recid) +
                  "amcatnlo gridpack!!! path:" + path)
            files = [
                'process/Cards/run_card.dat',
                './process/Cards/run_card.dat',
                'process/Cards/proc_card*.dat',
                './process/Cards/proc_card*.dat',
                'process/Cards/param_card.dat',
                './process/Cards/param_card.dat'
            ]
        elif 'madgraph' in path:
            files = [
                './process/madevent/Cards/run_card.dat',
                'process/madevent/Cards/run_card.dat',
                './process/madevent/Cards/proc_card*.dat',
                'process/madevent/Cards/proc_card*.dat',
                './process/madevent/Cards/param_card.dat',
                'process/madevent/Cards/param_card.dat',
            ]
        elif 'powheg' in path:
            files = [
                './*.input',
                '*.input',
            ]
        else:
            print("<path>\n[Error] Unknown path:('" + path +
                  "')\nDataset: " + dataset + '\n</path>', file=sys.stderr)
            return

        files = "'" + "' '".join(files) + "'"
        cmds = [
            "mkdir -p {out}; cd {out};\
            tar -xf {path} {files}".format(out=outfilepath, path=path, files=files)
        ]
        cmd_run(cmds, dataset)


das_dir = "./inputs/das-json-store"
mcm_dir = "./inputs/mcm-store"
with open("./inputs/CMS-2015-mc-datasets.txt", 'r') as file:
    dataset_full_names = file.readlines()


i = 1
l = len(dataset_full_names)
for dataset in dataset_full_names:
    dataset = dataset[:-1]

    lhe = get_lhe(dataset, das_dir, mcm_dir)
    if not lhe:
        continue

    recid = RECID_INFO[dataset]

    print("Getting ({i}/{l}): {ds}".format(
        i=i, l=l, ds=lhe or 'No LHE parent for this record'))

    t = threading.Thread(target=create_lhe_generator,
                         args=(lhe, recid, das_dir, mcm_dir))
    t.start()
    i += 1
    while threading.activeCount() >= 20:
        sleep(0.5)  # run 20 parallel
