'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 10.2
'''

try:
    fName = input("Enter file name: ")
    if fName == "": fName = "mbox-short.txt"
    file = open(fName)
except:
    print("Invalid file")
    exit()

hoursDict = dict()
hour = None

for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        time = words[5]
        if ":" in time:
            hour = time.split(':')[0]
        else:
            print("Cannot parse this '%s' time str and get the hour of submission" % time.strip())
            continue
    except:
        print("Cannot parse this '%s' line and get the time of submission" % line.strip())

    if hour is not None: hoursDict[hour] = hoursDict.get(hour, 0) + 1

hoursList = list([(value, key) for (key, value) in hoursDict.items()])
for occ, hour in hoursList:
    print("%s %d" % (hour, occ))
