'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 8.2 and 8.3
'''

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or words[0] != 'From': continue
    try:
        print(words[2])
    except:
        print("Cannot parse this '%s' line and get the day name" % line.strip())
