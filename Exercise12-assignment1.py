'''
Created on Feb 10, 2016

@author: Andrei Padnevici
@note: This is an test assignment 1 for topic 12
'''
import re
import urllib.parse
import urllib.request
from bs4 import *

import validators

addressStr = str(input("Enter address: "))
if addressStr is "" or addressStr is None:
    addressStr = "http://python-data.dr-chuck.net/comments_42.html"
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

# get all td tags
soup = BeautifulSoup(htmlResponse.decode("ISO-8859-1"), 'html.parser')
tdTags = soup.find_all("td")
comments = list()

# iterate through all td tags and select only digits
for tdTag in tdTags:
    if re.search("\d+",tdTag.string):
        comments.append(int(tdTag.string.strip()))

print(sum(comments))
