"""
Author: ThankGod Andrew

Purpose: Add code near the end of that program that does the following:

Gets the current date from the computer's operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire
"""

import math

def tire_volume():
    return math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000 
    
width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

print(f'\nThe approximate value is: {tire_volume():.2f} liters')

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Print only the date part of the current date and time.

with open('volume.txt', 'at') as volume_file:
    print(f'{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {tire_volume():.2f}', file=volume_file)



# i think based on my code i have been able to exceed requirements
#  i was able to perform the prompt questions on the assingnents
# 
# I am deeply sorry for turning in my assignment today which is late,
# i initially started this course earlier but fell sick by monday it was severe that 
# i got hospitalized. looking at the screen gives me headache. i will try my best to submit my work earlier this week
# Thanks! 
    