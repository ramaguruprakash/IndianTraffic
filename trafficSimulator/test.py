#! /users/guruprakash.r/miniconda2/bin/python

import numpy as np
import cv2
arr = np.zeros((500,500,3))
cv2.line(arr, (80, 100) ,(80, 300),(255,0,0), 1)
cv2.line(arr, (120, 100) ,(120, 300),(255,0,0), 1)
cv2.imshow("arr", arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
