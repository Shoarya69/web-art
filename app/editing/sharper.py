import cv2
import numpy as np
import os
sharpe =np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

def sharp(filepath,output):
    img = cv2.imread(filepath)
    temp = cv2.filter2D(img,cv2.CV_32F,sharpe)
    sharpend = cv2.convertScaleAbs(temp)
    filename = os.path.basename(filepath) 
    cv2.imwrite(f"{output}/sharp{filename}",sharpend)
    return f"sharp{filename}"