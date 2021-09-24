"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

num = input("Enter 3 numbers: ")
nums= list(num)
numbs = [int(x) for x in nums]

mn = min(numbs)
mx = max(numbs)
mid = sum(numbs) - mn - mx

print(f" From smallest to largest, the numbers are : {mn}, {mid}, {mx}.")

