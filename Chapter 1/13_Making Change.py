"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
"""

cents = int(input("Enter amount of cents: "))
cent_penny = 1    #number of cents in a penny
cent_nickel = 5    #number of cents in a nickel 
cent_dime = 10     #number of cents in a dime
cent_quarter = 25    #number of cents in a quarter
cent_loonies = 100     #number of cents in loonies i.e 1 dollar
cent_toonies = 200    #number of cents in toonies

#to get number of the denominations to give
numToonies = cents//cent_toonies
print(f"{numToonies} toonies")

cents = cents % cent_toonies
numLoonies = cents//cent_loonies
print(f"{numLoonies} loonies")

cents = cents % cent_loonies
numQuarter = cents//cent_quarter
print(f"{numQuarter} quarters")

cents = cents % cent_quarter
numDime = cents//cent_dime
print(f"{numDime} dimes")

cents = cents % cent_dime
numNickel = cents//cent_nickel
print(f"{numNickel} nickels")

cents = cents % cent_nickel
print(f"{cents} pennies")  

