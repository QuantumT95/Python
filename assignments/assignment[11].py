"""
Charlie Tran
Assignment #11
COSC 1306
"""

new_list = []

with open("zingarelli2005.txt") as folder:
    for ciao in folder.readlines():
        new_list.append(ciao.strip())

count = 0
number_of_A = 0
for a in new_list:
    count += len(a)
    number_of_A += a.count("A")

# print(count)
# print(number_of_A)

answer = {}
word = "MICROCENTER"
total = 0

for letter in word:
    if letter not in answer:
        answer[letter] = 0
    answer[letter] += 1
    total += 1

print("The letter frequencies are:")
# print(answer)

for key, value in sorted(answer.items()):
    print("{} - {:<5.3f}".format(key, (value/total) * 100), "%")
