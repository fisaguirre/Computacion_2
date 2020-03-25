#!/usr/bin/python3

import array
 
# PPM header
width = 256
height = 128
maxval = 255
ppm_header = f'P6 {width} {height} {maxval}\n'
# PPM image data (filled with blue)
image = array.array('B', [0, 0, 255] * width * height)

# Save the PPM image as a binary file
with open('blue_example.ppm', 'wb') as f:
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)