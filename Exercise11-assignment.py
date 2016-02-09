'''
Created on Feb 09, 2016

@author: Andrei Padnevici
@note: This is an exercise: 11.1
'''
import re

try:
    fName = input("Enter file name: ")
    if fName == "": fName = "regex_sum_42.txt "
    file = open(fName)
except:
    print("Invalid file")
    exit()

digits = list()
for line in file:
    buffer = re.findall("[\d]+", line)
    if len(buffer) == 0: continue
    for digit in buffer: digits.append(int(digit))

print(sum(digits))

print(sum([(int(d)) for (d) in re.findall("\d+", open(fName).read())]))
