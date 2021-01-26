# Author: Lukas Schumi, se201028
"""
Uebungsblatt 3

Aufgabe 2
"""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for letter in sentence:
    if letter not in  count_letters.keys():
        count_letters[letter] = 1
    else:
        count_letters[letter] += 1


print(count_letters)