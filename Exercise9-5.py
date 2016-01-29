'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 9.5
'''

try:
    file = open(input("Enter file name: "))
except:
    print("Invalid file")
    exit()

domainsDict = dict()
domain = None

for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        domain = words[1].split('@')[1]
    except:
        print("Cannot parse this '%s' line and get the domain name" % line.strip())

    if domain is not None: domainsDict[domain] = domainsDict.get(domain, 0) + 1

print(domainsDict)
