# This script imports the math module and defines a function that calculates the area of a circle using the formula A = πr^2. It then prints the area of a circle with a radius of 5.

import math

def calculate_circle_area(radius):
    # calculate the area of a circle using the formula A = πr^2
    return math.pi * radius ** 2

# call the function with a radius of 5 and print the result
print(calculate_circle_area(5))