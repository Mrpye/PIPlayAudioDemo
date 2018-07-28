import os
import pygame
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Your mp3 file goes here')
buttondown=False
play=False
print "Start"

try:

    while True:
        if(GPIO.input(21)==False):
            if(Play==False and buttondown==False):
                #Play Audio
                pygame.mixer.music.rewind()
                pygame.mixer.music.stop()
                pygame.mixer.music.play()
                buttondown=True
            elif(Play==True and buttondown==False):
                #Stop Audio
                pygame.mixer.music.stop()
                pygame.mixer.music.rewind()
                buttondown=True
        elif(buttondown==True):
            buttondown=False
        sleep(0.1)
except KeyboardInterrupt:
        pass
