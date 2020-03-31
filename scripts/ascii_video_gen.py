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

# This class will store the logical ASCII frames that we generate
# We will be serializing this class to JSON
class AsciiVideo:
    def __init__(self):
        # Meta data containing number of frames
        self.meta = {'nFrames': 0}
        # Actual list of frames
        self.frames = []
    
    # Push a new frame onto the list
    def push(self, frame):
        self.frames.append(frame)
        self.meta['nFrames'] += 1
        return self.meta['nFrames']
    
    # Add additional meta data if required
    def putMeta(self, key : str, value):
        self.meta[key] = value
    
    # Serialize the current object to a JSON string
    def toJson(self):
        # Just a bunch of stuff defining some JSON properties
        # Default is an important property. We need to define how each object will be serialized
        # In our case, the object's dictionary form will be used
        return json.dumps(self,
                default=lambda o: o.__dict__,
                sort_keys=False, indent=4)

# Converts a video into sequence of frames with an applied downscale
def __generate_frames(video, downsize = 10):
    # Read the first frame
    s,f = video.read()
    # Number of frames in the video
    vlen = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # Our logical ASCII frames container
    vid = AsciiVideo()
    # Let's put the dimensions as meta data if required later
    vid.putMeta('dim', [f.shape[1]//downsize, f.shape[0]//downsize])
    
    # TQDM is optional. It provides a progress bar.
    # Alternatively, We can use a simple loop
    # for i in range(vlen):
    for i in tqdm(range(vlen), position=0, leave=True, desc='Generating frames', unit=' frames', bar_format='{l_bar}{bar:25}{r_bar}{bar:-10b}'):
        # Generate an ASCII image using our previous module
        _data = ascii_art_gen.__generate_ascii(f, downsize)
        # Push this frame in our container
        vid.push(_data)
        # Read next frame
        s,f = video.read()
        
    print('=== Task Complete ===')
    # Return serialized JSON form of our AsciiVideo object
    return vid.toJson()

# Main
if __name__ == '__main__':
    # User provides a video file
    file = input('Enter the video file path: ')
    # Same kind of stripping we did for our ASCII image module
    if file[0] == '\"':
        file = file[1:-1]
    # Use open cv to read the video file
    vidcap = cv2.VideoCapture(file)
    # Let's take a downsize as input.
    # Higher value means lower quality but compact size.
    # It's same as the previous module
    d = int(input('Downsize: '))
    # let's generate ;)
    # res will contain the json string
    res = __generate_frames(vidcap, d)
    
    # We provide a file name for our json file
    filename = input('Enter file name: ')
    
    # Let's write it to a new file named filename+_vframes
    with open('..\\' + filename + '_vframes.json', 'w') as file:
        file.write(res)
    
    # Done
    print('Saved! Use player to view')