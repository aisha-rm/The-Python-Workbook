"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet.
"""

temp = float(input("Enter temperature in degrees Celsius: "))

F = (temp * (9/5) ) + 32
K = temp + 273.15

print(f"{temp} degrees Celsius is equivalent to {K} degrees Kelvin and {F} degrees farenheit")
