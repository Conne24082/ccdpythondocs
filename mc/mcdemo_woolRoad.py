import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
counter = 0
woolColors = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def buildHouse(direction):
    global counter
    pos = mc.player.getTilePos()
    if counter >= 15:
        counter = 0
    if counter < 0:
        counter = 15
    counter += direction
    mc.setBlock(pos.x, pos.y-1, pos.z, 35, woolColors[counter])

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6) == GPIO.LOW:
        buildHouse(1)
    if GPIO.input(13) == GPIO.LOW:
        buildHouse(-1)