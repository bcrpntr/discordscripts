# This script calculates the area of a circle using its radius.

import math

def calculate_circle_area(radius):
    # The formula for the area of a circle is pi * r^2.
    return math.pi * radius ** 2

# The function is called with a radius of 5, and the result is printed.
print(calculate_circle_area(5))