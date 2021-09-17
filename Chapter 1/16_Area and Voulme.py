"""
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr 2. The
volume of a sphere is computed using the formula volume = 4
3πr 3.
"""

import math 
rad = float(input("Enter radius: "))
area = math.pi * rad ** 2
volume = 4/3 * (math.pi * rad ** 3)

print(f"The area of a circle with radius of {rad} is {area:.2f}")
print(f"The volume of a sphere with same radius is {volume:.2f}")

