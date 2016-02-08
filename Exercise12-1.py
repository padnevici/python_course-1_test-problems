'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 12.1
'''
import re
import socket
import urllib.parse
import validators

addressStr = str(input("Enter address: "))
if addressStr is "" or addressStr is None:
    addressStr = "http://www.py4inf.com/code/romeo.txt"
addressStr = addressStr.strip()

# prepare url for urlparse
if re.search("^http[s]*://", addressStr) is None:
    if addressStr.startswith("//") is False:
        if addressStr.startswith("/") is True:
            addressStr = "/" + addressStr
        else:
            addressStr = "//" + addressStr

if re.search("/$",addressStr) is None:
    addressStr+="/"

address = urllib.parse.urlparse(addressStr, scheme="http")
addressStr = address.geturl()

# exit program if invalid url
if validators.url(addressStr) is not True:
    print("Invalid URL - [%s], please try again." % addressStr)
    exit(-1)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# init connection to server
print("Creating connection to:", address.netloc)
mysock.connect((address.netloc, 80))

# navigating to the address
getRequestStr = str('GET %s HTTP/1.0\n\n' % addressStr)
print("Sending:", getRequestStr)
try:
    mysock.send(getRequestStr.encode(encoding="iso-8859-1"))
except:
    print("Unknown error is occurred on navigating")
    exit(-1)

# read response
responce = bytes()
while True:
    try:
        data = mysock.recv(512)
        if (len(data) < 1):    break
        responce += data
    except:
        print("Unknown error is occurred on data reading")
        exit(-1)

print(responce.decode(encoding="ISO-8859-1"))
mysock.close()
