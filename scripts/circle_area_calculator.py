# Import the math module
import math

# Define the function to calculate the area of a circle with a given radius
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2) # Calculate the area using the radius
    return area 

# Ask the user to input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Call the function and store the area in a variable
area = calculate_circle_area(radius)

# Print out the result
print("The area of the circle is:", area)