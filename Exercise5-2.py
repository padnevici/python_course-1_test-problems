'''
Created on Jan 23, 2016

@author: Andrei Padnevici
@note: This is an exercise: 5.2
'''

enteredNumbers = set()

while True:
    try:
        userInput = input("Enter a number: ")
        if userInput.lower() == 'done':
            break
        
        enteredNumbers.add(float(userInput))
    except:
        print("Only number are accepted or 'done' for finish.")

print("Min: ", min(enteredNumbers))
print("Max: ", max(enteredNumbers))
