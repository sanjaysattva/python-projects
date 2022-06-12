import numpy as np
import cv2
from google.colab.patches import cv2_imshow  #if used in collab

img  = cv2.imread('/anveshaktest.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_ , thresh = cv2.threshold(imgGray,240 ,255 , cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours :
 approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
 x = approx.ravel()[0]
 y = approx.ravel()[1]
 if len(approx) == 4:
    cv2.putText(img, "Quadrilateral", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5 , (0,0,0))
    cv2.drawContours(img ,[approx], 0 ,(10, 50, 255), 5)


cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
