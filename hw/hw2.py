"""
Charlie Tran
Homework #2
1301022
COSC 1306
"""

ITERATIONS = 1000


def in_set(c):
    z = 0
    for i in range(ITERATIONS):
        if abs(z) > 2:
            return False
        z = z*z + c
    return True


width = int(input("Please enter your width: "))
height = int(input("Please enter your height: "))
for row in range(height):
    for col in range(width):
        x = -1.58 + 2/(width-1) * col
        y = -1 + 2/(height-1) * row
        c = complex(x, y)
        if in_set(c):
            print("*", end='')
        else:
            print(".", end='')
    print()
