import requests
import json

POST_URL = 'http://pagebot2018.herokuapp.com/addstore'
data = ''

with open('stores.json', 'r') as file:
    stores = json.load(file)
    for store in stores:
        if 'location' not in store:
            store['location'] = {'type':'Point', 'coordinates':[store['long'], store['lat']]}
        # if ('done' not in store) or store['done'] is False:
        requests.post(POST_URL, data = (store))
            # store['done'] = True
        print(store['name'])
    data = stores
    file.close()

with open('stores.json', 'w') as file:
    json.dump(data, file)
    file.close()