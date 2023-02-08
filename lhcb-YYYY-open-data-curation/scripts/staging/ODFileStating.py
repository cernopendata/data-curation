import os
Files = [
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

for file in Files:

    string = f"lb-dirac fts-rest-transfer-submit -s https://fts3-pilot.cern.ch:8446 -f {file}"
    print(string)
    os.system(string)
