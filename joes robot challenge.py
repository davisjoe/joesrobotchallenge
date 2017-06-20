#Joe's Robot Challenge
import pygame, sys
from pygame.locals import *

import usb.core
import RPi.GPIO as GPIO
import time, random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

pygame.init()
#print(pygame.font.get_fonts())
gameFont = pygame.font.SysFont("roboto", 172, True)



FPS = 90 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
width = 1600
height = 1000
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Joe\'s Robot Challenge')

SNOW = (255, 255, 255)
#catImg = pygame.image.load('cat.png')
x = 10
y = 10
speed = 50
direction = 'right'
puckWidth = 100
puckHeight = 100


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
    pygame.draw.rect(DISPLAYSURF, (255,0,0), (x, y, puckWidth, puckHeight))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    if dev.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=500)[0] :
      print ("Pressed at x = ", x)
      pressed = True

#clear motor signals
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)



#forward (right wheel)
#GPIO.output(9, 0)
#GPIO.output(10, 1)

#forward (left wheel)
#GPIO.output(7, 0)
#GPIO.output(8, 1)

xpercent = (x/width) * 100
print ("total x%", xpercent)
middle = width / 2
if (x == middle) :
    x+=1
if (x < middle) :
    print("left")
    xpercent = (x/middle) *100
    print ("left x %", xpercent)
else :
    print("right")
    xpercent = ((x-middle)/middle) * 100
    print ("right x%",xpercent)


text = gameFont.render("Positioning Robot", True, (0,0,0))

initialT = pygame.time.get_ticks()
delayMS = 5000

intime=True
textx = 100
texty = 300
rrange = 40
while intime: # the robot positioning loop
    DISPLAYSURF.fill(SNOW)
    textxr = textx - (rrange/2) + random.randrange(0,rrange)
    textyr = texty - (rrange/2) + random.randrange(0,rrange)
    DISPLAYSURF.blit(text, (textxr ,textyr))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(12)
    if (initialT + delayMS) < pygame.time.get_ticks() :
        print("time elapsed")
        intime = False
        
x = 10
y = 10
speed = 50
direction = 'down'
puckWidth = 100
puckHeight = 100      
pressed = False

while not pressed: # the up-down loop
    DISPLAYSURF.fill(SNOW)

    if direction == 'down':
        y += speed
        if y >= height:
            direction = 'up'

    elif direction == 'up':
        y -= speed
        if y <= 10:
            direction = 'down'


    #DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.draw.rect(DISPLAYSURF, (255,0,0), (x, y, puckWidth, puckHeight))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    if dev.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=500)[0] :
      print ("Pressed at y = ", y)
      pressed = True

ypercent = (y/height) * 100
print ("total y%", (100-ypercent))

            
#clear motor signals
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)
GPIO.cleanup()

pygame.quit()
