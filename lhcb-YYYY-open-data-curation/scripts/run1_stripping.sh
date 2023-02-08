#!/bin/bash
DIRS=(
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r1/90000000"
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r1/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21/90000000"
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r1p1a/90000000"
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r1p1a/90000000"
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r1p2/90000000"
	"/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r1p2/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r0p1a/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r0p1a/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r0p2/90000000"
	"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r0p2/90000000"
)
STREAMS=(
	"EW.DST"
	"LEPTONIC.MDST"
	"RADIATIVE.DST"
)

# IMPORTANT! RADIATIVE STREAM is not available in all stripping versions 

trap "kill 0" EXIT
for DIR in "${DIRS[@]}"
do
	for STREAM in "${STREAMS[@]}"
	do
		lb-dirac python MetadataWriter.py --BK="$DIR/$STREAM" --staging &
	done
done
wait
trap "echo Done" EXIT

# STREAMS=(
# 	"BHADRON.MDST"
# 	"BHADRONCOMPLETEEVENT.DST"
# 	"CHARM.MDST"
# 	"CHARMCOMPLETEEVENT.DST"
# 	"DIMUON.DST"
# 	"EW.DST"
# 	"LEPTONIC.MDST"
# 	"RADIATIVE.DST"
# 	"SEMILEPTONIC.DST"
# )
