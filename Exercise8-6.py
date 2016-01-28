'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.6
'''
import random

enteredNumbers = list()

while True:
    userInput = input("Enter a number: ")
    if userInput.lower() == 'done':
        break
    try:
        enteredNumbers.append(float(userInput))
    except:
        print("Only number are accepted or 'done' for finish.")
        continue

print("Maximum: ", max(enteredNumbers))
print("Minimum: ", min(enteredNumbers))
