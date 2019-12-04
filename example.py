import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

while b != 0:
    if a < b:
        temp = a
        a = b
        b = temp
        print("a:"int(a))
        print("b:"int(b))
    else:
        b = a
    b = a - b
    print("new b"int(b))
