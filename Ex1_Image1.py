import cv2
import numpy as np

W=500
H=500

im = np.zeros ((W,H), np.uint8)

def show_im(im):
    cv2.imshow('window', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
for i in range (W): im[i,i] = (255)

show_im(im)
