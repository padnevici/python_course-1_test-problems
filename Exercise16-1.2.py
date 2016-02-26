'''
Created on Feb 26, 2016

@author: Andrei Padnevici
@note: This is an exercise: 16.1-1
'''

import os
import hashlib


def getChecksum(filePath):
    try:
        file = open(filePath, "rb")
        data = file.read()
        file.close()
        return hashlib.md5(data).hexdigest()
    except:
        print("Cannot open this file:", filePath)
        return None


count = 0
mp3FilesDict = dict()

for (dirname, dirs, files) in os.walk("D:/Music"):
    for filename in files:
        if filename.endswith('.mp3'):
            filePath = os.path.join(dirname, filename)

            checksum = getChecksum(filePath)
            if checksum is None:
                continue
            else:
                isDuplicate = mp3FilesDict.get(checksum, None)
                if isDuplicate is None:
                    mp3FilesDict[checksum] = filePath
                else:
                    print("File size:", checksum)
                    print("Saved file:", isDuplicate)
                    print("Potential duplicate file:", filePath, "\n")
