#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading

import numpy as np
import cv2

import files
import OpenCVImages

class Camera(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

		self.cap = cv2.VideoCapture(0)

		self.capture = False
		self.recognize = False
		self.handle = files.load("tensor", "./tensorflow/classify.py")

		self.panel = None


	def run(self):
		if (not self.cap.isOpened()):
			camera.capture = False
			print("Camera not started.")
			return

		while(self.capture == True):
				ret, frame = self.cap.read()

				# Save image to file:
				#cv2.imwrite("frame.jpg", frame)

				# Convert from BGR to RGB:
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

				h, w = frame.shape[:2]
				self.panel.onCameraCapture(w, h, frame)

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


camera = Camera()

def capture(panel, status):
	global camera
	p = panel
	if status == True:
		camera.capture = True
		camera.panel = panel
		camera.start()
	elif status == False:
		camera.capture = False
		camera = Camera()


def recognize():
	global camera
	if (camera.recognize == True):
		camera.recognize = False
	elif (camera.recognize == False):
		camera.recognize = True
	return camera.recognize
