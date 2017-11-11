#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx

import GuiVideoPanel
import GuiCameraPanel

import files

class Gui(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Gui, self).__init__(*args, **kwargs) 
		self.InitUI()


	def InitUI(self):

		# Menu bar
		menuBar = wx.MenuBar()

		fileMenu = wx.Menu()
		videoMenuItem = fileMenu.Append(wx.ID_ANY, "&Video", "Video recognition.")
		self.Bind(wx.EVT_MENU, self.onVideo, videoMenuItem)
		cameraMenuItem = fileMenu.Append(wx.ID_ANY, "&Camera", "Real time recognition.")
		self.Bind(wx.EVT_MENU, self.onCamera, cameraMenuItem)
		quitMenuItem = fileMenu.Append(wx.ID_ANY, "&Quit", "Quit application.")
		self.Bind(wx.EVT_MENU, self.onQuit, quitMenuItem)
		menuBar.Append(fileMenu, "&File")

		windowMenu = wx.Menu()
		minimizeMenuItem = windowMenu.Append(wx.ID_ANY, "&Minimize", "Minimize.")
		self.Bind(wx.EVT_MENU, self.onMinimize, minimizeMenuItem)
		maximizeMenuItem = windowMenu.Append(wx.ID_ANY, "&Maximize", "Maximize.")
		self.Bind(wx.EVT_MENU, self.onMaximize, maximizeMenuItem)
		fullScreenMenuItem = windowMenu.Append(wx.ID_ANY, "&Full screen", "Full screen.")
		self.Bind(wx.EVT_MENU, self.onFullScreen, fullScreenMenuItem)
		self.isFullScreen = False
		menuBar.Append(windowMenu, "&Window")

		self.SetMenuBar(menuBar)

		# Panels
		# Add a panel so it looks correct on all platforms
		self.blankPanel = wx.Panel(self, wx.ID_ANY)
		self.blankPanel.Show()
		self.blankPanel.Bind(wx.EVT_KEY_DOWN, self.onKey)

		self.videoPanel = GuiVideoPanel.Panel(self)
		self.videoPanel.Hide()
		self.cameraPanel = GuiCameraPanel.Panel(self)
		self.cameraPanel.Hide()

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.blankPanel, 1, wx.ALL|wx.EXPAND, 5)
		sizer.Add(self.videoPanel, 1, wx.ALL|wx.EXPAND, 5)
		sizer.Add(self.cameraPanel, 1, wx.ALL|wx.EXPAND, 5)
		self.SetSizer(sizer)

		# Accelerators
		openFileID = wx.NewId()
		self.Bind(wx.EVT_MENU, self.onOpenFile, id=openFileID)

		fullScreenID = wx.NewId()
		self.Bind(wx.EVT_MENU, self.onFullScreen, id=fullScreenID)

		at1 = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord("O"), openFileID), 
		(wx.ACCEL_CTRL,  ord("F"), fullScreenID)])
		self.SetAcceleratorTable(at1)

		# Window        
		self.SetSize(800, 600)
		self.SetTitle("Recognition Tool")
		self.Centre()
		self.Show()


	def onQuit(self, e):
		self.Close()


	def onMaximize(self, event):
		self.Maximize(True)
		self.Layout()


	def onMinimize(self, event):
		self.Maximize(False)
		self.Layout()


	def onFullScreen(self, event):
		if self.isFullScreen:
			self.isFullScreen = False
			self.ShowFullScreen(False)
		else:
			self.isFullScreen = True
			self.ShowFullScreen(True)
		#self.Layout()


	def onKey(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_SPACE:
			print ("you pressed the spacebar!")
			handle = files.load("screenreader", "./screenreader/screenreader.py")
			handle.say("Hello")
		elif keyCode == wx.WXK_ESCAPE:
			self.ShowFullScreen(False)
		else:
			event.Skip()


	def onOpenFile(self, event):
		self.videoPanel.openFile(self)


	def onVideo(self, event):
		self.changePanel("VIDEO")


	def onCamera(self, event):
		self.changePanel("CAMERA")


	def changePanel(self, panelName):
		if panelName == "VIDEO":
			self.videoPanel.Show()
			self.blankPanel.Hide()
			self.cameraPanel.Hide()
		if panelName == "CAMERA":
			self.cameraPanel.Show()
			self.blankPanel.Hide()
			self.videoPanel.Hide()
		self.Layout()


def main():
	app = wx.App()
	Gui(None)
	app.MainLoop()    


if __name__ == '__main__':
	main()
