#!/usr/bin/python3

import array
from PIL import Image


image = Image.open('dog.ppm')
var = image.readline()
print("esto es: ",var)


new_image = image.resize((400, 400))
new_image.save('image_400.ppm')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)
print(image.mode)