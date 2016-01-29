'''
Created on Jan 20, 2016

@author: Andrei Padnevici
'''

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((word, len(word)))

print(t)
t.sort(reverse=False)
print(t)

res = list()
for length, word in t:
    res.append(length)
print(res)
