# WEEK 02 PREPARATION ACTIVITY

x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)

# Example 6

# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
length = len(text1)

# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper()

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)

# While it's usually a good practice, you don't have to store the value that is returned
#  from a function in a variable. Sometimes you will see it used directly as shown in example 7 at lines 10, 14, and 16.

# Example 7

import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and
# immediately print its return value.
print( math.sqrt(number) )

# Call the math.sqrt function again and
# use its return value in an if statement.
if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

# INSTEAD OF CALLING THE ROOT FUNCTION ALL THE TIME ITS BEST YOU STORE THE FUNCTION ALONG WITH ITS ARGUMENT IN A VARIABLE
# So it would be faster to save the result in a variable and reuse the variable instead, as shown in EXAMPEL 8

# Example 8

import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and store its
# return value in a variable to use later.
root = math.sqrt(number)

print(f"The square root is {root:.2f}")

if root < 100:
    print(f"The square root is less than 100.")
elif root > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

# END OF WEEK 2 PREPARATION ACTIVITY............................................................................................
