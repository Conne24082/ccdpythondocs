import requests
import random
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
pos = mc.player.getTilePos()
randomNumber = random.randint(0,5)

woolLine = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
woolGrid = [[0]
            [0,1,15,15,15,7,15,7],
            [0,1,14,15,7,7,7,15],
            [0,1,15,14,14,14,15,15],
            [0,15,15,7,8,14,14,14,14,8],
            [0,1,15,14,14,14,15,15],
            [0,1,14,15,7,7,7,15],
            [0,1,15,15,15,7,15,7],
            [0]]
#for i, wool in enumerate(woolLine):
    #print(str(i) + " is the color " + str(wool))
    #mc.setBlock(pos.x + i, pos.y + i, pos.z + i, 35, wool)
for i, row in enumerate(woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x + j + 5, pos.y + i, pos.z, 35, col)

