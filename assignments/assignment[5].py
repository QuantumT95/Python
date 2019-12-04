"""
Charlie Tran
Assignment #5
COSC 1306
"""

# Print out the options


def list_options():
    print("Please select from the following shapes:")
    print("1– Square")
    print("2– Rectangle")
    print("3– Right Triangle (left)")
    print("4– Right Triangle (right)")
    print("5– Diamond")
    print("0- Exit")

# Get a selection from the user


def get_shape():
    shape = int(input("Please enter your selection:"))
    while shape < 0 or shape > 5:
        # This is an invalid choice!
        print("Invalid selection >>", shape, "<<")
        shape = int(input("Please enter your selection:"))

    return shape


def get_size(measure, shape):
    result = int(input("Please enter the "+measure+" of the "+shape+": "))
    while result <= 0:
        print("Invalid", measure, ">>", result,
              "<<. Please enter a positive value.")
        result = int(input("Please enter the "+measure+" of the "+shape+": "))

    return result

# Draw some shapes


def draw_square(size):
    for i in range(size):
        print("X"*size)


def draw_rectangle(length, width):
    for i in range(width):
        print("@"*length)


def draw_leftTriangle(size):
    for i in range(size + 1):
        num_spaces = size - i
        print(" "*num_spaces + "^"*i)


def draw_rightTriangle(size):
    for i in range(size + 1):
        num_spaces = size - i
        print("^"*i + " "*num_spaces)


def draw_diamond(size):
    for i in range(size):
        # The number of spaces to print out before the marks
        num_spaces = abs(i-size//2)
        num_marks = size - 2*num_spaces  # the number of marks to print
        print(" "*num_spaces + "#"*num_marks)


# Start the main body of the program
while True:  # OMG an infinite loop!
    list_options()  # Show the options to the users
    shape = get_shape()  # Get their pick

    if shape == 0:
        break
    elif shape == 1:
        # Draw a square
        size = get_size("size", "square")
        draw_square(size)
    elif shape == 2:
        # Draw a rectangle
        length = get_size("length", "rectangle")
        width = get_size("width", "rectangle")
        draw_rectangle(length, width)
    elif shape == 3:
        # Draw a right triangle (left side)
        size = get_size("size", "Left Triangle")
        draw_leftTriangle(size)
    elif shape == 4:
        # Draw a right triangle (right side)
        size = get_size("size", "Right Triangle")
        draw_rightTriangle(size)
    elif shape == 5:
        # Draw a diamond
        size = get_size("size", "diamond")
        draw_diamond(size)

    # We need more options here for the triangles and diamonds
    print()  # Print out a nice blank line after the shape to split things up a bit

print("Thank you. Good-Bye!")
