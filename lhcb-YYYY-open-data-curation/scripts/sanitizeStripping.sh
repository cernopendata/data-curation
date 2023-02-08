#!/bin/bash

SOURCEDIR=../lhcb-runI/StrippingLines/raw
TARGETDIR=../lhcb-runI/StrippingLines/Processed

# Stripping version here corresponds to the directories in eos, holding html stripping pages (the actual processing pass (stripping version) might have a suffix (stripping21r1p1a))
for STRIPPINGVERSION in stripping21  stripping21r0p1  stripping21r0p2  stripping21r1  stripping21r1p1  stripping21r1p2;
do
    for stream in leptonic ew commonparticles radiative;
    # for stream in commonparticles;
    do
        
        # Radiative stream is not available for all stripping versions, empty files and indexes are created so we want to filter this out
        if [[ $STRIPPINGVERSION != stripping21 && $STRIPPINGVERSION != stripping21r1 && $stream = radiative ]] ; then
            echo The $stream stream is not available $STRIPPINGVERSION stripping version
            continue
        fi
        
        mkdir -p $TARGETDIR/${STRIPPINGVERSION}
        mkdir -p $TARGETDIR/${STRIPPINGVERSION}_${stream}_html
        mkdir -p $TARGETDIR/${STRIPPINGVERSION}/${stream}
        
        echo Creating indices...
        
        python cleanIndexPages.py $SOURCEDIR/$STRIPPINGVERSION/${STRIPPINGVERSION}_${stream}.html  $TARGETDIR/${STRIPPINGVERSION}_${stream}_html/ $STRIPPINGVERSION $stream;
        pandoc $TARGETDIR/${STRIPPINGVERSION}_${stream}_html/${STRIPPINGVERSION}_${stream}_cleanindex.html  --from html --to gfm --lua-filter=links-to-md.lua | sed 's/\\\[/[/g' | sed 's/\\\]/]/g' > $TARGETDIR/$STRIPPINGVERSION/${stream}/${STRIPPINGVERSION}_${stream}.md;
        
        echo Cleaning lines...
        
        for line in $SOURCEDIR/$STRIPPINGVERSION/$stream/*.html ;
        do  linename=$(basename -- "$line")
            python cleanStrippingPages.py $line $TARGETDIR/${STRIPPINGVERSION}_${stream}_html/ $STRIPPINGVERSION $stream;
        done;
        
        echo Writing to Markdown ...
        
        for line in $TARGETDIR/${STRIPPINGVERSION}_${stream}_html/*clean.html ;
        do  linename=$(basename -- "$line")
            pandoc ${line} --from html --to gfm --lua-filter=links-to-md.lua | sed 's/\\\[/[/g' | sed 's/\\\]/]/g' > $TARGETDIR/${STRIPPINGVERSION}/${stream}/${linename/_clean.html/.md}
        done;
        
        # Remove the temp dir
        rm -r $TARGETDIR/${STRIPPINGVERSION}_${stream}_html
        
        echo Completed ${STRIPPINGVERSION} ${stream}
        echo
    done;
done;

echo Making JSONS... 
python StrippingLinesJSONmaker.py