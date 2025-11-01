import cv2
import os
def gray(filepath,output):
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filename = os.path.basename(filepath) 
    cv2.imwrite(f"{output}/gray{filename}",gray)
    return f"gray{filename}"