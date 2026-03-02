"""
A script to read, resize, and display an image.
"""
import cv2

img = cv2.imread("galaxy.jpg", cv2.IMREAD_GRAYSCALE)

resized_img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))

cv2.imshow("Galaxy", resized_img)
cv2.imwrite("resized_galaxy.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
