'''
Created on Jan 20, 2016

@author: Andrei Padnevici
@note: This is an exercise: 3.1, 3.2 and 4.6
'''

def computepay(hours,rate):
    if hours > 40 :
        salary = 40 * rate
        salary = salary + ((hours - 40) * rate * 1.5)
    else:
        salary = hours * rate
    return salary

try:
    hours = float(input("Enter worked hours: "))
    rate = float(input("Enter rate per hour: "))
except:
    print("Only numbers are accepted")
    quit()

print(computepay(hours, rate))
    
