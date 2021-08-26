import json
import requests
import pandas as pd
import numpy as np

URL = 'https://bikeshare.metro.net/stations/json/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(URL, headers=headers)

data = json.loads(page.text)
data = data["features"]

columnNames = data[0]["properties"].keys()

df = pd.DataFrame(columns=columnNames)

for i,d in enumerate(data):
   
    column = list(d["properties"].values())

    while len(column) < len(columnNames):
        column.append("null")
    
    df.loc[i] = column


print(df)




#df = pd.DataFrame(cars, columns = ['Longitude','Price'], index=['Car_1','Car_2','Car_3','Car_4'])

#print (df)
