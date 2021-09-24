"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it.
"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height * height)

print("Your BMI is %.2f" % BMI)
