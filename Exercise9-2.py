'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 9.2
'''

try:
    file = open(input("Enter file name: "))
except:
    print("Invalid file")
    exit()

daysDict = dict()
day = None

for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        day = words[2]
    except:
        print("Cannot parse this '%s' line and get the day name" % line.strip())

    if day is not None: daysDict[day] = daysDict.get(day, 0) + 1

print(daysDict)
