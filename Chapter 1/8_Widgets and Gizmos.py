"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""

widgets = int(input("Please enter the number od widgets: "))
gizmos = int(input("Please neter the number of gizmos: "))
total = (widgets * 75) + (gizmos * 112)
print("The total weight is", total, "grams.")
