"""
Charlie Tran
Assignment #1
COSC 1306
"""

import math

PI = math.pi

radius = input("Enter radius for a circle")
radius = float(radius)

circleArea = PI * (math.pow(radius, 2))
hexagonArea = ((3*math.sqrt(3))/2)*math.pow(radius, 2)
shadedArea = circleArea - hexagonArea

print("========================================")
print("Circle area  = ", circleArea)
print("Hexagon area = ", hexagonArea)
print("Shaded area  = ", shadedArea)
print("========================================")

# This is the bonus
# bonusRadius = round(1/(PI-((3*math.sqrt(3))/2)), 6)
