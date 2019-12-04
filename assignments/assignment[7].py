# -*- coding: utf-8 -*-
"""
Charlie Tran
COSC 1306
Assignment #7
"""

import string

# This is the plain-text to be encrypted. Do Not delete this!
plain_text = input("Write your message: ")

code_word = input("Write your code word: ")

# 5. Write the helper functions needed to do the encryption (encrypt a letter)


def encrypt_letter(text_letter, code_letter):
    letters = list(string.ascii_letters)  # Get the all the letters
    temp = text_letter.upper()
    letter_index = letters.index(temp)
    code_index = letters.index(code_letter)
    letters = letters[code_index:] + letters[:code_index]
    result = letters[letter_index]
    if text_letter.islower():
        result = result.lower()
    return result


index = 0

for i in plain_text:
    if i.upper() not in list(string.ascii_uppercase):
        print(i, end='')
    else:
        print(encrypt_letter(i, code_word[index]), end='')
        index += 1
        if index >= len(code_word):
            index = 0
