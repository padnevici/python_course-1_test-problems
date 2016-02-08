'''
Created on Jan 24, 2016

@author: Andrei Padnevici
@note: This is an exercise: 12.2
'''
import re
import urllib.parse
import urllib.request

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

address = urllib.parse.urlparse(addressStr, scheme="http")
addressStr = address.geturl()

# exit program if invalid url
if validators.url(addressStr) is not True:
    print("Invalid URL - [%s], please try again." % addressStr)
    exit(-1)

# navigating to the address and read data
response = bytes()
print("Navigating to:", addressStr)
try:
    with urllib.request.urlopen(addressStr) as responseUrl:
        while True:
            data = responseUrl.read(512)
            if (len(data) < 1): break
            response += data
except:
    print("Unknown error is occurred on navigating")
    exit(-1)

# getting total count of chars
totalLen = len(response)
maxCharsToShow = 3000

if totalLen > maxCharsToShow:
    print(response.decode(encoding="ISO-8859-1")[:maxCharsToShow],
          "\n\n-->>First %d of total %d chars" % (maxCharsToShow, totalLen))
else:
    print(response.decode(encoding="ISO-8859-1"), "\n\n-->>Total chars: %d" % (totalLen))
