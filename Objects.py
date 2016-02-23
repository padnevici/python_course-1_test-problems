'''
Created on Feb 22, 2016

@author: Andrei Padnevici
@note: This is an example of object oriented program in python
'''
from tkinter import Pack


class PartyAnimal:
    x = 0

    def __init__(self, x=-1):
        self.x = x

    def party(self):
        self.x += 1
        print("So far", self.x)


class ChildParty(PartyAnimal):
    y = 0

    def __init__(self, x=0, y=0):
        super(ChildParty, self).__init__(x)
        self.y = y

    def sum(self):
        print(self.x + self.y)


p = PartyAnimal()
p.party()
p.party()
p.party()

p = PartyAnimal(5)
p.party()
p.party()
p.party()

c = ChildParty(9, 9)
c.party()
c.sum()
