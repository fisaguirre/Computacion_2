#!/usr/bin/python

import array
import PIL

from PIL import Image
FILENAME='dog.ppm' #image can be in gif jpeg or png format 
im=Image.open(FILENAME).convert('RGB')
pix=im.load()
w=im.size[0]
h=im.size[1]
for i in range(w):
  for j in range(h):
    print pix[i,j]