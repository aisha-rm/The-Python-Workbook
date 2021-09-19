"""
In this exercise you will reverse the process described in Exercise 24. Develop a
program that begins by reading a number of seconds from the user. Then your program
should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH,MM,and SS represent days, hours, minutes and seconds respectively. The hours,
minutes and seconds should all be formatted so that they occupy exactly two digits.

Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.
"""

secs = int(input("Enter the number of seconds: "))
days = secs // (24 * 60 * 60)
secs1 = secs % (24 * 60 * 60)
hours = secs1 // (60 * 60)
secs2 = secs1 % (60 * 60)
minutes = secs2 // 60
secs3 = secs2 % 60

print("That amounts to {:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, secs3))


