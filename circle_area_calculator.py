# This script imports the math module, which is used to access the value of pi for calculating the area of a circle.
# A function called 'calculate_circle_area' is defined, which takes the radius as an argument and calculates the area of the circle.
# The area is returned by the function.
# The user is prompted to input the radius of the circle.
# The function 'calculate_circle_area' is called using the user input as the argument.
# The value returned by the function is assigned to a variable called 'area'.
# The value of 'area' is printed along with the string "The area of the circle is:".

import math

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Calculate the area using the formula for a circle, and the value of pi from math module
    area = math.pi * (radius ** 2)
    # Return the calculated area
    return area

# Prompt user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area using the 'calculate_circle_area' function, passing in the user input as an argument
area = calculate_circle_area(radius)

# Print the calculated area with a string indicating its meaning.
print("The area of the circle is:", area)