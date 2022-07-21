#shivanshu Raj@class dataset downloader
from coco_dataset import coco_dataset_download as coco_dwn
import os

os.chdir(input("directory to download"))
classfile=input("path to classfiles.txt")
annotation_path=input("enter path to annotations:");
classname='person'
image_count=5
f=open(classfile+"/COCOclasses.txt","r");
if "#CLASS" in f.readline():
	while True:
		klass=f.readline();
		klass=klass.strip();
		if "#END" in klass:
			break;
		else:
			print("class:"+klass)
			coco_dwn.coco_dataset_download(klass,image_count,annotation_path);
f.close()
input();