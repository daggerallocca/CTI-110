# Dagger Allocca
# 09/11/2024
# P2LAB1
# Calculate math related to a circle

import math

# Get float input from user (radius)
radius = float(input('What is the radius of the circle? '))

print()

# Calculate the diameter, circumference, and area based on user's radius input
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Show the users all of the calculations
print('The diameter of the circle is',round(diameter, 2))
print('The circumference of the circle is',round(circumference, 2))
print('The area of the circle is',round(area, 2))


