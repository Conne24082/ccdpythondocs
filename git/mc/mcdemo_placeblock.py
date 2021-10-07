'''
mcdemo_placeblock.py
Get the player tile position and save it to a variable
Use the function to place a block under your current position
(under you is Y - 1)
'''
import requests

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP):
    while True:
    #Check the first button
    #Wait for one second
        time.sleep(1):
            from mcpi.minecraft import Minecraft
            mc = Minecraft.create()
            pos = mc.player.getTilePos()
            mc.setBlock(pos.x, pos.y - 1, pos.z, 0, 0)