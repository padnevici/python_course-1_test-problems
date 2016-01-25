'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 6.5
'''

str = 'X-DSPAM-Confidence: 0.8475'

# using split function
try:
    floatValue = float(str.split(":")[1])
    print(floatValue)
except:
    print("Float values was not extracted !!!")


# using find function    
posOfColon = str.find(":")
try:
    floatValue = float(str[posOfColon + 1:len(str)])
    print(floatValue)
except:
    print("Float values was not extracted !!!")