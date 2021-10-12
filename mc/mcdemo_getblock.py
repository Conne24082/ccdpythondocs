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

def blockid():
    print(mc.getBlockWithData(pos.x, pos.y - 1, pos.z))

while True:
    pos = mc.player.getTilePos()
    if GPIO.input(6) == GPIO.LOW:
        block = blockid()
        time.sleep(.5)
        #If block is dimond
        #Go sicko mod
        if block == 57:
            mc.player.setPos(pos.x, pos.y+20, pos.z)