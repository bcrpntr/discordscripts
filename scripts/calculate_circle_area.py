# Import the math module
import math

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Calculate the area using the radius and pi from the math module
    area = math.pi * (radius ** 2)
    # Return the area
    return area

# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))
# Call the function to calculate the area using the user-provided radius, and store the result in a variable
area = calculate_circle_area(radius)
# Print the result
print("The area of the circle is:", area)