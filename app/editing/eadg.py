import cv2
import os
def edge(filepath,output):
    img = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img,50,150)
    bit_nor = cv2.bitwise_not(edges)
    filename = os.path.basename(filepath) 
    cv2.imwrite(f"{output}/edge{filename}",bit_nor)
    return f"edge{filename}"