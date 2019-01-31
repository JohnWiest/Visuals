import pygame
import math
import random
import sys
import os

class object:
	def __init__(self,initial_p,initial_v):
		self.position = [initial_p[0],initial_p[1]]
		self.velocity = [initial_v[0],initial_v[1]]
		self.acceleration = [0,0]
		self.image = pygame.image.load("sun.png")
		self.initial_t = 0
		self.loop = 1

	def move(self):
		for i in range(2):
			self.velocity[i] += self.acceleration[i]
			self.position[i] += self.velocity[i]

	def changeAccel(self,center):
		k = 100000
		c = 100000
		radial_acc = ((c/((self.position[0]-center[0])**2+(self.position[1]-center[1])**2))-(k/(700-math.sqrt((self.position[0]-center[0])**2+(self.position[1]-center[1])**2))**2)) 
		self.acceleration[0] = radial_acc*(self.position[0]-center[0])/math.sqrt((self.position[0]-center[0])**2+(self.position[1]-center[1])**2)
		self.acceleration[1] = radial_acc*(self.position[1]-center[1])/math.sqrt((self.position[0]-center[0])**2+(self.position[1]-center[1])**2)

	def getPosition(self):
		return self.position

	def getVelocity(self):
		return self.velocity

	def getAcceleration(self):
		return self.acceleration

	def getPeriod(self,initial_p):
		if 1274.5 <= self.position[0] <= 1285.5 and self.velocity[0] > 0 and 300 < (pygame.time.get_ticks() - self.initial_t) and pygame.time.get_ticks() > 1000:
			print(self.position[0])
			print(self.velocity[0])
			t = pygame.time.get_ticks()
			print(t)
			period = (t)/(1000*self.loop)
			print(period)
			self.loop += 1
			self.initial_t = t
			return period

