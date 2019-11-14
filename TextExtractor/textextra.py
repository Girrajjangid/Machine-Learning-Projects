# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:35:44 2019

@author: GirrajJangid
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import pytesseract as pt
pt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def rectify(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2),dtype = np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h,axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew

image = cv2.imread(img_path)

# resize image so it can be processed
# choose optimal dimensions such that important content is not lost
#z = np.multiply(image.shape[:-1] , 2).tolist()
#z.reverse()
#image = cv2.resize(image, tuple(z))


# creating copy of original image


# convert to grayscale and blur to smooth
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#blurred = cv2.medianBlur(gray, 5)

# apply Canny Edge Detection
edged = cv2.Canny(blurred, 0, 50)
orig_edged = edged.copy()

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
(contours, _) = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

#x,y,w,h = cv2.boundingRect(contours[0])
#cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),0)

# get approximate contour
for c in contours:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)

    if len(approx) == 4:
        target = approx
        break

approx = rectify(target)
pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])

M = cv2.getPerspectiveTransform(approx,pts2)
dst = cv2.warpPerspective(orig,M,(800,800))
    
cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    
    # using thresholding on warped image to get scanned effect (If Required)
ret,th1 = cv2.threshold(dst,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(dst,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(dst,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
ret2,th4 = cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh1 = cv2.threshold(dst,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(dst,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(dst,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(dst,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(dst,127,255,cv2.THRESH_TOZERO_INV)
    
Image.fromarray(orig).save('Original.jpg')
Image.fromarray(gray).save('OriginalGray.jpg')
Image.fromarray(blurred).save('OriginalBlurred.jpg')
Image.fromarray(orig_edged).save('OriginalEdged.jpg')
Image.fromarray(image).save('Original_image.jpg')
Image.fromarray(th1).save('Thresh Binary.jpg')
Image.fromarray(th2).save('Thresh mean.jpg')
Image.fromarray(th3).save('Thresh gauss.jpg')
Image.fromarray(th4).save('Otsu.jpg')
Image.fromarray(dst).save('dst.jpg')
Image.fromarray(thresh1).save('thresh1.jpg')
Image.fromarray(thresh2).save('thresh2.jpg')
Image.fromarray(thresh3).save('thresh3.jpg')
Image.fromarray(thresh4).save('thresh4.jpg')
Image.fromarray(thresh5).save('thresh5.jpg')


img_path = 'images/1e288e8c.jpeg'

print(pt.image_to_string(img_path))