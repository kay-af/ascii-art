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

CHARS = ['@', '#', 'm', 'n', 'o', 'L', 'r', '/', '-', '.', ' ']

# Requires normalized values (0 - 1)
def pixel_to_ascii(pixel_val):
    n = len(CHARS) - 1
    k = int(pixel_val * n)
    return CHARS[k]

def __generate_ascii(image, downsize = 10):
    image = rgb2gray(image)
    image = downscale_local_mean(image, (downsize, downsize))
    image /= np.max(image)
    
    ascii_data = ''
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            c = pixel_to_ascii(image[i][j])
            ascii_data += c
        ascii_data += '\n'
    return ascii_data
    

if __name__ == '__main__':
    file = input('Enter the file path: ')
    if file[0] == '\"':
        file = file[1:-1]
    
    image = io.imread(file)
    DOWNSIZE = int(input('Down Size: '))
    data = __generate_ascii(image, DOWNSIZE)
    
    with open('ascii_output.html', 'w') as txtfile:
        ascii_data = template.replace('$ASCII', data)
        txtfile.write(ascii_data)
    os.system('ascii_output.html')
            