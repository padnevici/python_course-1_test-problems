'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 6.3
'''

def countOccurence(str, char):
    return str.count(char)

str = input("Please enter a string: ")
char = input("Please enter a character: ")
print(countOccurence(str,char))