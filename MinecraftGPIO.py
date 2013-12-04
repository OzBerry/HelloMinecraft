#!/usr/bin/python

import RPi.GPIO as GPIO
import minecraft
import block
import time

# The pin number used for input
pin = 22

# set the pin number mode
GPIO.setmode(GPIO.BOARD)

# set our pin to input mode
GPIO.setup(pin, GPIO.IN)

mc = minecraft.Minecraft.create()
mc.postToChat("Hello From the Minecraft API")
mc.setBlock(0, 10, 0, block.STONE)

buttonStateHasChanged = 0

while True:
  #take a reading
  input = GPIO.input(pin)
  #if the last reading was low and this one high, print
  if ((not buttonStateHasChanged) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)



