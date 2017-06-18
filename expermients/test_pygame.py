#pygame demo code 
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('Animation')

SNOW = (255, 255, 255)
#catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(SNOW)

    if direction == 'right':
        catx += 50
        if catx >= 900:
            direction = 'down'
    elif direction == 'down':
        caty += 25
        if caty >= 900:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 115
        if caty <= 10:
            direction = 'right'

    #DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.draw.rect(DISPLAYSURF, (255,0,0), (catx, caty, 100, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
