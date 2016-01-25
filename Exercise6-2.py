'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 6.1
'''

str = 'X-DSPAM-Confidence: 0.8475'

strLength = len(str) - 1

while strLength >= 0:
    print(str[strLength])
    strLength = strLength - 1
