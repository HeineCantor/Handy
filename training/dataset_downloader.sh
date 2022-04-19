#!/bin/sh

if [ -z "$(ls -A dataset)" ]; then

echo "######################"
echo "DOWNLOADING DATASET..."

mkdir dataset
curl -L "https://public.roboflow.com/ds/XPzvgz2uFU?key=BA5OO8Eay6" > roboflow.zip
unzip roboflow.zip -d dataset
rm roboflow.zip

echo "DATASET DOWNLOADED."
echo "######################"

fi

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

echo "EDITING DONE."
echo "######################"
echo
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