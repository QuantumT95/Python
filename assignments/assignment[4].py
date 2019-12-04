"""
Charlie Tran
Assignment #4
COSC 1306
"""

import math  # We'll need this for sqrt to compute the "correct" answer

################################################################################
# Write a function to get a value (float) from the user.
# It should validate that the number is not a negative number.
# If the number is negative, it should request a new number, as needed.
# It should then return the non-negative value.
################################################################################


def get_number():
    number = float(input("please enter a number: "))
    while number < 0:
        print("Invalid value: >>", number, "<< Please enter a positive value.")
        number = float(input("please enter a POSITIVE number: "))
    return number


################################################################################
# Write a function to run Newton's method for computing the square root.
# It should take as an input parameter a number on which to compute the square root.
# It should also take as an inut parameter the number of iterations to complete.
# It should start with a guess of the number/2.
# It should execute Newton's Method and return the result.
################################################################################

def newton(num, steps):
    guess = 2
    count = 0
    while count < steps:
        guess = (guess + num/guess)/2
        count += 1

    return guess


################################################################################
# Write a helper function to compute all the results for a given value.
# It should take as input parameter a number on which to compute the square root.
# It should print to the screen a full set of results for 1, 2, 4, 8, and 16
# iterations. It should also print out the "correct" answer using math.sqrt()
# It should print a nice line and some blank space to offset subsequent runs.
################################################################################

def work(value):
    print("Steps = Value")

    i = 1
    while i <= 16:
        print(i, "=", newton(value, i))
        i *= 2
    print("sqrt =", math.sqrt(value))
    print("="*40)


################################################################################
# Main Body of the program
################################################################################
# Construct a loop that gets a value from the user and calls the helper function
# to determine the results until the user enters a zero value.
# It should then exit with a "Thank you, Good Bye!" message.
################################################################################

value = 1
while value != 0:
    value = get_number()
    work(value)

print("Thank you, Good Bye!")
