import requests
import os
from dotenv import load_dotenv

load_dotenv()

IMGUR_CLIENT_IDS = [os.getenv("IMGUR_CLIENT_ID_" + str(i) ) for i in range(1,3)]


"""
headers = dict()
headers['Authorization'] = 'Client-ID %s' % CLIENT_ID

API = "https://api.imgur.com/3/image/"

res = requests.get(API + "ty2vT20", headers = headers)

print(res.status_code)
print(res.headers.items())
"""
for c_ids in IMGUR_CLIENT_IDS:

    headers = dict()
    headers['Authorization'] = 'Client-ID %s' % c_ids

    API = "https://api.imgur.com/3/credits"

    res = requests.get(API, headers = headers)

    #print(res.status_code)
    print(res.json()["data"])
    #print(res.headers.items())


"""API = "https://api.imgur.com/3/image/"

res = requests.get(API + "ty2vT20", headers = headers)

print(res.status_code)
print(res.headers.items())
"""