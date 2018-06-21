from matplotlib.pyplot import imshow, scatter, show, savefig
import cv2

# image = cv2.imread('test.png')
# pixel = image[5][5]
# print(pixel)
image = cv2.imread('Out.png')

row, col, __ = image.shape

for i in range(row):
    for j in range(col):
        k = image[i][j]
        if k[0]==224 and k[1]==139:
            print(i, j)
k = image[187][122]
print(k[0])
# #image = cv2.resize(image, (0,0), fx=4, fy=4)
# cv2.imshow("init", image)
# #_, image = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY)
# image = cv2.GaussianBlur(image.copy(), (27, 27), 0)
# cv2.imshow("init1", image)
# image = cv2.Canny(image, 0, 130)
# cv2.imshow("canny", image)
# cv2.waitKey(0)
# imshow(image, cmap='gray')

# circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 22, minDist=1, maxRadius=50)
# x = circles[0, :, 0]
# y = circles[0, :, 1]

# scatter(x, y)
# show()
# savefig('result1.png')
# cv2.waitKey(0)

# _, cnts, _ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE)

# # loop over the contours
# for c in cnts:
#     # compute the center of the contour
#     M = cv2.moments(c)
#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])

#     #draw the contour and center of the shape on the image
#     cv2.drawContours(image, [c], -1, (125, 125, 125), 2)
#     cv2.circle(image, (cX, cY), 3, (255, 255, 255), -1)

# cv2.imshow("Image", image)
# cv2.imwrite("result2.png", image)
# cv2.waitKey(0)