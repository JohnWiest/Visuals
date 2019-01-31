import pygame
import math
import random
import sys
import os

pygame.init()

def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen = pygame.display.set_mode((2560,1440),pygame.FULLSCREEN)
	sun = pygame.image.load("sun.png")
	boundary_f = pygame.image.load("boundary.png")
	center_f = pygame.image.load("center.png")
	center = [1208,648]
	p = [0,0] 
	v = [0,0]
	a = [0,0]
	data_p = 0
	data_v = 0
	data_a = 0
	time_s = 0
	t_initial = 0
	obj_motion = [p,v,a]
	images = [sun,data_p,data_v,data_a,time_s,boundary_f,center_f] 
	
	
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
		if pygame.mouse.get_pressed()[0]:
			obj_motion[0][0] = pygame.mouse.get_pos()[0] - 72
			obj_motion[0][1] = pygame.mouse.get_pos()[1] - 72
			obj_motion[1][0] = 0
			obj_motion[1][1] = 0


		#Run Functions
		conditions_2(obj_motion,center,t_initial)
		moveObject(obj_motion)
		onScreenData(images,obj_motion)
		updateScreen(images,obj_motion,screen)
	#Game Quits after the while loop is broken
	pygame.quit()
	return

def moveObject(obj_motion):
	for i in range(2):
		obj_motion[1][i] += obj_motion[2][i]
		obj_motion[0][i] += obj_motion[1][i]
	return obj_motion

def onScreenData(images,obj_motion):
	font = pygame.font.SysFont("comicsansms",30)
	images[1] = font.render("Position X :"+str(round(obj_motion[0][0],2)) +", Y: "+str(round(obj_motion[0][1],2)),True,(255,255,255),(0,0,0))
	images[2] = font.render("Velocity X :"+str(round(obj_motion[1][0],2)) +", Y: "+str(round(obj_motion[1][1],2)),True,(255,255,255),(0,0,0))
	images[3] = font.render("Acceleration X :"+str(round(obj_motion[2][0],2)) +", Y: "+str(round(obj_motion[2][1],2)),True,(255,255,255),(0,0,0))
	images[4] = font.render("Time: "+str(round(pygame.time.get_ticks()/1000,2))+" s",True,(255,255,255),(0,0,0))
	return images

def updateScreen(images,obj_motion,screen):
	screen.fill((0,0,0))
	screen.blit(images[0],(obj_motion[0][0],obj_motion[0][1]))
	screen.blit(images[1],(0,0))
	screen.blit(images[2],(0,40))
	screen.blit(images[3],(0,80))
	screen.blit(images[4],(0,120))
	screen.blit(images[5],(560,0))
	screen.blit(images[6],(1255,695))
	pygame.display.update()

def conditions_1(obj_motion,center):
	#these are the initial conditions
	if obj_motion[2] == [0,0] and obj_motion[1] == [0,0] and obj_motion[0] == [0,0]:
		obj_motion[0][0] = center[0]
		obj_motion[0][1] = center[1]
		obj_motion[1] = [20, 20]
		obj_motion[2] = [-0.5, -0.5]
		return obj_motion

	elif obj_motion[0][0]-center[0] > 0 and obj_motion[1][0] > 0 and obj_motion[2][0] > 0 or obj_motion[0][0]-center[0] < 0 and obj_motion[1][0] < 0 and obj_motion[2][0] < 0:
		print("working")
		obj_motion[2][0] = -obj_motion[2][0]

	elif obj_motion[0][1]-center[1] > 0 and obj_motion[1][1] > 0 and obj_motion[2][1] > 0 or obj_motion[0][1]-center[1] < 0 and obj_motion[1][1] < 0 and obj_motion[2][1] < 0:
		print("working")
		obj_motion[2][1] = -obj_motion[2][1]
	
	return obj_motion

def conditions_2(obj_motion,center,t_initial):
	#two concentric electric fields
	#initial conditions
	k = 1000000
	c = 1000000
	print(int(obj_motion[0][0]))
	print(obj_motion[1][0])
	if obj_motion[2] == [0,0] and obj_motion[1] == [0,0] and obj_motion[0] == [0,0]:
		obj_motion[0][0] = 1208
		obj_motion[0][1] = 120
		obj_motion[1] = [2, 0]
	if pygame.time.get_ticks() >= 1000 and int(obj_motion[0][0]) == 1208 and obj_motion[1][0] > 0:
		period = (round(pygame.time.get_ticks(), 2) - t_initial)/1000
		print(period)
		t_initial = round(pygame.time.get_ticks(), 2)
	#acceleration due to the electric fields
	radial_acc = ((c/((obj_motion[0][0]-center[0])**2+(obj_motion[0][1]-center[1])**2))-(k/(700-math.sqrt((obj_motion[0][0]-center[0])**2+(obj_motion[0][1]-center[1])**2))**2))
	obj_motion[2][0] = radial_acc*(obj_motion[0][0]-center[0])/math.sqrt((obj_motion[0][0]-center[0])**2+(obj_motion[0][1]-center[1])**2)
	obj_motion[2][1] = radial_acc*(obj_motion[0][1]-center[1])/math.sqrt((obj_motion[0][0]-center[0])**2+(obj_motion[0][1]-center[1])**2)
	return obj_motion
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