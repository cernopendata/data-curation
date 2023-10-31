import json

stagingindexefiles = [
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1_LEPTONIC.MDST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1p1a_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1p1a_LEPTONIC.MDST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1p2_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1p2_LEPTONIC.MDST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r1_RADIATIVE.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1_LEPTONIC.MDST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1p1a_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1p1a_LEPTONIC.MDST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1p2_EW.DST.txt",
    "FilesToStage_Beam3500GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r1p2_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r0p1a_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r0p1a_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r0p2_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21r0p2_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagDown__RealData_Reco14_Stripping21_RADIATIVE.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r0p1a_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r0p1a_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r0p2_EW.DST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21r0p2_LEPTONIC.MDST.txt",
    "FilesToStage_Beam4000GeV-VeloClosed-MagUp__RealData_Reco14_Stripping21_RADIATIVE.DST.txt",
]

newdict = {}

for indfile in stagingindexefiles:
    with open(f"FTSReady/{indfile}") as f:
        filesdict = json.load(f)

    if "MDST" in indfile:
        newfilename = indfile.removeprefix("FilesToStage_").replace("-","_").replace("__","_").replace(".MDST.txt","_MDST")
    else:
        newfilename = indfile.removeprefix("FilesToStage_").replace("-","_").replace("__","_").replace(".DST.txt","_DST")
            
    for file in filesdict["files"]:

        if "MDST" in indfile:
            newdict[file["destinations"][0]] = file["destinations"][0].split(".MDST")[0] + "/"+newfilename + file["destinations"][0].split(".MDST")[1]
        else:
            newdict[file["destinations"][0]] = file["destinations"][0].split(".DST")[0] + "/"+newfilename + file["destinations"][0].split(".DST")[1]
                
    print(json.dumps(newdict, indent=4, sort_keys=True))

with open("eosrenamedfiles.json", "w") as fl:

    json.dump(newdict, fl, indent=2)


