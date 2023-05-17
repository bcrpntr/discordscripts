# Script to calculate the area of a circle using Python's math module

import math

# Define a function to calculate the area of a circle based on its radius
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Test the function by passing in a radius of 5 and printing the result
print(calculate_circle_area(5))