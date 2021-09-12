"""

"""

deposit_upto_1L = 0.10
deposit_over_1L = 0.25
small = int(input("Enter number of container(s) up to 1 L: "))
big = int(input("Enter number of container(s) above 1L: "))
total = (small * deposit_upto_1L) + (big * deposit_over_1L)
print("Your refund will be $%.2f" % total)