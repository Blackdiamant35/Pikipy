#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

import tkinter as tk
import sys

# Software version
version = 'v0.1'

class MenuWindow(tk.Tk):
	"Window of the main menu"
	def __init__(self):
		tk.Tk.__init__(self)
		# Background Image
		self.can = tk.Canvas(self,width=640,height=480,bg='black')
		self.can.pack()
		self.background = tk.PhotoImage(file='bg.gif')
		bg = self.can.create_image(320, 240, image=self.background)

		# Window propreties
		self.wm_title('Pikipy '+version)
		self.resizable(width=False, height=False)
		self.protocol("WM_DELETE_WINDOW", self.close)
		self.mainloop()

	def close(self):
		"Called when user closes window"
		sys.exit('Closed app : pikipy')