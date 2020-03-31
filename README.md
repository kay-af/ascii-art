# ASCII ART

A set of scripts to generate and view ascii art and videos

You need opencv, scikit image, tqdm (For loading bar) and python3.6 with numpy installed for the generator.
Use FramePlayer.html to view your generated frames.

- https://pypi.org/project/opencv-python/ (Open CV for python)

- https://scikit-image.org/docs/dev/api/skimage.html (Scikit image)

- https://www.python.org/downloads/release/python-360/ (Python 3.6)

- https://pypi.org/project/tqdm/ (TQDM)

# USAGE

If you are on Windows, you can use the converter.bat directly else, launch your shell and navigate to the scripts folder and launch the ascii_art_gen.py or ascii_video_gen.py using python.
You need to provide the video path with or without " " and a downscale factor. The program will ask you for those.
For video, you need to specify the vframe file name too.
The vframe files are generated up one directory. That means they will be present outside the scripts folder.
ascii_art_gen.py uses os module in the main method so it's better to remove the launch code if you are not on windows.
Launch the FramePlayer.html inside Player folder to view your generated video art.

Preview

![](preview.gif)
