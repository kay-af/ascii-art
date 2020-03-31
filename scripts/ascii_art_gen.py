# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:47:35 2020
Image to ASCII art
@author: AFRIDI KAYAL
"""
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import downscale_local_mean
import os

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>ASCII ART VIEWER</title>
</head>
<body style="white-space: pre-line; text-align: justify; font-family: monospace; line-height: 0.85;">
$ASCII
</body>
</html>'''

# Darkest to Lightest :)
CHARS = ['@', '#', 'm', 'n', 'o', 'L', 'r', '/', '-', '.', ' ']

# This method converts a given pixel value to a symbol
# Requires normalized values (0 - 1)
def pixel_to_ascii(pixel_val):
    n = len(CHARS) - 1
    # Getting the index of the symbol which maps to the chars array based on pixel's intensity
    k = int(pixel_val * n) 
    return CHARS[k]

# Takes an image as input and optional downsize to apply to it
# Default downsize is 10 that means width and height will be downscaled by a factor of 10
def __generate_ascii(image, downsize = 10):
    # convert the image to grayscale
    image = rgb2gray(image)
    
    # downscale the image
    image = downscale_local_mean(image, (downsize, downsize))
    
    # Normalizing the pixel values.
    # Here we are making sure that all the pixels have intensity within range 0 and 1
    image /= np.max(image)
    
    # Our handy string that will actually hold the complete converted data
    ascii_data = ''
    
    # Iterate over each pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Getting the corresponding symbol using picel_to_ascii method
            c = pixel_to_ascii(image[i][j])
            # Append to the result so far
            ascii_data += c
        # Don't forget a new line
        ascii_data += '\n'

    return ascii_data
    
if __name__ == '__main__':
    file = input('Enter the file path: ')
    
    # Strip the extra " if the user provided the path with "
    if file[0] == '\"':
        file = file[1:-1]
    
    # Read the image
    image = io.imread(file)
    
    # Let the user declare a downsize. Higher value means lower quality but compact output
    DOWNSIZE = int(input('Down Size: '))
    
    # Generate the data
    data = __generate_ascii(image, DOWNSIZE)
    
    with open('ascii_output.html', 'w') as txtfile:
        ascii_data = template.replace('$ASCII', data)
        txtfile.write(ascii_data)
    os.system('ascii_output.html')