"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
import math
rad = float(input("Enter radius of the cylinder in cm: "))
height = float(input("Enter height of the cylinder in cm: "))

volume = math.pi * rad**2 * height
print(f"The volume of a cyliner with those measurements is {volume:.1f} cm^3")