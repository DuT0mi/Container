import cv2 as cv

img = cv.imread('pictures/cat.jpg')

# resize

scaleFactor = 1.0
width = int(img.shape[1] * scaleFactor / 10)
height = int(img.shape[0] * scaleFactor / 10)
dim = (width,height)

resizedImg = cv.resize(img,dim,interpolation=cv.INTER_AREA)


#cv.imshow('Cat',img)

# Converting to grayscale
gray = cv.cvtColor(resizedImg,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur

blur = cv.GaussianBlur(resizedImg,(11,11),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edges with blur is interesting
canny = cv.Canny(resizedImg,125,175)
cv.imshow('Canny',canny)


# Dilating
dilated = cv.dilate(canny,(7,7),iterations=1)
cv.imshow('Dilated',dilated)


# Eroding
eroded = cv.erode(dilated,(3,3),iterations=2)
cv.imshow('Eroded',eroded)


cv.waitKey(0)
cv.destroyAllWindows()