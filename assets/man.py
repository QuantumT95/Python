"""
Charlie Tran
Homework #2
COSC 1306
"""

ITERATIONS = 1000

def in_set(c):
  z = 0
  for i in range(ITERATIONS):
    if abs(z) > 2:
      return False
    z = z**2 + c
  return True



width = int(input("Please enter your width: "))
height = int(input("Please enter your height: "))
for row in range(height):
    for col in range(width):
        x = col
        y = row
        c = complex(x,y)
        if in_set(c):
          print("*",end='')
        else:
          print("-",end='')
