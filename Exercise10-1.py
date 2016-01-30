'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 10.1
'''

try:
    fName = input("Enter file name: ")
    if fName == "": fName = "mbox-short.txt"
    file = open(fName)
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

emailsList = list(sorted([(value, key) for (key, value) in emailsDict.items()], reverse=True))
print("%s %d" % (emailsList[0][1], emailsList[0][0]))
