"""
In this exercise you will create a program that reads a pressure from the user in kilopascals.
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

pressure = float(input("Enter the pressure in kilopascals: "))

psi = pressure / 6.895
mmHg = pressure * 7.501
atm = pressure / 101

print("{}kPa is equivalent to {:.3f}psi, {}mmHg, and {:.3f}atm".format(pressure, psi,  mmHg, atm))