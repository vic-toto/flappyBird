import pygame
import random

pygame.init()

#initialise game screen and global variables
gameScreen = pygame.display.set_mode((400, 750)) #set_mode(width, height)
screenWidth, screenHeight = gameScreen.get_size()
FPS = 50 #Frames per second
FORWARD_VELOCITY = 3

def init():
    global birdx, birdy, birdVelY, baseX
    birdx, birdy = 60, 150
    birdVelY = 0
    baseX = 500

init()

#adding elements to screen
def draw():
    gameScreen.blit(background, (0,0))
    gameScreen.blit(bird, (birdx, birdy))
    gameScreen.blit(base, (baseX, 700))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)



#create variables and set paths to assets
background = pygame.image.load('assets/townsville.png')
background = pygame.transform.scale(background, (screenWidth, screenHeight))
bird = pygame.image.load('assets/buttercup.png')
bird = pygame.transform.scale(bird, (100, 100))  # example bird size, change as necessary
base = pygame.image.load('assets/base.png')
base = pygame.transform.scale(base, (baseX, 200))
gameover = pygame.image.load('assets/gameover.png')
gameover = pygame.transform.scale(gameover, (screenWidth, screenHeight))
highTube = pygame.image.load('assets/highTube.png')
highTube = pygame.transform.scale(highTube, (screenWidth, screenHeight))  # example tube size, change as necessary
lowTube = pygame.image.load('assets/lowTube.png')
lowTube = pygame.transform.scale(lowTube, (screenWidth, screenHeight))



while True: 
    baseX -= FORWARD_VELOCITY
    if baseX < -45 : baseX = 0
    #gravity
    birdVelY += 1
    birdy += birdVelY

    #rules
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN 
            and event.key == pygame.K_UP ) :
            birdVelY = -10                      #manages bird movement
        if (event.type == pygame.QUIT):
            pygame.quit()                       #manages closing the gameScreen

    #update screen
    draw()
    update()
