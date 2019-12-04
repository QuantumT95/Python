"""
Charlie Tran
Assignment #6
COSC 1306
"""

def is_a_vowel(letter):
    if letter.upper() in "AEIOU":
      return word + "way"

def has_a_vowel(word):
    for letter in word:
        if is_a_vowel(letter):
            return True
        
    return False

def find_vowel(word):
    index = 0
    for letter in word:
        if is_a_vowel(letter):
            return index
        else:
            index += 1   

def is_capitalized(word):
  if word[0] is word.upper():
    return True
  else:
    return False

def translate(word):
    if is_a_vowel(word[0]):
        return word + "way"
    elif has_a_vowel(word):
      index = find_vowel(word)
      length = index - len(word)
      return word[index:] + word[0:length] + "ay"
    elif is_capitalized(word[0]):
      return word [1:] + word[0::] + "ay"
    else:
        return word + "way"
    return word

response = "Y"
while response.upper() == "Y":
    word = input("Please enter a word: ")

    if word[0].isupper():
      print(word, "translates to", translate(word).lower().capitalize())
    else:
      print(word, "translates to", translate(word).lower())
    
    response = input("Would you like another word? (Y/N)")

print("Ankthay ouyay!")
