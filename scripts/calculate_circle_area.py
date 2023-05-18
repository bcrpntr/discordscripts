#This imports the math module for using the value of pi
import math

#This is a function to calculate the area of a circle, given the radius
def calculate_circle_area(radius):
    #The area formula
    area = math.pi * (radius ** 2)
    #Returns the area value
    return area

#Asks user to enter a value for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
#Calculates the area of the circle using the calculate_circle_area function
area = calculate_circle_area(radius)
#Prints out the area of the circle
print("The area of the circle is:", area)