"""
This program calculates the Expected Date of Delivery when a user enters their Last Menstrual Period.
"""

lmp = input("Enter the date of your last period in DD-MM-YYYY format: ")
lst = lmp.split("-")
print(lst)

day = int(lst[0])
month = int(lst[1])
year= int(lst[2])

if month == 2:
    if day <1 or day >28:
        print("Error! Invalid date. Please enter date between 1 to 28 ")
elif month in [4, 6, 9, 11]:
    if day <1 or day > 30:
        print("Error! Invalid date. Please enter date between 1 to 30 ")
else:
    if day <1 or day >31:
        print("Error! Invalid date. Please enter date between 1 to 31 ")
        
if month <= 3:
                

#print("Your EDD is {}-{}-{}".format(naeg, naeg2, naeg3))