'''
Created on Jan 20, 2016

@author: Andrei Padnevici
'''

import os
import sys

if len(sys.argv) > 1:
    startFolder = sys.argv[1]
else:
    startFolder = "c:/"

print(startFolder)
count = 0
for (dirname, dirs, files) in os.walk(startFolder):
    for filename in files:
        if filename.endswith('.dll'):
            filePath = os.path.join(dirname, filename)
            fileSize = float(os.path.getsize(filePath) / 1024 / 1024).__round__(4)
            print(str(fileSize) + "M", filePath)
            break
