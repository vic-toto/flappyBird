import pygame
import random

pygame.init()

class   Tubes:
    def __init__(self):
        self.x = 300
        self.y = random. randint(20, 50)
    def go_and_draw(self):
        self.x -= FORWARD_VELOCITY
        gameScreen.blit(lowTube, (self.x, self.y-10))
        gameScreen.blit(highTube, (self.x+400, self.y+10))

#initialise game screen and global variables
gameScreen = pygame.display.set_mode((400, 750)) #set_mode(width, height)
screenWidth, screenHeight = gameScreen.get_size()
FPS = 50 #Frames per second
FORWARD_VELOCITY = 3

def init():
    global birdx, birdy, birdVelY, baseX, tube_list
    birdx, birdy = 60, 150
    birdVelY = 0
    baseX = 500
    tube_list = []
    tube_list.append(Tubes())

init()

#adding elements to screen
def draw():
    gameScreen.blit(background, (0,0))
    for t in tube_list:
        t.go_and_draw()
    gameScreen.blit(bird, (birdx, birdy))
    gameScreen.blit(base, (baseX, 700))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def game_over():
    gameScreen.blit(gameover, (100, 300))
    update()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE): #restarts game when press space
                init()
                restart = True
            if (event.type == pygame.QUIT):
                pygame.quit()                       #manages closing the gameScreen


#create variables and set paths to assets
background = pygame.image.load('assets/townsville.png')
background = pygame.transform.scale(background, (screenWidth, screenHeight))
bird = pygame.image.load('assets/buttercup.png')
bird = pygame.transform.scale(bird, (100, 100))  # example bird size, change as necessary
base = pygame.image.load('assets/base.png')
base = pygame.transform.scale(base, (baseX, 200))
gameover = pygame.image.load('assets/gameover.png')
gameover = pygame.transform.scale(gameover, (200, 80))
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
        if tube_list[-1].x < -300: tube_list.append(Tubes())
        if (birdy >= 650):
            game_over()                         #collision with base

    #update screen
    draw()
    update()
