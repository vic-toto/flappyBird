import pygame
import random

pygame.init()

#create variables and set paths to assets
background = pygame.image.load('assets/townsville.png')
bird = pygame.image.load('assets/buttercup.png')
base = pygame.image.load('assets/base.png')
gameover = pygame.image.load('assets/gameover.png')
highTube = pygame.image.load('assets/highTube.png')
lowTube = pygame.image.load('assets/lowTube.png')

#initialise game screen
gameScreen = pygame.display.set_mode((288, 512)) #set_mode(width, height)
FPS = 50 #Frames per second
#adding elements to screen

def init():
    global birdx, birdy, birdVelY
    birdx, birdy = 60, 150
    birdVelY = 0

def draw():
    gameScreen.blit(background, (0,0))
    gameScreen.blit(bird, (birdx, birdy))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

init()

while True: 
    #gravity
    birdVelY += 1
    birdy += birdVelY
    #update screen
    draw()
    update()
