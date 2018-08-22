import os
import cv2

images = os.listdir("./dump")
for i in images:
	img = cv2.imread("./dump/"+i)
	resized = cv2.resize(img,(100,100))
	cv2.imwrite("./dump/100x100 "+i,resized)
