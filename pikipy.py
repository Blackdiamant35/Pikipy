#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

######################################################
#		- Pikipy -				 
#										 
#	An opensource python based games 	 
#	plateform with community developped  
#	games. 								 
#										 
#	This is the main script to run !	 
#	Have fun !							 
#										 
######################################################


import tkinter as tk
from mainmenu import *
import sys

<<<<<<< HEAD
# Games 
sys.path.append('games/snake')
import snake

=======
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
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

		# Text label
		tk.Label(self, text='Enter a name :').grid(row=0,sticky='s')

		# Text entry
		self.name = tk.Entry(self, width=16)
		self.name.bind("<Return>", self.post)
		self.name.grid(row=1,padx=20,pady=20)

		# Confirmation button
		self.button = tk.Button(self, text='Enter',command=self.post)
		self.button.grid(row=2)

		# Window settings
		self.wm_title('Pikipy')
		self.resizable(width=False, height=False)
		self.protocol("WM_DELETE_WINDOW", self.close)
		self.mainloop()

	def close(self):
		"Called when user closes window"
		sys.exit('Closed app : pikipy')

	# Player Createion function
	def post(self, event=None): # event=None to work with the self.name.bind method that gives an object as arg
		name = self.name.get()
		global user
		user = Player(name)
		print("Added user, name : "+user.getName())
		self.destroy()

<<<<<<< HEAD
# Main program loop
if __name__ == '__main__':
	form = PseudoForm()
	while True:

		game = runMenu(user)

		if game == 'snake':
			print(snake.run())
		elif game == 'pong':
			print('Game not ready to be played sry !')
=======
form = PseudoForm()
runMenu()
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
