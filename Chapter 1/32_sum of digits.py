"""
Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3+1+4+1=9.
"""

num = input("Enter a four-digit integer: ")
digits = list(num)
total = sum(int(d) for d in digits)
print(f"{num[0]}+{num[1]}+{num[2]}+{num[3]}={total}")