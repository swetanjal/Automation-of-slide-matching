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
    processed_img = img # cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.filter2D(processed_img, -1, kern)
    ret,processed_img = cv2.threshold(processed_img, 200, 255,cv2.THRESH_BINARY_INV)
    return processed_img

def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def xcorr2(IMG1, IMG2):
    # ORB Detectors
    ORB = cv2.ORB_create()
    KP1, DS1 = ORB.detectAndCompute(IMG1, None)
    KP2, DS2 = ORB.detectAndCompute(IMG2, None)

    #Brute Force Matching
    BF = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches = BF.match(DS1, DS2)
    matches = sorted(matches, key = lambda x: x.distance)

    #drawing matcehs
    matching_result = cv2.drawMatches(IMG1, KP1, IMG2, KP2, matches[:75], None, flags = 2)
    res = 0
    threshold = 75
    cnt = 0
    for m in matches:
        cnt = cnt + 1
        res = res + m.distance * m.distance
        if cnt == threshold:
            break
    return res

path_to_slides = sys.argv[1]
path_to_frames = sys.argv[2]

original_slides = []
original_slides_names = []
frames = []
frames_names = []
matched_slide = []

def addSlide(path, name):
    original_slides.append(preprocess(cv2.imread(path, cv2.IMREAD_GRAYSCALE)))
    original_slides_names.append(name)
def addFrame(path, name):
    frames.append(preprocess(cv2.imread(path, cv2.IMREAD_GRAYSCALE))) 
    frames_names.append(name)


for r, d, f in os.walk(path_to_slides):
    for file in f:
        addSlide(os.path.join(r, file), file)

for r, d, f in os.walk(path_to_frames):
    for file in f:
        addFrame(os.path.join(r, file), file)
ccc = 0
for frame in frames:
    res = 1000000000000000000000000000000000000000000000000000000000000
    pos = -1
    counter = 0
    for slide in original_slides:
        tmp = xcorr2(frame, slide)
        if tmp <= res:
            res = tmp
            pos = counter
        counter += 1
    print(frames_names[ccc] + " " + original_slides_names[pos])
    matched_slide.append(pos)
    ccc = ccc + 1
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
