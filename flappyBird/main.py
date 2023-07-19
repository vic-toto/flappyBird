import pygame
import random

pygame.init()

#create variables and set paths to assets
background = pygame.image.load('assets/townsville.png')
bird = pygame.image.load('assets/bittercup.png')
base = pygame.image.load('assets/base.png')
gameover = pygame.image.load('assets/gameover.png')
highTube = pygame.image.load('assets/highTube.png')
lowTube = pygame.image.load('assets/lowTube.png')

#initialise game screen
gameScreen = pygame.display.set_mode((288, 512)) #set_mode(width, height)

