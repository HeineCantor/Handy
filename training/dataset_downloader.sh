#!/bin/sh

if [ -z "$1" ]; then
    DATASET="HANDS"
else
    DATASET="$1"
fi

if [ -z "$(ls -A dataset)" ]; then

    
    echo "######################"
    echo "DOWNLOADING DATASET..."

    

    mkdir dataset
    
    if [ $DATASET = "egohands" ]; then
        curl -L "https://public.roboflow.com/ds/XPzvgz2uFU?key=BA5OO8Eay6" > roboflow.zip
        unzip roboflow.zip -d dataset
        rm roboflow.zip
    else
        gdown 1FjOtDttsO9U5n6l9fTi681su0B_qC5me
        unzip dataset.zip
        rm dataset.zip
    fi

    echo "DATASET DOWNLOADED."
    echo "######################"

fi

if [ $DATASET = "egohands" ]; then

    echo "######################"
    echo "4 TO 1 CLASS EDITING..."

    cd dataset

    #edit data.yaml

    echo train: ../dataset/train/images > data.yaml
    echo val: ../dataset/valid/images >> data.yaml
    echo >> data.yaml
    echo nc: 1 >> data.yaml
    echo names: ['hand'] >> data.yaml

    cd ..
    
    cd preprocessing

    python3 4_to_1_labels.py
    
    cd ..
    
    echo "EDITING DONE."
    echo "######################"
    echo
    
fi

cd preprocessing


echo "######################"
echo "IMAGE RESIZE 1280x720 -> 640x360..."

python3 resizer.py

echo "IMAGE RESIZE DONE."
echo "######################"
echo
echo "######################"
echo "IMAGE LUMINANCE RANDOMIZER..."

python3 luminance_randomizer.py

echo "LUMINANCE RANDOMIZING DONE."
echo "######################"
echo
echo "######################"
echo "IMAGE GAUSSIAN NOISE..."

python3 gaussian_noise.py

echo "GAUSSIAN NOISING DONE."
echo "######################"

echo
echo "Dataset is ready :)"
