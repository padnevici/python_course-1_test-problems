'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 9.3 and 9.4
'''

try:
    file = open(input("Enter file name: "))
except:
    print("Invalid file")
    exit()

emailsDict = dict()
email = None

for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        email = words[1]
    except:
        print("Cannot parse this '%s' line and get the email address" % line.strip())

    if email is not None: emailsDict[email] = emailsDict.get(email, 0) + 1

print(emailsDict)

maxValue = None
maxValueKey = None

for key, value in emailsDict.items():
    if maxValue is None or value > maxValue:
        maxValueKey = key
        maxValue = value

print("%s %d" % (maxValueKey, emailsDict[maxValueKey]))
