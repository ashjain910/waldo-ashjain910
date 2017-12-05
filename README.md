INSTALLATION
============

The program assumes that you are using a python 2.x version and also have a necessary pip version installed.

`pip install -r requirements.txt`

to install the necessary libraries required to run the program.

How to run ?

`python is_cropped_image.py outer1.jpg inner1.jpg`

ASSUMPTIONS
===========

There are a few assumptions that are made when writing this program.

1) It is okay to use a external library like openCV for matching/checking images since its not explicitly mentioned to not use any libraries.
2) The cropped file is always smaller than the original file from which the image is cropped.

LOGIC 
=====

1. First we check if the input arguments are correct
2. After that, we process the file_locations to check if they exist and they are of jpg/JPEG file type.
3. Once we have established that the inputs are valid, we find out which of the images is smaller out of the given two images
4. We use the `matchTemplate()` from openCV to check if the smaller_image is a part of the bigger_image.
5. We extract the location of the smaller_image using `minMaxLoc()` method to output the necessary data.