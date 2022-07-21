import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import os 
import cv2 as cv
import numpy as np
from matplotlib import pyplot
from numpy import expand_dims
neuralnet=tf.keras.applications.vgg16.VGG16(
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

	feature=neuralnet.predict(x)
	print(feature.shape)

	square=8
	ix=1
	for _ in range(square):
		for _ in range(square):
			plot=pyplot.subplot(square,square,ix)
			plot.set_xticks([])
			plot.set_yticks([])
			pyplot.imshow(feature[0,:,:,ix+1]);
			ix+=1

	pyplot.show()
	cv.waitKey(0);

