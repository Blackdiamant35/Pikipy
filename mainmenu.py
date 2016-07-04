#!/usr/bin/python3
# -*- Coding:Utf-8 -*-

import time
import pygame
from pygame.locals import *
import sys
from pikiclasses import *

# Software version
version = 'v0.1'


# Basic sound manager
class MenuSound(object):
	"Basic sound system"

	def __init__(self):
		self.state = False
		pygame.mixer.music.load('menu.mp3')

	def stop(self,soundbutton):
		# Mute sound
		self.state = False
		pygame.mixer.music.stop()
		print('Sound stopped.')

		# Change speaker image
		soundbutton.setFile('sound_off.png', 'sound_off.png')

	def play(self,soundbutton):
		# Start sound
		self.state = True
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.3)
		print('Sound played.')

		# Change speaker image
		soundbutton.setFile('sound_on.png', 'sound_on.png')

	def getState(self):
		return self.state

class MenuWindow(object):
	"Game window object"

	def __init__(self):
		# Starting PyGame

		pygame.init()
		pygame.key.set_repeat(1, 10)
		pygame.display.set_caption("Pikipy "+version, "")
		self.root = pygame.display.set_mode((640, 480))


def runMenu(user, alreadyExists=False):
	# Create window & sound object
	window = MenuWindow()
	# Insert background
	bg = Background(file='bg.gif')
	title = Title()
	text = Text(x=20,y=420,text='Welcome, '+user.getName(),size=36)
	legend = Text(x=3,y=460,text='The program is in alpha phase, please report bugs @ github.com/Blackdiamant35/Pikipy',size=22,color=(155,155,155))

	if alreadyExists == False:
		global soundbutton # Necessarry to access this object after.
		##### BUTTONS CONFIGURATION #####

		leaderboardsbutton = GameButton(file='score_off.png', hover='score_on.png', x=520, y=292, action='leaderboards')
		soundbutton = GameButton(file='sound_on.png', hover='sound_on.png', x=575, y=5, action='sound')
		settingsbutton = GameButton(file='settings.png', hover='settings.png', x=610, y=5, action='settings')
		snakebutton = GameButton(file='button_snake.png', hover='button_snake_hovered.png', x=20, y=50, action='snake')
		pongbutton = GameButton(file='button_pong.png', hover='button_pong_hovered.png', x=20, y=130, action='pong')

		##### END BUTTONS CONFIGURATION #####

	# Window state
	active = True
	sound = MenuSound()
	sound.play(soundbutton)

	# Image update function
	def calculate():
		bg.blit(window)
		title.blit(window)
		legend.blit(window)
		text.blit(window)
		for button in buttons:
			button.blit(window)
		pygame.display.flip()

	# Main loop
	while active:
		for event in pygame.event.get():
			# On close
			if event.type == QUIT:
				sys.exit('Closed app : pikipy')
			# On mouse motion
			if event.type == MOUSEMOTION:
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
									sound.play(soundbutton)
							elif button.getAction() == 'settings':
								print('Setting menu not aviable in this update, try later.')
							else:
								game = button.getAction()
								print('ran program: '+game)
								# Stopping sound
								# sound.stop(soundbutton)				
								pygame.quit()
								return game
								break

		calculate()
		time.sleep(0.1)
