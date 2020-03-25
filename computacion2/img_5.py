#!/usr/bin/python

import array
import PIL

from PIL import Image

FILENAME='dog.ppm' #image can be in gif jpeg or png format 
im=Image.open(FILENAME).convert('RGB')
pix=im.load()
w=im.size[0]
h=im.size[1]
print(w)
print(h)

imprimir rojo verde y azul
armar una imagen con cada componenete(una roja una verde y una azul)
