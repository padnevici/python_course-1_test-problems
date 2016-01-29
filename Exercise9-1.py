'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 9.1
'''

file = open("romeo.txt")

wordsDict = dict()

for line in file:
    words = line.split()
    for word in words:
        wordsDict[word] = wordsDict.get(word, 0)

print("window: ","window"in wordsDict)
print("wdsfsindow: ","wdsfsindow"in wordsDict)
print(wordsDict)