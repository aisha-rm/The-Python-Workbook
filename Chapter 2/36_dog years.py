"""
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""

age = int(input("Enter your age: "))

if age < 2:
    years = 10.5 * age
    print("Your age in dog years is {}".format(years))
elif age < 0:
    print("Invalid. Please enter age above 0")
else:
    x = 2 * 10.5
    y = (age - 2) * 4
    years = x + y
    print("Your age in dog years is {}".format(years))

