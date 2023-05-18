# Calculate the circumference of a circle
import math

def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Test the function
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circle_circumference(radius)
print("The circumference of the circle is:", circumference)

# Calculate the volume of a cylinder