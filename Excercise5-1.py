'''
Created on Jan 23, 2016

@author: Andrei Padnevici
@note: This is an exercise: 5.1
'''

total = 0
count = 0
average = 0
enteredNumber = 0

while True:
    try:
        userInput = input("Enter a number: ")
        if userInput.lower() == 'done':
            break
        
        enteredNumber = float(userInput)
        total = total + enteredNumber
        count = count + 1
        average = total / count
    except:
        print("Only number are accepted or 'done' for finish.")

print("Total: ", total)
print("Count: ", count)
print("Average: ", average)
