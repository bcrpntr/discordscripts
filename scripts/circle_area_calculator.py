# This script imports the math module and defines a function to calculate the area of a circle 
# based on its radius. The function returns the result. The radius value is passed as an argument 
# to the function, and its call is printed to the console.

import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

print(calculate_circle_area(5))