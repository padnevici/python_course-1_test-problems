'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 11.1
'''
import re

pattern = input("Enter a regular expression: ")
fName = "mbox.txt"
file = open(fName)

count = 0

for line in file:
    if re.search(pattern, line): count += 1

print("%s had %d lines that matched %s" % (fName, count, pattern))
