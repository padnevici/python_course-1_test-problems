'''
Created on Jan 19, 2016

@author: Andrei Padnevici
'''
floor = None
try:
    floor = input("What is European floor?")
    floor = int(floor)
    print(floor + 1)
except ValueError:
    print("The '{name}' is not an number. Please try again.".format(name=floor))
    print("The '%s' is not an number. Please try again." % floor)


