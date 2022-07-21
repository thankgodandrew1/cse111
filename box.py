"""
A manufacturing company needs a program that will help
its employees pack manufactured items into boxes for 
shipping. Write a Python program named boxes.py that
asks the user for two integers:

Your program must compute and print the number of boxes 
necessary to hold the items. This must be awhole number.
 Note that the last box may be packed with fewer items than the other boxes.
"""
# imports math to use the ceil function
import math

# requires user input to know amunt of items and amount of items needed in a box

items = int(input('What is the number of manufactured items? '))
user_item = int(input('What is the number of items a user will pack per box? '))

# calls in the ceil function

number_box = math.ceil(items / user_item)

#the below code creates a blank line
print()


print(f'For {items} items, packing {user_item} items in each box, you will need {number_box} boxes')
