#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

import time
import pygame
from pygame.locals import *
import sys

# Software version
version = 'v0.1'

<<<<<<< HEAD
# Buttons object list
buttons = []

=======
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
# Basic sound manager
class MenuSound(object):
	"Basic sound system"

	def __init__(self):
<<<<<<< HEAD
		self.state = True
=======
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
		pygame.mixer.music.load('menu.mp3')
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)

<<<<<<< HEAD
	def stop(self,soundbutton):
		# Mute sound
		self.state = False
		pygame.mixer.music.stop()
		print('Sound stopped.')

		# Change speaker image
		soundbutton.setFile('sound_off.png', 'sound_off.png')

	def resume(self,soundbutton):
		# Start sound
		self.state = True
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)
		print('Sound resumed.')

		# Change speaker image
		soundbutton.setFile('sound_on.png', 'sound_on.png')

	def getState(self):
		return self.state

class Background(object):
	"Background layer control"
=======
	def stop(self):
		pygame.mixer.music.stop()

	def resume(self):
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)

class Background(object):
	"Window of the main menu"
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6

	def __init__(self,file='bg1.gif'):
		self.image = pygame.image.load(file)

	def blit(self,window):
		window.root.blit(self.image, (0,0))

<<<<<<< HEAD
class Title(object):
	"Main title image"

	def __init__(self,file='title.png'):
		self.image = pygame.image.load(file)

	def blit(self,window):
		window.root.blit(self.image, (185,0))

class GameButton(object):
	"Game button object"

	def __init__(self,file='button.png',hover='button_hovered.png',x=0,y=0,action='myGame'):
		self.file, self.hover, self.x, self.y, self.action = file, hover, x, y, action
		self.hovered = False
		# Load the files
		self.button = pygame.image.load(self.file).convert_alpha()
		self.button_hover = pygame.image.load(self.hover).convert_alpha()
		# Collision box shape
		self.rect = pygame.Rect(self.x, self.y, self.button.get_size()[0], self.button.get_size()[1])
		# Add this button to the buttons object list
		buttons.append(self)
=======
class GameButton(object):
	"Game button object"

	def __init__(self,file='button.png',x=0,y=0,action='myGame'):
		self.file, self.x, self.y, self.action = file, x, y, action
		# Load the file
		self.button = pygame.image.load(file).convert_alpha()
		# Collision box shape
		self.rect = pygame.Rect(self.x, self.y, self.button.get_size()[0], self.button.get_size()[1])
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
		print('New button : '+self.action+', Collision Box='+str(self.rect))

	def blit(self,window):
		window.root.blit(self.button, (self.x, self.y))
<<<<<<< HEAD
		if self.hovered == True:
			window.root.blit(self.button_hover, (self.x, self.y))

	def setHovered(self,state=True):
		self.hovered = state

	def getAction(self):
		return self.action

	def setFile(self, file='button.png',hover='button_hovered.png'):
		self.file, self.hover = file, hover
		self.button = pygame.image.load(self.file).convert_alpha()
		self.button_hover = pygame.image.load(self.hover).convert_alpha()
		self.rect = pygame.Rect(self.x, self.y, self.button.get_size()[0], self.button.get_size()[1])

class Text(object):
	"Basic text"

	def __init__(self, x=0, y=0, text='Default text', size=36, color=(255, 255, 255)):
		self.x, self.y, self.text, self.size, self.color = x, y, text, size, color
		self.font = pygame.font.Font(None, size)
		self.content = self.font.render(self.text, 1, self.color)

	def blit(self,window):
		window.root.blit(self.content, (self.x, self.y))
=======
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6

class MenuWindow(object):
	"Game window object"

	def __init__(self):
		# Starting PyGame
<<<<<<< HEAD

		pygame.init()
		pygame.key.set_repeat(1, 10)
		pygame.display.set_caption("Pikipy "+version, "")
		self.root = pygame.display.set_mode((640, 480))


def runMenu(user):
=======
		pygame.init()
		pygame.key.set_repeat(1, 10)
		self.root = pygame.display.set_mode((640, 480))

def runMenu():
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
	# Create window & sound object
	window = MenuWindow()
	sound = MenuSound()

	# Insert background
	bg = Background(file='bg1.gif')
<<<<<<< HEAD
	title = Title()
	text = Text(x=20,y=420,text='Welcome, '+user.getName(),size=36)
	legend = Text(x=3,y=460,text='The program is in alpha phase, please report bugs @ github.com/Blackdiamant35/Pikipy',size=22,color=(155,155,155))

	##### BUTTONS CONFIGURATION #####

	leaderboardsbutton = GameButton(file='score_off.png', hover='score_on.png', x=520, y=292, action='leaderboards')
	soundbutton = GameButton(file='sound_on.png', hover='sound_on.png', x=575, y=5, action='sound')
	settingsbutton = GameButton(file='settings.png', hover='settings.png', x=610, y=5, action='settings')
	snakebutton = GameButton(file='button_snake.png', hover='button_snake_hovered.png', x=20, y=50, action='snake')
	pongbutton = GameButton(file='button_pong.png', hover='button_pong_hovered.png', x=20, y=130, action='pong')

	##### END BUTTONS CONFIGURATION #####
=======
	bg.blit(window)

	# Snake button
	snakebutton = GameButton(file='perso.png', x=100, y=100, action='snake')
	snakebutton.blit(window)
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6

	# Window state
	active = True

<<<<<<< HEAD
	# Image update function
	def calculate():
		window.root.fill((255,255,255,0))
		bg.blit(window)
		title.blit(window)
		legend.blit(window)
		text.blit(window)
		for button in buttons:
			button.blit(window)
		pygame.display.flip()

=======
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
	# Main loop
	while active:
		for event in pygame.event.get():
			# On close
			if event.type == QUIT:
				sys.exit('Closed app : pikipy')
			# On mouse motion
			if event.type == MOUSEMOTION:
<<<<<<< HEAD
				for button in buttons:
					if button.rect.collidepoint(pygame.mouse.get_pos()):
						button.setHovered()
					else:
						button.setHovered(False)

			# On mouse click
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					# Loop button test
					for button in buttons:
						if button.rect.collidepoint(pygame.mouse.get_pos()):
							if button.getAction() == 'sound':
								if sound.getState() == True:
									sound.stop(soundbutton)
								else:
									sound.resume(soundbutton)
							elif button.getAction() == 'settings':
								print('Setting menu not aviable in this update, try later.')
							else:
								print('ran program: '+button.getAction())
								sound.stop(soundbutton)
								pygame.quit()
								return button.getAction()
								break

		calculate()
		time.sleep(0.1)
=======
				if snakebutton.rect.collidepoint(pygame.mouse.get_pos()):
					print('hovered')

		pygame.display.flip()
		time.sleep(0.1)
>>>>>>> fddd860216c8967b85c8f6ddfa4c882cc94361b6
