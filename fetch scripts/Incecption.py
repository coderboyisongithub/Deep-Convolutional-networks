import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import os 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

model=tf.keras.applications.inception_v3 .InceptionV3(
    include_top=False)

directory=input("image directory")

image_list=os.listdir(directory);
os.chdir(directory);
for image_file in image_list:
	print(image_file)
	img=cv.imread(image_file);
	cv.imshow("image",img);
	x=image.img_to_array(img);
	x=np.expand_dims(x,axis=0)
	x=preprocess_input(x)

	feature=model.predict(x)
	print(feature.shape)
	cv.waitKey(0);

