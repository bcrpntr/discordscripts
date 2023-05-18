# Importing the math module
import math

# Defining a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Calculating the area using the math module's formula for pi, multiplied by the square of the radius
    area = math.pi * (radius ** 2)
    # Returning the area
    return area

# Asking the user to input the radius of the circle as a float value
radius = float(input("Enter the radius of the circle: "))

# Assigning the output of the function to a variable called 'area'
area = calculate_circle_area(radius)

# Printing the result as a string, with the calculated area displayed to the user
print("The area of the circle is:", area)