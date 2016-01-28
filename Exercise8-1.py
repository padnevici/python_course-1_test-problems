'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.1
'''
import random


def chop(list):
    del list[0]
    del list[len(list) - 1]


def middle(list):
    return list[1:len(list) - 1]


list = list(range(random.randrange(10, 20)))

print(list)
chop(list)
print(list)

newList = middle(list)
print(list)
print(newList)