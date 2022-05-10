# Code inspired from
# OpenCV tutorial on stereo depthmaps https://docs.opencv.org/4.5.5/dd/d53/tutorial_py_depthmap.html
# and https://learnopencv.com/introduction-to-epipolar-geometry-and-stereo-vision/
import cv2
import numpy as np

# TODO Reading the left and right images.
<<<<<<< HEAD
img_left = cv2.imread('images/tsukuba01.jpg')
img_right = cv2.imread('images/tsukuba02.jpg')

# TODO Set parameters for block matching stereo
numDisparities = 64
blockSize = 9

# TODO Create a simple block matching stereo computation object StereoBM_create
stereo = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

# TODO Setting parameters for StereoSGBM algorithm
minDisparity = 0
numDisparities = 64
blockSize = 8
disp12MaxDiff = 1
uniquenessRatio = 10
speckleWindowSize = 10
speckleRange = 8

# TODO Creating an object of StereoSGBM algorithm
stereo = cv2.StereoSGBM_create(minDisparity=minDisparity,
                               numDisparities=numDisparities,
                               blockSize=blockSize,
                               disp12MaxDiff=disp12MaxDiff,
                               uniquenessRatio=uniquenessRatio,
                               speckleWindowSize=speckleWindowSize,
                               speckleRange=speckleRange)

# TODO Calculate disparity using the chosen stereo algorithm
disp = stereo.compute(img_left, img_right).astype(np.float32)

# TODO Normalize the disparity map in order to display it
disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)

cv2.imshow("left image", img_left)
cv2.imshow("right image", img_left)

# TODO Display the disparity map
cv2.imshow("disparity", disp)
cv2.waitKey(0)
=======


# TODO Set parameters needed for stereo matching


# TODO Create a stereo computation object using StereoBM_create or StereoSGBM_create

# TODO Calculate disparity using the chosen stereo algorithm


# TODO Normalize the disparity map in order to display it

# TODO Display the disparity map
>>>>>>> 59a7c87fc9f45ce608c0f771e6eb36d1e8fb94aa
