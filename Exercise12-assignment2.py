'''
Created on Feb 11, 2016

@author: Andrei Padnevici
@note: This is an test assignment 2 for topic 12
'''
import re
import urllib.parse
import urllib.request
from bs4 import *

import validators


def prepareUrl(addressStr):
    # prepare url for urlparse
    if re.search("^http[s]*://", addressStr) is None:
        if addressStr.startswith("//") is False:
            if addressStr.startswith("/") is True:
                addressStr = "/" + addressStr
            else:
                addressStr = "//" + addressStr

    address = urllib.parse.urlparse(addressStr, scheme="http")
    return address.geturl()


def checkUrl(addressStr):
    # exit program if invalid url
    if validators.url(addressStr) is not True:
        print("Invalid URL - [%s], please try again." % addressStr)
        exit(-1)


def navigateAndRead(addressStr):
    checkUrl(addressStr)
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
    return htmlResponse.decode("ISO-8859-1")


defaultUrlPattern = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/"

def getUrlFromAtagAtPosition(htmlDocument, position):
    soup = BeautifulSoup(htmlDocument, 'html.parser')
    aTags = soup.find_all("a")
    if position >= len(aTags) or position < 0:
        print("Provide position %d is out of range of all found links %d" % (position, len(aTags)))
        exit(-1)
    url = aTags[position].get('href', None)
    if url is None:
        print("There is no href attribute at %d position" % position)
        exit(-1)
    return prepareUrl(defaultUrlPattern + url.strip())


# enter url
addressStr = str(input("Enter address: ")).strip()
if addressStr is "" or addressStr is None:
    addressStr = defaultUrlPattern + "/known_by_Fikret.html"
addressStr = prepareUrl(addressStr)
checkUrl(addressStr)

# enter count and position
try:
    position = int(input("\nEnter position: "))
    position -= 1
    count = int(input("\nEnter count: "))
except:
    print("Not a number")
    exit(-1)

nextUrl = getUrlFromAtagAtPosition(navigateAndRead(addressStr), position)

for c in range(count):
    nextUrl = getUrlFromAtagAtPosition(navigateAndRead(nextUrl), position)
