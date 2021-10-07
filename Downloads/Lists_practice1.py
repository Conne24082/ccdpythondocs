#Conner Dorsey
#List Practice 1

#A variable that holds more than one value is a list
#groceries = ['bread', 'milk', 'egg', 'cheese']
#You can get item from a list by their index
#print(groceries[2])

#Start an empty list
#cart = []

#For every item in my grocery list, add to my cart
#for item in groceries:
#    cart.append(item)
#print(cart)


import requests

import time

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


# Setup each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import random
randomNumber = random.randint(0,3)
joke = ['Your mom', "Your're mom", 'SHE LOOK LIKE A MICTHUGIT', 'bim bop bow, you are now a cow']

while True:
    #Check the first button
    #Wait for one second
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        print(joke[randomNumber])