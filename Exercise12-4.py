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
responseDataBytes = bytes()
print("Navigating to:", addressStr)
try:
    with urllib.request.urlopen(addressStr) as responseUrl:
        while True:
            data = responseUrl.read(512)
            if (len(data) < 1): break
            responseDataBytes += data
except:
    print("Unknown error is occurred on navigating")
    exit(-1)

# getting total count of <p> tag
pTags = re.findall("<p>", responseDataBytes.decode("ISO-8859-1"))
print("There are %d of <p> tags in the requested page" % len(pTags))
