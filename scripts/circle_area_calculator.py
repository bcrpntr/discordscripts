# This script contains a function to calculate the area of a circle
# The math module is imported to access the value of pi

import math

# This function takes in the radius of a circle and returns its area
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# The function is called with a radius of 5 and the result is printed out
print(calculate_circle_area(5))