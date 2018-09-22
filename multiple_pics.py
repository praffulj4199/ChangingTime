from PIL import Image
import glob
import cv2

from edit import convert 
image_list = []
print("Enter an offset(h, m, s, sign)")
h, m, s, sign = input().split()
h = int(h)
m = int(m)
s = int(s)
print(h)
print(m)
print(s)
print(sign)
for filename in glob.glob('*.jpg'): #assuming gif
    convert(filename, (h, m, s), sign)

#print (image_list)

