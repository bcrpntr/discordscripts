# This script imports the math module to use the value of pi.
import math

# This function calculates the area of the circle given its radius as input.
def calculate_circle_area(radius):
    # The area of a circle is pi times the radius squared.
    area = math.pi * (radius ** 2)
    return area

# The user is prompted to input the radius of the circle which is converted to a float.
radius = float(input("Enter the radius of the circle: "))

# The calculate_circle_area function is called with the user input as its argument, which returns the area of the circle.
area = calculate_circle_area(radius)

# The area of the circle is printed to the console, with a message that includes the actual area.
print("The area of the circle is:", area)