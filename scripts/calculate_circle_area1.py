# This script imports the math module
import math

# This defines a function that takes the radius of a circle as input and returns the area of the circle
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# This prompts the user to enter the radius of the circle as a float
radius = float(input("Enter the radius of the circle: "))

# This calls the calculate_circle_area function using the user's input as the argument and assigns the result to the variable 'area'
area = calculate_circle_area(radius)

# This prints the area of the circle as a string, along with a message to make the output more readable
print("The area of the circle is:", area)