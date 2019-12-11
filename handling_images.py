import cv2

img = cv2.imread('kylo_ren.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Kylo Ren', img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('kylo_ren_copy.png', img)
    cv2.destroyAllWindows()
