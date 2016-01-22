'''
Created on Jan 20, 2016

@author: padne_000
'''

hours = 0
rate = 0

try:
    hours = float(input("Enter worked hours: "))
    rate = float(input("Enter rate per hour: "))
except:
    print("Only numbers are accepted")

if hours > 0 and rate > 0:    
    if hours > 40 :
        salary = 40 * rate
        salary = salary + ((hours - 40) * rate * 1.5)
    else:
        salary = hours * rate
    
    print("Your salary is = %s" % salary)
    
