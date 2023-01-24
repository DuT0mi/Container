import  pandas as pd
import cv2 as cv
import numpy as np
from glob import glob
import matplotlib.pyplot as plt


catFiles = glob('pics/*.jpg')

imgMatplotLipb = plt.imread(catFiles[0])
img = cv.imread(catFiles[0])

# height,width,channels

pd.Series(imgMatplotLipb.flatten()).plot(kind='hist',bins=50,title='Distirbution of Pixel Values')

# Display Images
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(imgMatplotLipb)
ax.axis('off')
# plt.show()

# Channels
# shape = imgMatplotLipb.shape # For getting the img's dimensions
fig,axs = plt.subplots(1,3,figsize=(15,5))
axs[0].imshow(imgMatplotLipb[:,:,0],cmap='Reds')
axs[1].imshow(imgMatplotLipb[:,:,1],cmap='Greens')
axs[2].imshow(imgMatplotLipb[:,:,2],cmap='Blues')
axs[0].axis('off')
axs[0].set_title('Red channel')
axs[1].axis('off')
axs[1].set_title('Green channel')
axs[2].axis('off')
axs[2].set_title('Blue channel')
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()