# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:56:25 2020
ASCII Video generator
@author: AFRIDI KAYAL
"""

import cv2
import ascii_art_gen
import json
from tqdm import tqdm
import random as rd

class AsciiVideo:
    def __init__(self):
        self.meta = {'nFrames': 0}
        self.frames = []
        
    def push(self, frame):
        self.frames.append(frame)
        self.meta['nFrames'] += 1
        return self.meta['nFrames']
        
    def putMeta(self, key : str, value):
        self.meta[key] = value
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

def __generate_frames(video, downsize = 10):
    s,f = video.read()
    vlen = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    vid = AsciiVideo()
    vid.putMeta('dim', [f.shape[1]//downsize, f.shape[0]//downsize])
    count = 1
    for i in tqdm(range(vlen), desc='Generating frames', unit=' frames', bar_format='{l_bar}{bar:25}{r_bar}{bar:-10b}'):
        # Process the frame
        _data = ascii_art_gen.__generate_ascii(f, downsize)
        vid.push(_data)
        s,f = video.read()
        count += 1
    print('=== Task Complete ===')
    return vid.toJson()

if __name__ == '__main__':
    file = input('Enter the video file path: ')
    if file[0] == '\"':
        file = file[1:-1]
    vidcap = cv2.VideoCapture(file)
    d = int(input('Downsize: '))
    res = __generate_frames(vidcap, d)
    filename = input('Enter file name: ')
    # Generate Copy of Template
    with open('..\\' + filename + '_vframes.json', 'w') as file:
        file.write(res)
    print('Saved! Use player to view')