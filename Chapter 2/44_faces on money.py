"""
It is common for images of a country’s previous leaders, or other individuals of historical
significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in below.

George Washington   $1
Thomas Jefferson    $2
Abraham Lincoln     $5
Alexander Hamilton  $10
Andrew Jackson      $20
Ulysses S. Grant    $50
Benjamin Franklin   $100

Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.
"""

notes = ['1', '2', '5', '10', '20', '50', '100']
names = {'1' : 'George Washington', '2' : 'Thomas Jefferson', '5' : 'Abraham Lincoln', '10' : 'Alexander Hamilton', '20' : 'Andrew Jackson', '50': 'Ulysses S. Grant', '100': 'Benjamin Franklin'}

banknote = input("Enter denomination of banknote in digits: ")

if banknote in notes:
    for key, value in names.items():
        if banknote == key:
            print(f"The name of the individual that appears on the ${banknote} note is {value}.")
            break
    
else:
    print(f"This note ${banknote} does not exist. Please enter a valid denomination in digits.")
