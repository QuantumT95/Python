"""
Charlie Tran
Homework #5
COSC 1306
"""

maxLength = 0
maxSeq = []
maxX = 0
seqValue = 2000000

for x in range(seqValue):
    value = x + 1
    seq = [value]
    length = 1
    while value != 1:
        if value % 2 == 0:
            value = int(value/2)
        else:
            value = int(3*value + 1)
        length += 1
        seq.append(value)
    if maxLength < length:
        maxLength = length
        maxSeq = seq
        maxX = x + 1

print("The longest sequence up to {} is {} with a length of {}.".format(
    seqValue, maxX, maxLength))
print(maxSeq)
