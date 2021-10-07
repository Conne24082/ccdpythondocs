import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
counter = 0
woolColors = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(13) == GPIO.LOW:
        #pos = mc.player.getTilePos()
        #blockid()
        pos = mc.player.getTilePos()
        mc.setBlocks(pos.x-7, pos.y-5, pos.z-7, pos.x+7, pos.y+6, pos.z+7, 0)