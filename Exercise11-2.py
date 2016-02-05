'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 11.1
'''
import re

try:
    fName = input("Enter file name: ")
    if fName == "": fName = "mbox-short.txt"
    file = open(fName)
except:
    print("Invalid file")
    exit()

txt = file.read()
revisons = re.findall("New Revision: ([\d]+)", txt)

print(sum([(float(n)) for n in revisons]) / len(revisons))
