import os
import cv2

path = "/home/pysolo/Pictures/170120_subset/"
filename = "2017_01_22_03_16_00_344571.png"
fp = os.path.join(path, filename)
try:
    frame = cv2.imread(fp,cv2.CV_LOAD_IMAGE_COLOR)
except Exception as e:
    print ( 'Error loading image! %s' % fp )
    print str(e) 
    raise
    
cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
