'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 10.3
'''
import string

try:
    fName = input("Enter file name: ")
    if fName == "": fName = "mbox-short.txt"
    file = open(fName)
except:
    print("Invalid file")
    exit()

# count chars
charsDict = dict()

for line in file:
    words = line.lower().strip().split()
    for word in words:
        chars = list(word)
        for char in chars:
            if char in string.punctuation or char in string.digits: continue
            charsDict[char] = charsDict.get(char, 0) + 1

# count average value of appearence
totalChars = sum(charsDict.values())
charsAverageDict = dict()

for (k, v) in charsDict.items():
    charsAverageDict[k] = (float(charsDict[k]) / float(totalChars), charsDict[k])

charsAverageLst = sorted([(v, k) for (k, v) in charsAverageDict.items()], reverse=True)

print("Total chars:", totalChars)
print("Char\t", "Count\t", "Average")
for index in range(len(charsAverageLst)):
    print("%s\t%d\t%g" % (
        charsAverageLst[index][1], charsAverageLst[index][0][1], round(charsAverageLst[index][0][0] * 100, 2)), "%")
