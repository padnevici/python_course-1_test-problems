'''
Created on Jan 20, 2016

@author: Andrei Padnevici
@note: This is an exercise: 3.3 and 4.7
'''

def computegrade(score):
    if score > 1.0 or score < 0:
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
        
try:
    score = float(input("Enter score: "))
except:
    print("Only numbers are accepted")
    quit()

print(computegrade(score))