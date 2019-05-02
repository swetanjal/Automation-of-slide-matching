import cv2
import scipy
import numpy as np
import os
import sys

def kernel(ksize, sigma):
    res = np.zeros((ksize, ksize))
    s = 0
    for i in range(ksize):
        for j in range(ksize):
                a = ((i * i) + (j * j)) / (2.0 * sigma * sigma)
                var = (-1.0 / np.pi * sigma * sigma * sigma * sigma) * (1 - a) * np.exp(-a)
                res[i][j] = var
                s = s + res[i][j] 
    for i in range(ksize):
            for j in range(ksize):
                    res[i][j] = res[i][j] / s
    return res

kern = kernel(100, 3)

def preprocess(img):
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.filter2D(processed_img, -1, kern)
    ret,processed_img = cv2.threshold(processed_img, 200, 255,cv2.THRESH_BINARY_INV)
    return processed_img

def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def xcorr2(im1, im2):
    ret = cv2.matchTemplate(im1, im2, cv2.TM_CCORR_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(ret)
    return maxVal

path_to_slides = sys.argv[1]
path_to_frames = sys.argv[2]

original_slides = []
original_slides_names = []
frames = []
frames_names = []
matched_slide = []

def addSlide(path, name):
    original_slides.append(preprocess(cv2.imread(path)))
    original_slides_names.append(name)
def addFrame(path, name):
    frames.append(preprocess(cv2.imread(path))) 
    frames_names.append(name)


for r, d, f in os.walk(path_to_slides):
    for file in f:
        addSlide(os.path.join(r, file), file)

for r, d, f in os.walk(path_to_frames):
    for file in f:
        addFrame(os.path.join(r, file), file)

for frame in frames:
    res = -1000000000000000000000000000000000000000000000000000000000000
    pos = -1
    counter = 0
    for slide in original_slides:
        tmp = xcorr2(frame, slide)
        if tmp >= res:
            res = tmp
            pos = counter
        counter += 1
    matched_slide.append(pos)
c = 0
output = []
for frame in frames:
    output.append(frames_names[c] + " " + original_slides_names[matched_slide[c]] + "\n")
    c = c + 1
output.sort()
f = open("2017.txt", "w+")
for o in output:
        f.write(o)
f.close()
