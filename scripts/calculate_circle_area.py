# This script defines a function to calculate the area of a circle and uses it to find the area of a circle with a radius of 5.

import math

# Define the function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Call the function with a radius of 5 and print the result
print(calculate_circle_area(5))