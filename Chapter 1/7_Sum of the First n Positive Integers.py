"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1)/2
"""

n = int(input("Enter any number: "))
sum_n = (n)*(n + 1)/2
print("The sum of all positive numbers from 1 to that number is", sum_n)