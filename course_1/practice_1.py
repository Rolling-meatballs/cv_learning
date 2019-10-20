import cv2
import random
import numpy as np
from matplotlib import pyplot as plt


img_gray = cv2.imread('C:\Users\yangf\Murphy\test\cv_learning\course1/woman-3219507__340.jpg',0)
cv2.imshow('woman', img_gray)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()