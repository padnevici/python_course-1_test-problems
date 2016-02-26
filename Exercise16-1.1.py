'''
Created on Feb 26, 2016

@author: Andrei Padnevici
@note: This is an exercise: 16.1-1
'''

import os

count = 0
mp3FilesDict = dict()

for (dirname, dirs, files) in os.walk("D:/Music"):
    for filename in files:
        if filename.endswith('.mp3'):
            filePath = os.path.join(dirname, filename)
            fileSize = os.path.getsize(filePath)
            isDuplicate = mp3FilesDict.get(fileSize, None)
            if isDuplicate is None:
                mp3FilesDict[fileSize] = filePath
            else:
                print("File size:", fileSize)
                print("Saved file:", isDuplicate)
                print("Potential duplicate file:", filePath, "\n")
