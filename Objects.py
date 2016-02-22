'''
Created on Feb 22, 2016

@author: Andrei Padnevici
@note: This is an example of object oriented program in python
'''
from tkinter import Pack


class PartyAnimal:
    x = 0

    def party(self):
        self.x+=1
        print("So far", self.x)

p = PartyAnimal()
p.party()
p.party()
p.party()

PartyAnimal.party(PartyAnimal())