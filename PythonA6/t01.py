"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
"""
from functions import get_brightness

wattage = int(input('Lightbulb wattage (w): '))

brightness = get_brightness(wattage)
print(brightness)
