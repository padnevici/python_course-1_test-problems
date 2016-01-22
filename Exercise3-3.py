'''
Created on Jan 20, 2016

@author: padne_000
'''

score = None

try:
    score = float(input("Enter score: "))
except:
    print("Only numbers are accepted")

if score != None:
    if score > 1.0 or score < 0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print ("D")
    else:
        print("F")




    
