#!/usr/bin/python

import RPi.GPIO as GPIO
import minecraft
import block
import time

# The pin number used for input
pin = 18

# set the pin mode and default state
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# connect to the local Minecraft server
mc = minecraft.Minecraft.create()
mc.postToChat("Hello from the  Minecraft API :)")
time.sleep(10)
mc.postToChat('Press your hardware button for some new flooring')

# control loop
while True:
	
	buttonInput = GPIO.input(pin)
  	if buttonInput == GPIO.LOW:
		#print('input low')
		time.sleep(0.05)
  	else:
		print('button pressed!')
                # find the players location in minecraft
		playerTilePos = mc.player.getTilePos()
		# create a dimond pad 10 x 10 under the player
		mc.setBlocks(playerTilePos.x - 5, playerTilePos.y - 1, playerTilePos.z - 5, playerTilePos.x + 5, playerTilePos.y -1, playerTilePos.z + 5, block.DIAMOND_BLOCK)
                time.sleep(0.20) # really rough button debounce


