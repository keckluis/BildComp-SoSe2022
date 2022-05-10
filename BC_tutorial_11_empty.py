import exifread
import cv2
import numpy as np


# TODO Define  a function to compute a fraction given as string
<<<<<<< HEAD
def _derationalize(rational):
    all = rational.split('/')

    if len(all) > 1:
        numerator = float(all[0])
        denominator = float(all[1])
        return numerator / denominator
    return float(rational)

# TODO Open an jpg image file in order to read out the exif data
img_file = 'Fuji/DSCF7164.JPG'
f = open(img_file, 'rb')

# TODO Get all Exif tags
tags = exifread.process_file(f, details = False)

# TODO Read the EXIF FocalLength tag and compute the value from it
for tag in tags.keys():
    if tag in ('EXIF FocalLength'):
        focalLength_mm = _derationalize(tags[tag].__str__())

# TODO print the computed focal length as float value
print('Focal length: ' + str(focalLength_mm))

# TODO Close the file
f.close()

# TODO Read the file as an OpenCV image
img = cv2.imread(img_file)

# TODO Extract image resolution
width, height, channels = img.shape

# TODO Compute fx, fy, cx, cy using sensor size information
sensor_width_mm = 23.5
sensor_height_mm = 15.6
fx = width * focalLength_mm / sensor_width_mm
fy = height * focalLength_mm / sensor_height_mm
cx = width / 2.0
cy = height / 2.0

# TODO define camera intrinsic matrix K
K = np.zeros((3, 3), np.float32)
K[0, 0] = fx
K[1, 1] = fy
K[0, 2] = cx
K[1, 2] = cy
K[2, 2] = 0.0

# TODO print(K)
print(K)
=======

# TODO Open an jpg image file in order to read out the exif data

# TODO Get all Exif tags

# TODO Read the EXIF FocalLength tag and compute the value from it

# TODO print the computed focal length as float value

# TODO Close the file

# TODO Read the file as an OpenCV image

# TODO Extract image resolution

# TODO Compute fx, fy, cx, cy using sensor size information as proposed here:
# http://phototour.cs.washington.edu/focal.html
# focal length in pixels = (image width in pixels) * (focal length in mm) / (CCD width in mm)
# Exemplary iPhone 8 image sensor size from https://www.dpreview.com/forums/thread/4206729 and
# https://en.wikipedia.org/wiki/Image_sensor_format#Table_of_sensor_formats_and_sizes
# Type  Diagonal (mm) 	Width (mm) 	Height (mm) 	Aspect Ratio
# 1/3"  6.00 	        4.80       	3.60        	4:3

# TODO define camera intrinsic matrix K

# TODO print(K)
>>>>>>> 59a7c87fc9f45ce608c0f771e6eb36d1e8fb94aa
