#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

import tkinter as tk

class MenuWindow(tk.Tk):
	"Window of the main menu"
	def __init__(self):
		tk.Tk.__init__(self)
		self.background = tk.PhotoImage(file='bg.jpg')
		self.can = tk.Canvas(self,width=640,height=480)
		self.can.pack()
		bg = self.can.create_image(640, 480, image=self.background)
		self.mainloop()