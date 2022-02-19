import time

import requests
import json
def geocoding(address='list'):
    key = #使用者key

    addresslist = []
    for i in address:
        html = 'https://api.tomtom.com/search/2/geocode/%s.json?key=%s&storeResult=false&typeahead=true&limit=1&ofs=0&countrySet=TWN&language=zh-TW' % (
            str(i), key)
        try:
            a = requests.get(html).text
        except:
            time.sleep(2)
            a = requests.get(html).text

        ##參數詳情:https://developer.tomtom.com/search-api/search-api-documentation-geocoding/geocode

        print(a)
        b = json.loads(a)
        c = b['results'][0]['position']
        long = c['lon']
        lat = c['lat']
        position = [long, lat]
        addresslist.append(position)
        print(position)




    return addresslist







