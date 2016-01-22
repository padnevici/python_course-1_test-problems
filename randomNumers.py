'''
Created on Jan 21, 2016

@author: Andrei Padnevici
'''
import random

def printRandoms(minNumber, maxNumber):
    for x in range(0, 100):
        rand = random.random()
        print("Min: ", minNumber)
        print("Max: ", maxNumber)
        print("Rand: ", rand,)
        print("Rand calculated: ", (maxNumber - minNumber) * rand)
        print("Rand int calculated: ", int((maxNumber - minNumber) * rand) + 1)
        print(minNumber + int((maxNumber - minNumber) * rand) + 1)
        print("\n")

minNumber = int(input("Enter min:\n"))
maxNumber = int(input("Enter max:\n"))

printRandoms(minNumber, maxNumber)
