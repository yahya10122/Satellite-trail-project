import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

src_img = cv.imread('/Users/yahya2/PycharmProjects/Satellite trail project/venv/test.jpeg')
cv.imshow('Original Image',src_img)

temp = cv.fastNlMeansDenoisingColored(src_img,None,10,10,7,21)
dst_img = cv.Canny(temp, 50, 200, None, 3)


plt.subplot(121),plt.imshow(src_img)
plt.subplot(122),plt.imshow(temp)
plt.show()

lines = cv.HoughLines(dst_img, 1, np.pi / 180, 150, None, 0, 0)

try:
    for i in range(0, len(lines)):
                rho_l = lines[i][0][0]
                theta_l = lines[i][0][1]
                a_l = math.cos(theta_l)
                b_l = math.sin(theta_l)
                x0_l = a_l * rho_l
                y0_l = b_l * rho_l
                pt1_l = (int(x0_l + 1000*(-b_l)), int(y0_l + 1000*(a_l)))
                pt2_l = (int(x0_l - 1000*(-b_l)), int(y0_l - 1000*(a_l)))
                cv.line(src_img, pt1_l, pt2_l, (0,0,255), 3, cv.LINE_AA)
except:
    print("No Lines Found")

cv.imshow("Image with lines", src_img)
cv.waitKey(0)
