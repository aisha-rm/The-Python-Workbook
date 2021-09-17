"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:

q = mCΔT

Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 J
g◦C. Because water has a
density of 1.0 grams per milliliter, you can use grams and milliliters interchangeably
in this exercise.

Extend your program so that it also computes the cost of heating the water. Electricity
is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
your program to compute the cost of boiling the water needed for a cup of coffee.

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.
"""

mass = float(input("Enter the amount of water in grams or milliliters: "))
tempChange = float(input("Enter the desired temperature change: "))
heatCap = 4.186   #specific heat capacity of water
energy = mass * heatCap * tempChange

print(f"The energy required to achieve the desired temperature change is {energy: .2f} Joules")

electriCost = 8.9  #8.9 cents per kilowathh hour
# 1kWh = 3.6 million J
kiloWH = energy /(3.6 * (10**6))
cost = kiloWH * electriCost

print(f"The cost of boiling a cup of water for coffee is {cost:.2f} cents")