"""
Charlie Tran
Assignment #10
COSC 1306
"""

result = {}
limit = 2019
for perimeter in range(12, limit, 2):
    for a in range(1, perimeter//3):
        for b in range(a+1, perimeter//2):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                if perimeter not in result:
                    result[perimeter] = []
                result[perimeter].append((a, b, c))

# searches for most triangles
counter = 1
for x in result.keys():
    if len(result[x]) > counter:
        counter = len(result[x])

for x in result:
    if len(result[x]) == counter:
        print("For a limit of", limit)
        print()
        print("The perimeter of", x,
              "gives a maximum number of", counter, "triangles.")
        print()
        print("The triangles are:")
        print()
        print(*result[x], sep="\n\n")
        break
