import cv2
import os
def cartoon(filepath,output):
    img = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    gray_blur = cv2.medianBlur(img,13)
    edgs = cv2.Canny(img,50,150)
    bit_nor = cv2.bitwise_not(edgs)
    blend = cv2.addWeighted(bit_nor,0.7,gray_blur,1.1,-120)
    filename = os.path.basename(filepath) 
    cv2.imwrite(f"{output}/cart{filename}",blend)
    return f"cart{filename}"