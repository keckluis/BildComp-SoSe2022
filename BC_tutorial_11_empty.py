import exifread
import cv2
import numpy as np


# TODO Define  a function to compute a fraction given as string
def _derationalize(rational):
    all = rational.split('/')
    numerator = float(all[0])
    denominator = float(all[1])

    return numerator / denominator

# TODO Open an jpg image file in order to read out the exif data
img_file = 'images/OnePlus7.jpg'
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
sensor_width_mm = 6.4
sensor_height_mm = 4.8
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
