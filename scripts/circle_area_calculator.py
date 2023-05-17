# This script imports the math module and defines a function that calculates the area of a circle given its radius.

import math

# Define function to calculate circle area
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Print the area of a circle with radius equal to 5
print(calculate_circle_area(5))