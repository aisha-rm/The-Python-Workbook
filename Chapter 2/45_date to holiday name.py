"""
Canada has three national holidays which fall on the same dates each year.

Holiday                                 Date
New Year’s Day                          January 1
Canada Day                              July 1
Christmas Day                           December 25

Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
"""

month = input("Enter the month (in words): ")
month = month.capitalize()
day = input("Enter the day of the month (in digits): ")

date  = month + " " + day
#print(date)

if date  == "January 1":
    print("The date entered corresponds to New Year's Day")
    
elif date == "July 1":
    print("The date entered corresponds to Canada Day")
    
elif date == "December 25":
    print("The date entered corresponds to Christmas Day")

else:
    print("Sorry, there is no corresponding holiday for the entered date.")