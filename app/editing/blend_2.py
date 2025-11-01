import cv2

def blend(filepath1,filepath2,output):
    img1 = cv2.imread(filepath1)
    img2 = cv2.imread(filepath2)

    blend = cv2.addWeighted(img1,0.5,img2,0.5,-100)
    cv2.imwrite(f"blend2{output}.jpg",blend)