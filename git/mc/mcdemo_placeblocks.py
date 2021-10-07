#Conner Dorsey
#How to build house ezy lol
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

def buildHouse():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x-5, pos.y-1, pos.z-5, pos.x+5, pos.y+3, pos.z+5, 45)
    mc.setBlocks(pos.x-4, pos.y, pos.z-4, pos.x+4, pos.y+2, pos.z+4, 0)
    mc.setBlocks(pos.x-3, pos.y, pos.z-3, pos.x-5, pos.y+1, pos.z-3, 64)

def blockid():
    print(mc.getBlockWithData(pos.x, pos.y - 1, pos.z))

#Start an infinite loop
while True:
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        buildHouse()
    if GPIO.input(13) == GPIO.LOW:
        #pos = mc.player.getTilePos()
        #blockid()
        pos = mc.player.getTilePos()
        mc.setBlocks(pos.x-7, pos.y-5, pos.z-7, pos.x+7, pos.y+6, pos.z+7, 0)
    if GPIO.input(19) == GPIO.LOW:
        mc.postToChat("Who has entered my realm?")
        time.sleep(1)
    if GPIO.input(26) == GPIO.LOW:
        mc.postToChat("Kekw!")
        time.sleep(1)
