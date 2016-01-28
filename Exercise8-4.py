'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.4
'''
import random


file = open("romeo.txt")
selectedWords = list()

for line in file:
    words = line.strip().split()
    for word in words:
        if word not in selectedWords:
            selectedWords.append(word)

selectedWords.sort()
print(selectedWords)
