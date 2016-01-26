'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 7.1
'''

file = open("mbox-short.txt")

for line in file:
    print(line.upper())
