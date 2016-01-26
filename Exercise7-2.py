'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 7.2
'''
from fileinput import filename
from builtins import sum

spam = set()

fileName = input("Enter file name: ")
try:
    file = open(fileName)
except:
    print("This '%s' file does not exist, or it locates " % fileName)
    exit()

searchPattern = "X-DSPAM-Confidence:"

for line in file:
    if line.strip().lower().startswith(searchPattern.lower()):
        try:
            spam.add(float(line.strip().split(":")[1]))
        except:
            print("Cannot get float number for this line: '%s'" % line)

if len(spam) > 0:
    print("Average spam confidence: %g" % (sum(spam) / len(spam)))
else:
    print("Average spam confidence: %g" % 0)        