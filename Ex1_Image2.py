import cv2
import numpy as np
#import matplotlib.pyplot as plt

img1= np.zeros((500,500,3), np.uint8)

cv2.rectangle(img1,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=50,lineType=cv2.LINE_8)
cv2.rectangle(img1,pt1=(150,150),pt2=(350,350),color=(0,255,0),thickness=65,lineType=cv2.LINE_8)
cv2.rectangle(img1,pt1=(100,100),pt2=(400,400),color=(255,0,0),thickness=50,lineType=cv2.LINE_4)

cv2.imshow('imgZEROS', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
