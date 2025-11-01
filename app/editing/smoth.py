import cv2
import os
def smoth(filepath,output):
    img = cv2.imread(filepath)
    blur = cv2.GaussianBlur(img,(3,3),0)
    filename = os.path.basename(filepath) 
    cv2.imwrite(f"{output}/smoth{filename}",blur)
    return f"smoth{filename}"