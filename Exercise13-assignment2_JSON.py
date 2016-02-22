'''
Created on Feb 22, 2016

@author: Andrei Padnevici
@note: This is an exercise: 13.1
'''
import urllib.request
import urllib.parse
import json
import re

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(str(data.decode("ISO-8859-1")))
    except:
        js = None

    if js is None or 'status' not in js or js['status'].lower() != 'OK'.lower():
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # get country code from response or print no country code
    try:
        print(dict(js["results"][0]).get("place_id", None))
        # address_components = list(js["results"][0]["address_components"])
        # for address_component in address_components:
        #     countryCode = dict(address_component).get("short_name", None)
        #     types = list(dict(address_component).get("types", None))
        #
        #     if countryCode is None or "country" not in [str(c).lower() for (c) in types]:
        #         countryCode = None
        #         continue
        #
        #     if re.match("[A-Z]{2}", countryCode.strip()):
        #         break
        #     else:
        #         countryCode = None
        #
        # if countryCode is not None:
        #     print("Country code:", countryCode)
        # else:
        #     print("Country code were not found")
    except:
        continue
