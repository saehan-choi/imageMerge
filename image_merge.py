import cv2
import numpy as np
from glob import glob
import random

path = './all_of_images/*'

paths = glob(path)
random.shuffle(paths)

ones = np.ones((2000,2000,3), dtype=np.int64)

resultImgsize = (2000,2000)

for i in range(0, resultImgsize[0], 10):
    for j in range(0, resultImgsize[1], 10):
        
        img = cv2.imread(paths.pop())
        img = cv2.resize(img,(10, 10))
        
        ones[i:i+10,j:j+10,:] = img.copy()

cv2.imwrite('all_of_images_merge.jpg', ones)