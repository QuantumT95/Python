"""
Charlie Tran
Homework #4
COSC 1306
"""


def get_sig(word):  # Get the signature for a given word
    temp = list(word)
    temp.sort()
    return tuple(temp)


# Read in all the words for processing
words = []
with open("words.txt") as file:
    for word in file.readlines():
        word = word.strip()
        if len(word) == 3:
            words.append(word)


# Begin the main body of the program here
for word in words:
    print(word, get_sig(word))

anagram_size = 1
while anagram_size != 0:
    anagram_size = input(
        "Please enter the anagram group size (1-3) or 0 to quit:")
    if anagram_size == 0:
        print("Happy Thanksgiving")
        break
