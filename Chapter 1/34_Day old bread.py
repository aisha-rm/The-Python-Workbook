"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label. All of
the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.

"""

new = 3.49
discount = 0.6 * new
old = new - discount
num = int(input('Number of day old loaves to purchase: '))
costnew = num*new
costold = num*old 

print(f"{num} loaves of fresh bread costs ${costnew:.2f}")
print(f"The discount for buying day old loaf is {discount:.2f}")
print(f"The total price of {num} day old loaves is {costold:.2f}")
