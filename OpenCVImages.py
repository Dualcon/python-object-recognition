#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2


def loadImageFromFile(path, flag):
	""" read an image.
	The image should be in the working directory or a full path of image should be
	given.
	The Second argument is a flag which specifies the way image should be read.
	cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be
	neglected. It is the default flag.
	cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
	cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
	Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

	Args:
	path: the string with the file path.
	flag: an integer, how the image should be read.


	Returns:
	image: an image object.
	"""
	if (flag == 1):
		image = cv2.imread(path, cv2.IMREAD_COLOR)
	elif (flag == 0):
		image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
	elif (flag == -1):
		image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
	else :
		return None
	return image


def BGRToRGB(image):
	""" Convert from BGR to RGB """
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return image


def toString(image):
	""" Convert from numpy array to string object. """
	string = cv2.imencode('.jpg', image)[1].tostring()
	return string
