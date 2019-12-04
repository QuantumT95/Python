"""
Charlie Tran
Assignment #2
COSC 1306
"""

# Rounding function


def round(x):
    return int(x+0.99999)


# takes user input for dimensions of the room + cost of bottle
lengthRoom = int(input("Enter the length of the room (m): "))
widthRoom = int(input("Enter the width of the room (m): "))
costBottle = int(input("Enter the cost per bottle ($): "))

# calculation for areas for room and materials / costs
area = lengthRoom * widthRoom
sealantNeeded = round(area / 6)
bottlesNeeded = round(sealantNeeded / 2)
totalCost = bottlesNeeded * 2

# print statements for materials needed and room
print("=======================================")
print("Room area      (m2) =", area)
print("Sealant needed (L)  =", sealantNeeded)
print("Bottles needed      =", bottlesNeeded)
print("Total Cost ($)      =", totalCost)
print("=======================================")
