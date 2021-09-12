"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
"""

#hint 1 acre = 43560 square feet
widthF = float(input("Please enter the width of the field in feet: "))
lengthF = float(input("Please enter the length of the field in feet: "))
areaF = widthF * lengthF
#convert to acres
inAcres = areaF / 43560
print("The area of the field is %f acres" % inAcres)