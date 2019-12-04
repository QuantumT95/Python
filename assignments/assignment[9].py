"""
Charlie Tran
COSC 1306
Assignment #9
"""

words = []
with open("words.txt") as file:
  for aWord in file.readlines():
    words.append(aWord.strip())

good_list = []
for word in words:
  if len(word) == 3 or len(word) == 4:
    good_list.append(word)


key_pad = {"1": ["L", "I"], "2":["A", "B", "C"],
"3":["D","E","F"], "4":["G", "H", "I"], "5":["J", "K", "L"],
"6":["M","N", "O"], "7":["P","Q","R","S"], "8":["T", "U", "V"],
"9":["W", "X", "Y", "Z"], "0":["O"]}

def helper(first, second):
  result = []
  for a in first:
    for b in second:
      result.append(a+b)
  
  return result



def get_words(number):
  temp = [""]
  for letter in number:
    temp = helper(temp, key_pad[letter])
  if len(number) == 3:
    for possible_word in temp:
      if possible_word in good_list:
        pos_word_1.append(possible_word)
  else:
    for possible_word in temp:
      if possible_word in good_list:
       pos_word_2.append(possible_word)

def get_abreviations(phone_number):
  digits = phone_number[:3]
  digits2 = phone_number[-4:]
  # get possible word combinations for set 1
  get_words(digits)
  # get possible word combinations for set 2
  get_words(digits2)
  # Using for loop 
  for i in range(len(pos_word_1)): 
    for j in range(len(pos_word_2)):
      print(pos_word_1[i] + "-" + pos_word_2[j])


ans = "Y"
while ans == "Y":
  phone_number = input("Please enter a phone number(###-####) :")
  print("Results include...")
  pos_word_1 = []
  pos_word_2 = []
  get_abreviations(phone_number)
  print()
  ans = input("Try another (Y/N)?")
  if ans == "N":
    print("Good-Bye!")
