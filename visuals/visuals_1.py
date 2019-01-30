import pygame
import math
import random
import sys
import os
from object import *

pygame.init()

def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen = pygame.display.set_mode((2560,1440),)
	boundary = pygame.image.load("boundary.png")
	center_dot = pygame.image.load("center.png")
	center = [1280,720]
	radial_v = 3

	object1 = object([1280,220],[radial_v,0])
	object2 = object([1780,720],[0,radial_v])
	object3 = object([1280,1220],[-radial_v,0])
	object4 = object([780,720],[0,-radial_v])
	object5 = object([1280,220],[-radial_v,0])
	object6 = object([1780,720],[0,-radial_v])
	object7 = object([1280,1220],[radial_v,0])
	object8 = object([780,720],[0,radial_v])
	objects = [object1,object2,object3,object4,object5,object6,object7,object8]
	
	run = True
	while run:
		pygame.time.delay(1)

		#This allows the game to quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			run = False
		if keys[pygame.K_UP]:
			radial_v += 1
			objectInitialConditions(objects,radial_v)

		if keys[pygame.K_DOWN]:
			radial_v -= 1
			objectInitialConditions(objects,radial_v)


		#Run Functions
		updateScreen(screen,boundary,center_dot,objects)

		for i in range(8):
			objects[i].move()
			object1.getPeriod([object1.getPosition()[0],object1.getPosition()[1]])
			objects[i].changeAccel(center)
			

	#Game Quits after the while loop is broken
	pygame.quit()
	return

def updateScreen(screen,boundary,center_dot,objects):
	screen.fill((0,0,0))
	screen.blit(boundary,(560,0))
	screen.blit(center_dot,(1255,695))
	for i in range(8):
		screen.blit(objects[i].image,(objects[i].getPosition()[0]-72,objects[i].getPosition()[1]-72))
	pygame.display.update()

def objectInitialConditions(objects,radial_v):
	objects[0] = object([1280,220],[radial_v,0])
	objects[1] = object([1780,720],[0,radial_v])
	objects[2] = object([1280,1220],[-radial_v,0])
	objects[3] = object([780,720],[0,-radial_v])
	objects[4] = object([1280,220],[-radial_v,0])
	objects[5] = object([1780,720],[0,-radial_v])
	objects[6] = object([1280,1220],[radial_v,0])
	objects[7] = object([780,720],[0,radial_v])
	return

main()

#the period of the occillations between E fields only depends on the force constants
#the period around the circle only depends on the initial position and velocity
#it would look cool if the period around the circle = n * the period of the one occillation between the fields
#come up with formulas for both periods
#put this to music with multiple other objects

#parameters for minute hand at td(1)
#k = 1000000
#c = 1000000
#obj_motion[0][0] = 1208
#obj_motion[0][1] = 350
#obj_motion[1] = [0.923, 0]