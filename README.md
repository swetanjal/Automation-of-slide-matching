# Automation-of-slide-matching
##### Team Members: Teja Sai Dhondu(20171075), Swetanjal Murati Dutta(20171077), Nishant Sharma(20171079)  

## Problem Description:
These days, the demand for online lectures is increasing. For better visual experience,
along with the video of the lecture, soft copy of the slides is also being embedded into the
video. But most of the universities are manually matching slides from the video to the soft
copy which is a laborious task. So the problem statement is to automate this slide matching
process.

So to be more precise, you are given a set of noisy slide images extracted from the video and
a set of slides from the original ppt. You need to build a mapping for each of the sampled
noisy slides with the corresponding original slide.

## Generating Test Data:
- Follow format in ./Data/sample_test.

## Run script:
- python3 20171075\_20171077\_20171079.py path\_to\_slides path\_to\_frames
- The script writes to the file 20171075\_20171077\_20171079.txt which contains the mappings between frames and corresponding slides

## Testing:
- cd Test
- g++ checker.cpp
- ./a.out
- Enter the path to the directory containing \_rolllno\_.txt(the file containing the Ground Truth mappings). Eg: ../Data/sample_test

## Algorithmic details:
- Refer to the report 20171075\_20171077\_20171079.pdf