'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.1
'''
import random


def chop(listVals):
    if len(listVals) > 2:
        del listVals[0]
        del listVals[len(listVals) - 1]


def middle(listVal):
    if len(listVal) > 2:
        return listVal[1:len(listVal) - 1]
    else:
        return listVal


for x in range(10):
    listVals = list(range(random.randrange(0, 10)))

    print(listVals)
    chop(listVals)
    print(listVals)

    newList = middle(listVals)
    print(listVals)
    print(newList)
