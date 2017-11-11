#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import os
import images
import OpenCVVideo


class Panel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.frame = parent

		self.path = None
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


	def onVideoFile(self, width, height, frame):
		bitmap = images.fromRGBToBitmap(width, height, frame)
		W,H = self.GetSize()
		self.image = images.scaleImage(bitmap, W, H)#self.sb1.SetBitmap(bitmap)
		self.Layout()


	def openFile(self, event):
		dirName = os.path.dirname(os.path.abspath(__file__))
		wildcard = "Media Files (*.*)|*.*"
		dlg = wx.FileDialog(
		self, message="Choose a file",
		defaultDir=dirName, 
		defaultFile="",
		wildcard=wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			self.path = path


	def onKey(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_SPACE:
			if self.start == False:
				self.start = True
				OpenCVVideo.start(self, True, self.path)
			else:
				self.start = False
				OpenCVVideo.start(self, False, None)
				self.image = wx.Bitmap(0, 0)
				self.Layout()
		else:
			event.Skip()


	def onRecognition(self, event):
		OpenCVVideo.recognize()
