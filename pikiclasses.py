### FILE TO IMPORT CONTAINING CORE GAME CLASSES ###
import pygame
from pygame.locals import *
import time
import math

# Buttons object list
buttons = []

class Background(object):
	"Background layer control"

	def __init__(self,file='bg.gif'):
		self.image = pygame.image.load(file)

	def blit(self,window):
		window.root.blit(self.image, (0,0))

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
		print('New button : '+self.action+', Collision Box='+str(self.rect))

	def blit(self,window):
		window.root.blit(self.button, (self.x, self.y))
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

	def __init__(self, x=0, y=0, text='Default text', size=36, color=(255, 255, 255), font=None):
		self.x, self.y, self.text, self.size, self.color = x, y, text, size, color
		self.font = pygame.font.Font(font, size)
		self.content = self.font.render(self.text, 1, self.color)

	def blit(self,window):
		window.root.blit(self.content, (self.x, self.y))

class Title(object):
	"Main title image"

	def __init__(self,file='title.png'):
		self.image = pygame.image.load(file)

	def blit(self,window):
		window.root.blit(self.image, (185,0))