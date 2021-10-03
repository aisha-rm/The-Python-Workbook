""""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.
"""

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("This is an equilateral triangle")
    
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an isosceles triangle.")
    
else:
    print("This is not a scalene triangle.")