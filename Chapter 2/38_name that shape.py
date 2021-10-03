"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

sides = int(input("Enter the number of sides of the shape: "))

shapes = ['triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']

if 3 <= sides <= 10:
    print("The corresponding shape for the number of sides is {}".format(shapes[sides-3]))
else:
    print("Invalid number of sides. Please enter a number between 3 and 10.")