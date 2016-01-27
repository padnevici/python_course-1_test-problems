'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 7.2 and 7.3
'''
from builtins import sum
import random


def printJoke():
    rand = random.randrange(1, 9)
    if rand == 1:
        print("If you do your best, whatever happens will be for the best.")
    elif rand == 2:
        print("Things that go away by themselves can come back by themselves.")
    elif rand == 3:
        print("Plaid shirts and striped pants rarely make a positive fashion statement.")
    elif rand == 4:
        print("You should never dive into murky waters.")
    elif rand == 5:
        print("It's never too late to learn to play the piano.")
    elif rand == 6:
        print("You can hurt yourself if you run with scissors.")
    elif rand == 7:
        print("You should never look directly at the sun.")
    elif rand == 8:
        print("This is the last tip.")


spam = []
total = 0
count = 0

fileName = input("Enter file name: ")
try:
    file = open(fileName)
except:
    # print("This '%s' file does not exist, or it locates " % fileName)
    printJoke()
    exit()

searchPattern = "X-DSPAM-Confidence:"

for line in file:
    if line.strip().lower().startswith(searchPattern.lower()):
        try:
            value = float(line.strip().split(":")[1])
            spam.append(value)
            total = total + value
            count = count + 1
        except:
            print("Cannot get float number for this line: '%s'" % line)

if len(spam) > 0:
    print("Average spam confidence: %g/%d = %g" % (sum(spam), len(spam), sum(spam) / len(spam)))
    print("Average spam confidence: %g/%d = %g" % (total, count, total / count))
else:
    print("Average spam confidence: %g" % 0)
