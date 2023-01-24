import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale) 
    dimesnions = (width,height)
    return cv.resize(frame,dimesnions,interpolation=cv.INTER_AREA)

img = cv.imread('pictures/cat.jpg') 
scaleFactor = 1.0
widht = int(img.shape[1] * scaleFactor / 10)
height = int(img.shape[0] * scaleFactor / 10)
dim = (widht,height)

resized = cv.resize(img,dim,interpolation=cv.INTER_AREA)
           
cv.imshow('Cat',resized)
cv.waitKey(0)
cv.destroyAllWindows()
