#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import images
import OpenCVCamera


class Panel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.frame = parent

		self.start = False

		self.image = wx.Bitmap(0, 0)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_KEY_DOWN, self.onKey)

		# Accelerators
		recognitionID = wx.NewId()
		self.Bind(wx.EVT_MENU, self.onRecognition, id=recognitionID)

		at1 = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord("R"), recognitionID)])
		self.SetAcceleratorTable(at1)

		self.SetBackgroundColour("blue")

		self.sb1 = wx.StaticBitmap(self, wx.ID_ANY)

		sizer1 = wx.BoxSizer(wx.VERTICAL)
		sizer1.Add(self.sb1, 1, wx.ALL|wx.EXPAND, 5)
		self.SetSizerAndFit(sizer1)


	def OnPaint(self, event):
		self.sb1.SetBitmap(self.image)
		#self.Layout()


	def onPaintStaticImage(self, event):
		filename = "./images/ferrari.jpg"
		bitmap = wx.Bitmap(filename)
		W,H = self.frame.GetSize()
		newBitmap = images.scaleImage(bitmap, W, H)
		self.sb1.SetBitmap(newBitmap)
		self.Layout()


	def onCameraCapture(self, width, height, frame):
		bitmap = images.fromRGBToBitmap(width, height, frame)
		W,H = self.GetSize()
		self.image = images.scaleImage(bitmap, W, H)#self.sb1.SetBitmap(bitmap)
		self.Layout()


	def onKey(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_SPACE:
			if self.start == False:
				self.start = True
				OpenCVCamera.capture(self, True)
			else:
				self.start = False
				OpenCVCamera.capture(self, False)
				self.image = wx.Bitmap(0, 0)
				self.Layout()
		else:
			event.Skip()


	def onRecognition(self, event):
		OpenCVCamera.recognize()
