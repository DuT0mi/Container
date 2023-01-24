import cv2 as cv
import numpy as np

def translate(pImg,pX,pY):
    transMatrix = np.float32([[1,0,pX],[0,1,pY]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(pImg,transMatrix,dimensions)

img = cv.imread('pictures/cat.jpg')

scaleFactor = 1.0

width = int(img.shape[1] * scaleFactor / 10)

height = int(img.shape[0] * scaleFactor / 10)

dim = (width,height)

resizedImg = cv.resize(img,dim,interpolation=cv.INTER_AREA)

cv.imshow('Cat',resizedImg)

# translation
translatedImg = translate(resizedImg,-100,100)
cv.imshow('Translated',translatedImg)

cv.waitKey(0)
cv.destroyAllWindows()