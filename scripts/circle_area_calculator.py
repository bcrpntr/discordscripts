# This script imports the math module to calculate the area of a circle using its radius
import math

# Defines a function to calculate the area of a circle using its radius
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Calls the function with a radius of 5 and prints the result
print(calculate_circle_area(5))