import cv2 as cv

# Configurable Parameter
source = "img.JPG"
destination = "newImage.png"
scale_percent = 50

image = cv.imread(source, cv.IMREAD_UNCHANGED)
cv.imshow('title', image)


# calculate the 50 percent of original dimesion
width = int(image.shape[1] * scale_percent /100)
height = int(image.shape[0] * scale_percent / 100)

# image resize
output = cv.resize(image, (width, height))


cv.imwrite(destination, output)
cv.waitKey(0)
