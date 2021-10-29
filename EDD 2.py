"""
This promgram computes the Expected Date of Delivery from the Last Menstrual Period.
"""

from datetime import timedelta, date

lmp_day = int(input("Enter day: "))
lmp_month = int(input("Enter month: "))
lmp_year = int(input("Enter year: "))

date1 = date(lmp_year, lmp_month, lmp_day)
delta = timedelta(days = 7, weeks = -13)
date2 = date1 + delta
print(date2)
delta2 = timedelta(weeks = 52)
date3 = date2 + delta2
print(date3)
# naeg = lmp_day + 7
# naeg2 = lmp_month - 3
# naeg3 = lmp_year + 1

# if lmp_month <=3:
#     if lmp_month == 2:
#         if lmp_day < 1 and lmp_month > 29:
#             print("Oops! February has 28/29 days!")
#         else:
#             naeg = lmp_day + 7
#             naeg2 = lmp_month 