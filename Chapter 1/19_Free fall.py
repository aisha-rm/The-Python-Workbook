"""
Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf =
v2i+ 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""

import math
d = float(input("Enter the height in meters from which the ball is dropped: "))
a = 9.8  # acceleration due to gravity is 9.8 m/s^2
speedI = 0
speedF = math.sqrt((speedI **2) + (2*a*d))
print(f"The object is traveling at {speedF:.1f} m/s^2 when it hits the ground.")