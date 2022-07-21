from coco_dataset import coco_dataset_download as coco_dwn
import os

os.chdir(input("directory to download"))
classname='person'
image_count=50
annotation_path=input("enter path to annotations:");
coco_dwn.coco_dataset_download(classname,image_count,annotation_path);