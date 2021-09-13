"""
Create a program that reads two integers, a and b, from the user.Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a raised to the power of b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""

from math import log10
a = int(input("Enter a number, a: "))
b = int(input("Enter another number, b: "))
sumNum = a + b
diffNum = a - b
prodNum = a * b 
quotient = a / a
remainder = a % b
result = log10(a)
result2 = a**b
print(f"""
• The sum of a and b is {sumNum}
• The difference when b is subtracted from a is {diffNum}
• The product of a and b is {prodNum}
• The quotient when a is divided by b is {quotient}
• The remainder when a is divided by b is {remainder}
• The result of log10 a is {result}
• The result of a raised to the power of b is {result2}
""") 



















