import requests

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


# Setup each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Set pin 10 to be an input pin and set initial value to be
# pulled low (off)

#Start an infinite loop
while True:
    #Check the first button
    #Wait for one second
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    #Check the first button
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    #Check the first button
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    #Check the first button
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")