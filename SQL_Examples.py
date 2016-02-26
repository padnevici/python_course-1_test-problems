'''
Created on Feb 23, 2016

@author: Andrei Padnevici
@note: This is an example of sqlite 3 lib usage
'''

import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

print ('%d - - %d ->%s' %(1,2,3))

cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.commit()

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', ('My Way', 15))
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
