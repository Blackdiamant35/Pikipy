#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

import time
import pygame
from pygame.locals import *
import sys

# Software version
version = 'v0.1'

# Basic sound manager
class MenuSound(object):
	"Basic sound system"

	def __init__(self):
		pygame.mixer.music.load('menu.mp3')
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)

	def stop(self):
		pygame.mixer.music.stop()

	def resume(self):
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)

class Background(object):
	"Window of the main menu"

	def __init__(self,file='bg1.gif'):
		self.image = pygame.image.load(file)

	def blit(self,window):
		window.root.blit(self.image, (0,0))

class GameButton(object):
	"Game button object"

	def __init__(self,file='button.png',x=0,y=0,action='myGame'):
		self.file, self.x, self.y, self.action = file, x, y, action
		# Load the file
		self.button = pygame.image.load(file).convert_alpha()
		# Collision box shape
		self.rect = pygame.Rect(self.x, self.y, self.button.get_size()[0], self.button.get_size()[1])
		print('New button : '+self.action+', Collision Box='+str(self.rect))

	def blit(self,window):
		window.root.blit(self.button, (self.x, self.y))

class MenuWindow(object):
	"Game window object"

	def __init__(self):
		# Starting PyGame
		pygame.init()
		pygame.key.set_repeat(1, 10)
		self.root = pygame.display.set_mode((640, 480))

def runMenu():
	# Create window & sound object
	window = MenuWindow()
	sound = MenuSound()

	# Insert background
	bg = Background(file='bg1.gif')
	bg.blit(window)

	# Snake button
	snakebutton = GameButton(file='perso.png', x=100, y=100, action='snake')
	snakebutton.blit(window)

	# Window state
	active = True

	# Main loop
	while active:
		for event in pygame.event.get():
			# On close
			if event.type == QUIT:
				sys.exit('Closed app : pikipy')
			# On mouse motion
			if event.type == MOUSEMOTION:
				if snakebutton.rect.collidepoint(pygame.mouse.get_pos()):
					print('hovered')

		pygame.display.flip()
		time.sleep(0.1)
