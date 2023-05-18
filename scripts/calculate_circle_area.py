# Import the math module
import math

# Define a function that calculates the area of a circle
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)  # Use Pi from the math module to calculate the area
    return area  # Return the calculated area

# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Call the calculate_circle_area function to calculate the area of the circle with the given radius
area = calculate_circle_area(radius)

# Print the calculated area of the circle to the console
print("The area of the circle is:", area)