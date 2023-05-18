#Import the math module
import math

#Defining the function to calculate the circle area
def calculate_circle_area(radius):
    #Calculate the area using the formula
    area = math.pi * (radius ** 2)
    #Return the area
    return area

#Ask the user to input the radius
radius = float(input("Enter the radius of the circle: "))
#Assign the output of the function to a variable called area
area = calculate_circle_area(radius)
#Print the result
print("The area of the circle is:", area)