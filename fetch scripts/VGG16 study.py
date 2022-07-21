import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import os 
import cv2 as cv
import numpy as np
from matplotlib import pyplot

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

	for layer in neuralnet.layers:
		if 'conv' not in layer.name:
			continue;
		kernel,bias=layer.get_weights()
		print(layer.name,kernel.shape)
		minfilter,maxfilter=kernel.min(),kernel.max();
		kernel=(kernel-minfilter)/(maxfilter-minfilter)
		n_filter=2
		ix=1

		for i in range(n_filter):
			f=kernel[:,:,:,i]
			for j in range(3):
				plot=pyplot.subplot(n_filter,3,ix)
				plot.set_xticks([])
				plot.set_yticks([])
				pyplot.imshow(f[:,:,j],cmap='gray')
				ix+=1
	pyplot.show()
	cv.waitKey(0);

