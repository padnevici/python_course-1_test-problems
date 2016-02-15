'''
Created on Feb 15, 2016

@author: Andrei Padnevici
@note: This is an test assignment 1 XML for topic 13
'''
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import validators

addressStr = str(input("Enter address: "))
if addressStr is "" or addressStr is None:
    addressStr = "http://python-data.dr-chuck.net/comments_42.xml"
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
htmlResponse = bytes()
print("Navigating to:", addressStr)
try:
    with urllib.request.urlopen(addressStr) as responseUrl:
        while True:
            data = responseUrl.read(512)
            if (len(data) < 1): break
            htmlResponse += data
except:
    print("Unknown error is occurred on navigating")
    exit(-1)

# get all comment tags
xmlDoc = ET.fromstring(htmlResponse.decode("ISO-8859-1"))
xmlChilds = xmlDoc.find("comments").findall("comment")

# iterate through all comment tags and get values of count tag
comments = list()
for xmlChild in xmlChilds:
    count = xmlChild.find("count").text
    if count is not None:
        comments.append(int(count))

print(sum(comments))
