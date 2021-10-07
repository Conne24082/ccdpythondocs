#Conner Dorsey
#Make a program that places a randomly colored wool block

'''
Set up pgoram for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of diffrent colored wool
Define a function called placeNext
    - it takes one argument called direction
    - it changes the counter by adding the direction argument
    - place a wool block of the color from the list where
      the index matches the counter variable
    - if the counter is out of bounds of the index, reset it
In a forever loop:
    - if the first button was pressed, placeNext(-1)
    - if the second button was pressed, placeNext(-1)
'''
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
woolColors = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def placeNext(direction):
    global counter
    counter += direction
    if counter >= 15:
        counter = 0
    if counter < 0:
        counter = 15
    mc.setBlock(-88,0,-49, 35, woolColors[counter])
def placeNextToP(direction):
    global counter
    counter += direction
    if counter >= 15:
        counter = 0
    if counter < 0:
        counter = 15
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x-5, pos.y-1, pos.z-5, pos.x+5, pos.y, pos.z+5, 35, woolColors[counter])
def buildHouse(direction):
    global counter
    pos = mc.player.getTilePos()
    if counter >= 15:
        counter = 0
    if counter < 0:
        counter = 15
    counter += direction
    mc.setBlocks(pos.x-5, pos.y-1, pos.z-5, pos.x+5, pos.y+3, pos.z+5, 35, woolColors[counter])
    mc.setBlocks(pos.x-4, pos.y, pos.z-4, pos.x+4, pos.y+2, pos.z+4, 0, woolColors[counter])

while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
        time.sleep(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
        time.sleep(1)
    elif GPIO.input(19) == GPIO.LOW:
        buildHouse(1)
    elif GPIO.input(26) == GPIO.LOW:
        buildHouse(-1)