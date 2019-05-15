import numpy as np
import cv2
from pyzbar import pyzbar
import time

def decode(filename):
    start_time = time.time()
    image = cv2.imread(filename)
    print("BARCODE: ", int(pyzbar.decode(image)[0][0]))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    blurred = cv2.blur(gradient, (3, 3))
    (_, thresh) = cv2.threshold(blurred, 210, 250, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    closed = cv2.erode(closed, None, iterations = 7)
    closed = cv2.dilate(closed, None, iterations = 2)

    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

    finish_time = time.time()
    print("Time: ", finish_time-start_time)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.imwrite('result.png', image)

if __name__ == '__main__':
    decode('barcode1.jpg')

