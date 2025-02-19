"""
Created by: Liya Getachew
Created on: February 19 2025
This makes the LED blink every second.
The blink time increments by 1 every loop.

"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

blink_time = 3000

# loop forever
while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(blink_time)

    blink_time = blink_time + 1000
