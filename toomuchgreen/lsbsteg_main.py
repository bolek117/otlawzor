__author__ = 'root'

from LSBSteg import LSBSteg
import cv2
import numpy as np

im = cv2.imread('toomuchgreen.png')
steg = LSBSteg(im)
#dec = steg.unhideImage()
#cv2.imwrite('recovered', dec)
dec = steg.unhideText()
print dec