# EgoHands > specific
https://public.roboflow.ai/object-detection/hands

Provided by [IU Computer Vision Lab](http://vision.soic.indiana.edu/projects/egohands/)
License: CC BY 4.0

![EgoHands Dataset](https://i.imgur.com/eEWi4PT.png)

## About this dataset

The EgoHands dataset is a collection of 4800 annotated images of human hands from a first-person view originally collected and labeled by Sven Bambach, Stefan Lee, David Crandall, and Chen Yu of the University of Indiana.

The dataset was captured via frames extracted from video recorded through head-mounted cameras on a Google Glass headset while peforming four activities: building a puzzle, playing chess, playing Jenga, and playing cards. There are 100 labeled frames for each of 48 video clips.

## Our modifications

[The original EgoHands dataset](http://vision.soic.indiana.edu/projects/egohands/) was labeled with polygons for segmentation and released in a Matlab binary format. We converted it to an object detection dataset using a modified version of [this script](https://github.com/molyswu/hand_detection/blob/temp/hand_detection/egohands_dataset_clean.py) from [@molyswu](https://github.com/molyswu) and have archived it in many popular formats for use with your [computer vision models](https://models.roboflow.com).

After converting to bounding boxes for object detection, we noticed that there were several dozen unlabeled hands. We added these by hand and improved severla hundred of the other labels that did not fully encompass the hands (usually to include omitted fingertips, knuckles, or thumbs). In total, 344 images' annotations were edited manually.

We chose a new [random train/test split](https://blog.roboflow.com/train-test-split/) of 80% training, 10% validation, and 10% testing. Notably, this is not the same split as in [the original EgoHands paper](http://vision.soic.indiana.edu/papers/egohands2015iccv.pdf).

There are two versions of the converted dataset available:
* **specific** is labeled with four classes: `myleft`, `myright`, `yourleft`, `yourright` representing which hand of which person (the viewer or the opponent across the table) is contained in the bounding box.
* **generic** contains the same boxes but with a single `hand` class.

## Using this dataset

The authors have graciously allowed Roboflow to re-host this derivative dataset. It is released under a Creative Commons by Attribution 4.0 license. You may use it for academic or commercial purposes but must cite [the original paper](http://vision.soic.indiana.edu/papers/egohands2015iccv.pdf).

Please use the following Bibtext:
```
@inproceedings{egohands2015iccv,
    title = {Lending A Hand: Detecting Hands and Recognizing Activities in Complex Egocentric Interactions},
    author = {Sven Bambach and Stefan Lee and David Crandall and Chen Yu},
    booktitle = {IEEE International Conference on Computer Vision (ICCV)},
    year = {2015}
}
```