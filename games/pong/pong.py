#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *
import time
import math
import sys
from pikiclasses import *

version = 'v0.1'

class GameWindow(object):
	"Game window object"

	def __init__(self):
		# Starting PyGame

		pygame.init()
		pygame.key.set_repeat(1, 10)
		pygame.display.set_caption("Pong "+version, "")
		self.root = pygame.display.set_mode((800, 600))

class Paddle(object):
	"Simple paddle"

	def __init__(self, x, y, file):
		self.x, self.y, self.file = x, y, file
		# Load the files
		self.surface = pygame.image.load(self.file).convert_alpha()
		# Collision box shape
		self.rect = pygame.Rect(self.x, self.y, self.surface.get_size()[0], self.surface.get_size()[1])

	def blit(self, window):
		window.root.blit(self.surface, (self.x, self.y))

	def ascend(self, var):
		if (self.y+var > 0 and self.y+var < 472):
			self.y += var
			self.rect.move_ip(0, var)

class Ball(object):
	"Textured ball dynamic vector object"

	def __init__(self, file='games/pong/ball.png'):
		# Vector components
		self.x = 400.0       # x coordinate
		self.y = 300.0       # y coordinate
		self.direction = 45   # Polar direction, starting from right to bottom, in degrees
		self.speed = 15       # Speed, in pixel per tick

		# Loading the file surface
		self.file = file
		self.surface = pygame.image.load(self.file).convert_alpha()

		# Collision box shape
		self.rect = pygame.Rect(self.x, self.y, self.surface.get_size()[0], self.surface.get_size()[1])

	def blit(self, window):
		window.root.blit(self.surface, (self.x, self.y))

	def move(self,paddleleft,paddleright):
		dx = math.cos(2*math.pi*self.direction/360) * self.speed
		dy = math.sin(2*math.pi*self.direction/360) * self.speed
		self.x += dx
		self.y += dy

		# top and bottom collision
		if (self.y < 0 or self.y > 568):
			self.direction = -self.direction

		# paddle collision
		self.rect = pygame.Rect(self.x, self.y, self.surface.get_size()[0], self.surface.get_size()[1])
		if paddleleft.rect.colliderect(self.rect):
			if self.direction >= 0: 
				self.direction = 180-self.direction
			if self.direction <= 0: 
				self.direction = -180-self.direction
		if paddleright.rect.collidepoint(self.x, self.y):
			if self.direction >= 0: 
				self.direction = 180-self.direction
			if self.direction <= 0: 
				self.direction = -180-self.direction

		global left, right
		# Out of game
		if self.x > 800:
			self.reset()
			left += 1
		if self.x < 0:
			self.reset()
			right += 1

	def reset(self):
		self.x = 400.0
		self.y = 300.0

def menu(window):
	# Calculate Frame fonction
	def calculate():
		court.blit(window)
		solobutton.blit(window)
		pygame.display.flip()

	court = Background(file='games/pong/court.png')
	solobutton = GameButton(file='games/pong/paddle_grey.png', hover='games/pong/paddle_blue.png', x=520, y=292, action='leaderboards')


	while True:
		for event in pygame.event.get():
			# On mouse motion
			if event.type == QUIT:
				return(0)
			if event.type == MOUSEMOTION:
				for button in buttons:
					if button.rect.collidepoint(pygame.mouse.get_pos()):
						button.setHovered()
					else:
						button.setHovered(False)
		calculate()


def run():
	while True:
		window = GameWindow()
		menu(window)
		# Calculate Frame fonction
		def calculate():
			court.blit(window)
			paddle_left.blit(window)
			paddle_right.blit(window)
			ball.blit(window)
			score_left.blit(window)
			score_right.blit(window)
			pygame.display.flip()

		global left, right
		left = 0
		right = 0
		court = Background(file='games/pong/court.png')
		score_left = Text(text=str(left), x=335, y=40, size=60, font='games/pong/cinnabar.ttf')
		score_right = Text(text=str(right), x=425, y=40, size=60, font='games/pong/cinnabar.ttf')
		paddle_left = Paddle(x=15,y=230,file='games/pong/paddle_blue.png')
		paddle_right = Paddle(x=753,y=230,file='games/pong/paddle_green.png')
		ball = Ball()

		while True:
			# Framerate calculator
			timer = pygame.time.get_ticks()

			ball.move(paddle_left, paddle_right)
			for event in pygame.event.get():
				# On close
				if event.type == QUIT:
					return 0
				if event.type == KEYDOWN:
					keys = pygame.key.get_pressed()
					if keys[K_UP]:
						paddle_right.ascend(-15)
					if keys[K_DOWN]:
						paddle_right.ascend(15)
					if keys[K_z]:
						paddle_left.ascend(-15)
					if keys[K_s]:
						paddle_left.ascend(15)
			calculate()

			# Framerate calculator wait for CPU optimitzation
			timeover = pygame.time.get_ticks()-timer
			towait = 14-timeover # Miliseconds to wait before beeing synchronized with 60 fps
			if towait > 0: 
				time.sleep(towait/1000)

