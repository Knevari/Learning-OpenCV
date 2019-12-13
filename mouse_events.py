import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        colorImg = np.zeros((512, 512, 3), np.uint8)
        colorImg[:] = [b, g, r]

        cv2.imshow('Color', colorImg)

# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('kylo_ren.png', 1)

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
