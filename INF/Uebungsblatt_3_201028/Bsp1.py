# Author: Lukas Schumi, se201028
"""
Uebungsblatt 3

Aufgabe 1
"""

import random


lower = 1
upper = 101
count = 0

x = random.randint(0,101)

print("Welcome to the guessing game!\nThink of a number between 1 and 100!\nIf your number is lower than my guess, please type 'l', if it's higher type 'h'.\nIf I got your number, please confirm with 'y'.")

while True:

    print("Is your number: {}".format(x))
    z = input()
    if z == "y" or z == "Y" or z == "yes":
        if count == 0:
            print("Wow, at the first try")
        else:
            print("number found in {} moves".format(count))
        break
    elif z == "h":
        lower = x
        count += 1
        x = (lower + upper)//2
    elif z == "l":
        upper = x
        count += 1
        x = (lower + upper)//2
    else:
        print('please "h" fpr higher, "l" for lower or "y" for yes')