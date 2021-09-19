"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""

days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

secs = seconds + (minutes * 60) + (hours * 60 * 60) + (days * 24 * 60 * 60)

print("Total seconds:", secs)

