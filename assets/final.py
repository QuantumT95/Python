QUESTION 1
Consider all the positive integers below 10 that are multiples of 3 or 5: 3, 5, 6, and 9. The sum of these numbers is 23.
What is the sum of all the positive integers below 1000 that are multiples of 3 or 5? 
"""
"""
total = 0
for pick_a_number in range (1,1000):
    if pick_a_number % 3 == 0 or pick_a_number % 5 == 0:
        total = pick_a_number + total
print(total)
"""
#233168
"""
                                            QUESTION 2
The first five(5) prime numbers are: 2, 3, 5, 7, and 11. The sum of these numbers is 28.
What is the sum of the first 500 prime numbers?
"""
"""
total=0
def number_list(number):
    for divisable_by in range (2,number):
        if number % divisable_by == 0:
            return False
    return True
is_number_prime(18)
basket = 3
number_list = [2]
while basket < 3580:
    if is_number_prime(basket):
          number_list.append(basket)
    basket += 2
print(number_list)
total_sum = number_list + total
print(total_sum)
"""
#824693
"""
                                            QUESTION 3
The 1st prime number is 2, the 101st prime number is 547.
What is the 10001st prime number?
"""
"""
def prime_number(number):
    for divisable_by in range (2,number):
        if number % divisable_by == 0:
            return False
    return True
prime_number(18)
temp = 3
number_list = [2]
while len(number_list) < 10001:
    if prime_number(basket):
          number_list.append(basket)
    temp += 2
print(number_list)
"""
#104743
"""
                                            QUESTION 4
The file yawl.txt contains a large number of words. 
If you consider the letters that those words start with, 
the letter X is the fewest with only 304 words. 
What is the most common starting letter for words in this file? 
"""
"""
new_list = []
with open("yawl.txt") as file:
    for line in file.readlines():
        new_list.append(line.strip())
final_answer = {}
for word in new_list:
    letter = word[0]
    if letter not in final_answer:
        final_answer[letter]= 0
    final_answer[letter]+=1
print(final_answer)
"""
#S
"""
                                            QUESTION 5
In word games, like Scrabble, players alternate spelling words with letter tiles.
 Each letter is assigned a point value and the total of these values is used to compute the score for a word.
For words of up to 3 letters in length, the highest possible score is 21
 (for the words ZIZ and ZUZ).
Consider the words in the file yawl.txt, for
 words of up to 8 letters in length, what is the highest word score possible?
Hint: The point values for the various letters are given by:
points = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
"""


points = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
new_list = []
highest_points = 0
best_word=0
with open("yawl.txt") as file:
    for line in file.readlines():
        if len(line.strip())<9:
            new_list.append(line.strip())
for words in new_list:
    total = 0
    for letter in words:
        total += points[letter]
    if total > highest_points:
        highest_points = total
        best_word = words
print (best_word, highest_points)

#PIZZAZZY 49
