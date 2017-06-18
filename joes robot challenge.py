#pygame demo code 
import pygame, sys
from pygame.locals import *

import usb.core


pygame.init()

FPS = 90 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
width = 800
height = 1000
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Joe\'s Robot Challenge')

SNOW = (255, 255, 255)
#catImg = pygame.image.load('cat.png')
x = 10
y = 10
speed = 50
direction = 'right'


dev = usb.core.find(idVendor=0x1130, idProduct=0x0202)
if not dev :
    print('USB Button is NOT ATTACHED!!')
    exit()
    
try:    
    dev.detach_kernel_driver(0) # Get rid of hidraw
except Exception as e :
    print(e)

    
pressed = False
while not pressed: # the left-right loop
    DISPLAYSURF.fill(SNOW)

    if direction == 'right':
        x += speed
        if x >= width:
            direction = 'left'

    elif direction == 'left':
        x -= speed
        if x <= 10:
            direction = 'right'


    #DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.draw.rect(DISPLAYSURF, (255,0,0), (x, y, 100, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    if dev.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=500)[0] :
      print ("Pressed at x = ", x)
      pressed = True
