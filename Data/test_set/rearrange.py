import cv2
import sys
import os
path = sys.argv[1]
cnt = 0
slide_cnt = 1
frames = []
slides = []
names = []
for r, d, f in os.walk(path):
    for dir in d:
        if dir == 'slides' or dir == 'frames':
            continue
        for r_, d_, f_ in os.walk(os.path.join(r, dir)):
            t = []
            for file in f_:
                if file == 'ppt.jpg':
                    name = r_ + "/" + file
                    img  = r_ + "/" + file
                    img = cv2.imread(name)
                    cv2.imwrite(r + "/" + "slides/ppt" + str(slide_cnt) + ".jpg", img)
                    names.append("ppt" + str(slide_cnt) + ".jpg")
                    continue
                name = r_ + "/" + file
                img = cv2.imread(name)
                cv2.imwrite(r + "/" + "frames/" + str(cnt) + ".jpg", img)
                t.append(str(cnt) + '.jpg')
                cnt = cnt + 1
            slide_cnt = slide_cnt + 1
            for x in t:
                frames.append(x)
                slides.append(names[len(names) - 1])

c = 0
f = open("_rollno_.txt", "w+")
for frame in frames:
    f.write(frame + " " + slides[c] + "\n")
    c = c + 1
f.close()