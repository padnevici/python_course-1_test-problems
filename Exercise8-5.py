'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.5
'''
import random

fileName = input("Enter file name: ")
try:
    file = open(fileName)
except:
    print("This '%s' file does not exist, or it locates " % fileName)
    exit()

count = 0
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        print(words[1])
        count = count + 1
    except:
        print("Cannot parse this '%s' line and get the day name" % line.strip())

print("There were %d lines in the file with From as the first word" % count)