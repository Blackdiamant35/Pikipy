#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

##########################################
#	     		- Pikipy -				 #
#										 #
#	An opensource python based games 	 #
#	plateform with community developped  #
#	games. 								 #
#										 #
#	This is the main script to run !	 #
#	Have fun !							 #
#										 #
##########################################


import tkinter as tk
import mainmenu

# Creates a player
class Player(object):
	"Informations about user"

	def __init__(self, name='Player 1'):
		# name displayed
		if name == "":
			name="Player 1"
		self.name = name
		# Score in games
		self.scores = {}
		# isAfk, also used when player puts game in pause.
		self.isafk = False

	def getName(self):
		return self.name

# Called when ask player's name
class PseudoForm(tk.Tk):
	"Creates nickname form"

	def __init__(self): 
		tk.Tk.__init__(self)

		tk.Label(self, text='Enter a name :', anchor='center').grid(row=0)

		self.name = tk.Entry(self, width=16)
		self.name.bind("<Return>", self.post)
		self.name.grid(row=1)

		self.button = tk.Button(self, text='Enter', command=self.post)
		self.button.grid(row=2)

		self.mainloop()

	# Player Createion function
	def post(self, event=None): # event=None to work with the self.name.bind method that gives an object as arg
		name = self.name.get()
		global user
		user = Player(name)
		print("Added user, name : "+user.getName())
		self.destroy()

form = PseudoForm()
fen = mainmenu.MenuWindow()