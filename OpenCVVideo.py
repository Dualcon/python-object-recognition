#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading

import numpy as np
import cv2

import files
import OpenCVImages


class Video(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

		self.path = None
		self.capture = False
		self.recognize = False
		self.handle = files.load("tensor", "./tensorflow/classify.py")

		self.panel = None


	def run(self):
		self.cap = cv2.VideoCapture(self.path)

		if (not self.cap.isOpened()):
			self.capture = False
			print("Video not started.")
			return

		while(self.capture == True):
				ret, frame = self.cap.read()

				# Convert from BGR to RGB:
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				h, w = frame.shape[:2]

				self.panel.onVideoFile(w, h, frame)

				# Recognize object with Tensorflow:
				if (self.recognize == True):
					self.classify(frame)

		self.cap.release()
		cv2.destroyAllWindows()
		self.do_run = False


	def classify(self, image):
		image = OpenCVImages.toString(image)
		str = self.handle.recognizeFromImageBuffer(image, 5, 0.1)
		if (str != None):
			screeReaderHandle = files.load("screenreader", "./screenreader/screenreader.py")
			screeReaderHandle.say(str)
			print(str)


video = Video()

def start(panel, status, path):
	global video
	p = panel
	if status == True:
		video.path = path
		video.capture = True
		video.panel = panel
		video.start()
	elif status == False:
		video.path = None
		video.capture = False
		video = Video()


def recognize():
	global video
	if (video.recognize == True):
		video.recognize = False
	elif (video.recognize == False):
		video.recognize = True
	return video.recognize
