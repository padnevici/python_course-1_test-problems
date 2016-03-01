'''
Created on Mar 01, 2016

@author: Andrei Padnevici
@note: This is an test assignment 2 SQL. Read the mbox.tx and count of emails send from a specific domain. All data is stored in DB
'''
import re
import sqlite3

conn = sqlite3.connect("database.sqlite")
conn.execute("DROP TABLE IF EXISTS Counts")
conn.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
conn.commit()

file = open("mbox.txt", "r")

for line in file:
    if re.match("^From [\S]+@[\S]+", line):
        domain = re.search("@([\S]+)", line).group(1)
        dbCount = conn.execute("SELECT count FROM Counts WHERE org='%s'" % domain).fetchone()
        if dbCount is None:
            print(">>", domain, 1)
            conn.execute("INSERT INTO Counts (org, count) VALUES (?,?)", (domain, 1))
        else:
            count = dbCount[0]
            count += 1
            print("++", domain, count)
            conn.execute("UPDATE Counts SET count=%d WHERE org='%s'" % (count, domain))

conn.commit()
