"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
"""

#4% interest/ year 
savings = float(input("Enter amount deposited in savings account: "))
interest = 0.04 
savings1 = (interest*savings) + savings
savings2 = savings1 + (interest*savings1)
savings3 = savings2 + (interest*savings2)

print("Your savings will be %.2f after 1 year, %.2f after 2 years and %.2f after 3 years" % (savings1, savings2, savings3))