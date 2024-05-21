# Detection of floating plastic litter and water hyacinths using Yolov8 deep learning model

This repository contains the code used for the following publication:
```bash
  To do: XXXXXXXX
```

The aim of this code is to use Yolov8 deep learning model to detect floating plastic litter and water hyacinths in the Saigon rivers, Vietnam.

Acknowledgement:

This project was inspired by the work of Ultralytics YOLOv8 (https://github.com/ultralytics/ultralytics). 
Learn more about Ultralytics YOLOv8 at [documentation](https://docs.ultralytics.com/).

## Dataset

"XXX" dataset is a new labelled dataset for detecting floating plastic litter and water hyacinths with computer vision. It includes 272 images and 9,352 annotated plastic litter items and water hyacinths (with bounding boxes). This dataset and further details can be found in:

```bash
  To do: XXXXXXXX
```

## Requirements:
- Windows 10
- Python 3.9.12
- Pytorch 2.0.0

(1) Install Pytorch 2.0.0 (CUDA 11.7) in Windows10

```bash
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia
```
(2) Install other packages

```bash
  pip install -r requirements.txt
```

## Usage

-  `main_Train_.ipynb` is the code for training the Yolov8 model for object detection.
-  `main_Evaluate.ipynb` is the code for (1) evaluating model performances on test sets (e.g., output mAP50, precision and recall), (2) predicting objects in images and videos, and (3) outputing bounding box (bbox) information (e.g., the area of each bbox).


## Citing this dataste or paper

If you find this code and dataset are useful in your research or wish to refer to the paper, please use the following BibTeX entry.

```BibTeX
XXXXX
```

## Contact

➡️ Tianlong Jia ([T.Jia@tudelft.nl](mailto:T.Jia@tudelft.nl))
