"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""

feet = float(input("Enter distance in feet: "))
inches = feet * 12
yards = feet / 3
miles = feet / 5280  

print(f"The equivalent distance of {feet} feet is {inches:.2f} inches, or {yards:.2f} yards, or {miles:.2f} miles")
