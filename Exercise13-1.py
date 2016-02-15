'''
Created on Feb 15, 2016

@author: Andrei Padnevici
@note: This is an exercise: 13.1
'''
import urllib.request
import urllib.parse
import json
import re

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

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

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)

    location = js['results'][0]['formatted_address']
    print(location)

    # get country code from response or print no country code
    try:
        address_components = list(js["results"][0]["address_components"])
        for address_component in address_components:
            countryCode = dict(address_component).get("short_name", None)
            types = list(dict(address_component).get("types", None))

            if countryCode is None or "country" not in [str(c).lower() for (c) in types]:
                countryCode = None
                continue

            if re.match("[A-Z]{2}", countryCode.strip()):
                break
            else:
                countryCode = None

        if countryCode is not None:
            print("Country code:", countryCode)
        else:
            print("Country code were not found")
    except:
        continue
