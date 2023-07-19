import pygame
import random

pygame.init()

#initialise game screen
gameScreen = pygame.display.set_mode((400, 750)) #set_mode(width, height)
screenWidth, screenHeight = gameScreen.get_size()
FPS = 50 #Frames per second

#create variables and set paths to assets
background = pygame.image.load('assets/townsville.png')
background = pygame.transform.scale(background, (screenWidth, screenHeight))
bird = pygame.image.load('assets/buttercup.png')
bird = pygame.transform.scale(bird, (100, 100))  # example bird size, change as necessary
base = pygame.image.load('assets/base.png')
base = pygame.transform.scale(base, (screenWidth, screenHeight))
gameover = pygame.image.load('assets/gameover.png')
gameover = pygame.transform.scale(gameover, (screenWidth, screenHeight))
highTube = pygame.image.load('assets/highTube.png')
highTube = pygame.transform.scale(highTube, (100, 300))  # example tube size, change as necessary
lowTube = pygame.image.load('assets/lowTube.png')
lowTube = pygame.transform.scale(lowTube, (100, 300))

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

    #rules
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP ) :
            birdVelY = -10
        if (event.type == pygame.QUIT):
            pygame.quit()

    #update screen
    draw()
    update()
