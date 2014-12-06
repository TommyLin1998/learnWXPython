#! /usr/bin/evn python

#import the graphical library
import wx

#import the time module
import time
import random

buttons = []

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race")
		
		#Make a new Panel
		self.panel = wx.Panel(self)

		#Make the start button
		self.btnStart = wx.Button(self.panel, label = "Start", pos = (152,100))

		#Make the other ten buttons
		for i in range(1, 11):
                        curBtn = wx.Button(self.panel, label = "Button{}".format(i), pos = (random.randint(0, 300), random.randint(0, 200)))
                        buttons.append(curBtn)
                        curBtn.Bind(wx.EVT_BUTTON, self.OnAnyButton)

		#Hide the other ten buttons
                        curBtn.Show(False)

		#Bind all the buttons to their event handlers
		self.btnStart.Bind(wx.EVT_BUTTON, self.OnStart)
		
	# Event handler for the start button
	def OnStart(self, e):

		#Make the start button disappear
                self.btnStart.Show(False)
		self.startTime = time.time()

		#Make Button One appear
		buttons[0].Show(True)

	#Other event handlers here
	def OnAnyButton(self, e):
                clickedButton = e.GetEventObject()
                clickedButton.Show(False)
                for i in range(10):
                        if clickedButton == buttons[i]:
                                if i<9:
                                        buttons[i+1].Show(True)
                                else:
                                        self.ShowTime(e)

	#Remember the last event handler needs to print the final time.
	def ShowTime(self, e):
                f = open("time.txt", "r+")
                fileContents = float(f.read())
                self.finalTime = time.time()
                self.time = round(self.finalTime - self.startTime, 1)
                wx.StaticText(self.panel, label = "Your time is: {}s".format(self.time))
                
                if self.time < fileContents:
                        f.seek(0)
                        f.write(str(self.time))
                        f.seek(0)
                        fileContents = f.read()
                        
                wx.StaticText(self.panel, label = "Your record is: {}s".format(fileContents), pos = (0, 20))
                
                f.close()

# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()
