from coco_dataset import coco_dataset_download as coco_dwn
import os

os.chdir(input("directory to download"))
#classfile=input("path to classfiles.txt")
annotation_path=input("enter path to annotations:");
classname='bicycle'
image_count=5
coco_dwn.coco_dataset_download(classname,image_count,annotation_path);
f.close()
input();