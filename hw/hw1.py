"""
Charlie Tran
Homework #1
COSC 1306
"""

import math

# doubles the value


def double(x):
    return 2*x


# takes user input for dimensions of the room
lengthRoom = float(input("Enter the length of the room in feet: "))
widthRoom = float(input("Enter the width of the room in feet: "))
heightRoom = float(input("Enter the height of the room in feet: "))

# calculation for areas for room
areaLengthWall = lengthRoom * heightRoom
areaWidthWall = widthRoom * heightRoom
areaCeiling = lengthRoom * widthRoom
totalArea = double(areaLengthWall) + double(areaWidthWall) + areaCeiling

# calculation for materials required and rounds up
gallonsRequired = math.ceil(totalArea/400)
tilesRequired = math.ceil(areaCeiling * 16)

# print statements for materials needed
print("The total paint needed to cover the walls and ceiling is",
      gallonsRequired, "gallons.")
print("A total of", tilesRequired, "tiles are needed to cover the floor.")
