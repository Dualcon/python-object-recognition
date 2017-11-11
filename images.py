#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx

import numpy


# scale images, preserving the aspect ratio:

def scale_bitmap(bitmap, width, height):
	image = bitmap.ConvertToImage()
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	bitmap = wx.Image.ConvertToBitmap(image, depth=-1)
	return bitmap


def scaleImage(bitmap, width, height):
	W = bitmap.GetWidth()
	H = bitmap.GetHeight()
	if W > H:
		NewW = width
		NewH = width * H / W
	else:
		NewH = height
		NewW = height * W / H
	bitmap = scale_bitmap(bitmap, NewW, NewH)
	return bitmap



# Convert images:

def fromRGBToBitmap(width, height, frame):
	bitmap = wx.Bitmap.FromBuffer(width, height, frame)
	return bitmap


# Save to file:

def bitmapToFile(bitmap, name):
	wx.Bitmap.SaveFile(bitmap, name, wx.BITMAP_TYPE_JPEG, palette=None)


# Load from file:
def imageFromFile(path):
	image = wx.Image(path, wx.BITMAP_TYPE_ANY)
	return image