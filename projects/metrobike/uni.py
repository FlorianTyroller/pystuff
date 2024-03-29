import json
import requests
import pandas as pd
import numpy as np
import geopy.distance
import random
import sys
import PySimpleGUI as sg
import webbrowser




def createDataFrame():
    URL = 'https://bikeshare.metro.net/stations/json/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(URL, headers=headers)

    data = json.loads(page.text)
    data = data["features"]

    columnNames = list(data[0]["properties"].keys())

    columnNames.append("distanceToUser")

    df = pd.DataFrame(columns=columnNames)

    for i,d in enumerate(data):

        column = list(d["properties"].values())



        while len(column) < len(columnNames):
            column.append("null")

        df.loc[i] = column

    return df


def findStationsWithBikes(dataFrame, coordinates):
    df = dataFrame
    df = fillDistance(df, coordinates)

    df = df.sort_values("distanceToUser")

    df = df[df["bikesAvailable"].map(lambda x: x) > 0]

    return df

 



def findStationsWithDocks(dataFrame, coordinates):
    df = dataFrame
    df = fillDistance(df, coordinates)

    df = df.sort_values("distanceToUser")

    df = df[df["docksAvailable"].map(lambda x: x) > 0]

    return df
    


def fillDistance(dataFrame, coordinates):
    df = dataFrame
    df["distanceToUser"] = df.apply(lambda x:  geopy.distance.distance((x["latitude"],x["longitude"]),coordinates), axis=1)
    return df


def findRoute(dataFrame, coordsOrigin, coordsDestination): 
    df = dataFrame
    #coordsDestination = (34.14987, -118.37889)
    #coordsOrigin = (34.04554, -118.25667)
    stationOrigin = findStationsWithBikes(df,coordsOrigin)[["latitude", "longitude"]]
    stationDestination = findStationsWithDocks(df,coordsDestination)[["latitude", "longitude"]]
    return ((stationOrigin.iloc[0]['latitude'],stationOrigin.iloc[0]['longitude']), (stationDestination.iloc[0]['latitude'],stationDestination.iloc[0]['longitude']))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

    
#------GUI------

def runGUI(dataFrame):

    # selection side (left)

    search_column = [
        [sg.Text("Find closest stations")],
    ]
    left_search = [
        [sg.Text('Latitude', size=(15, 1)), sg.InputText(size=(15, 1),key="lat")],
        [sg.Text('Longitude', size=(15, 1)), sg.InputText(size=(15, 1),key="long")],
        [sg.Text('Results', size=(15, 1)), sg.InputText(size=(5, 1),key="results")],
        [sg.Checkbox('has Bikes', default=False,key="bikes"), sg.Checkbox('has Docks', default=False,key="docks")],
        [sg.Button('Search', size=(5, 1))],
    ]


    # route side (middle)

    route_column = [
        [sg.Text("Route")],
        
    ]
    middle_route = [
        [sg.Text("Origin")],
        [sg.Text('Latitude', size=(15, 1)), sg.InputText(size=(15, 1),key="latOrigin")],
        [sg.Text('Longitude', size=(15, 1)), sg.InputText(size=(15, 1),key="longOrigin")],
        [sg.Text("Destination")],
        [sg.Text('Latitude', size=(15, 1)), sg.InputText(size=(15, 1),key="latDestination")],
        [sg.Text('Longitude', size=(15, 1)), sg.InputText(size=(15, 1),key="longDestination")],
        [sg.Button('Find', size=(5, 1))],
    ]


    #result side (right)

    result_column = [
        [sg.Text("Result")],
        [sg.Button('Route to nearest Station', size=(10, 2),key="r1")],
        [sg.Button('Bike Route', size=(10, 1),key="r2")],
        [sg.Button('Station to Destination', size=(10, 2),key="r3")],
        [sg.Button('Overview', size=(10, 1),key="r4")],   
    ]



    

    # ----- Full layout -----
    layout = [
        [   

            sg.Column(search_column+left_search),
            sg.VSeperator(),
            sg.Column(route_column+middle_route),
            sg.Column(result_column),

        ]
    ]


    # Create the window
    window = sg.Window("Bike", layout)

    # Create an event loop
    URLs = []
    while True:
        
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        

        print(event)
        if event=="Search":
            df = dataFrame
            coords = (values["lat"],values["long"])
            if is_number(coords[0]) and is_number(coords[1]): 
                if values["bikes"]:
                    df = findStationsWithBikes(df,coords)
                if values["docks"]:
                    df = findStationsWithDocks(df,coords)

                results = values["results"]

                if results.isnumeric():

                    if int(results) > len(df.index):
                        results = 10

                    df = df[0:int(results)]

                
                URL = buildPlacesURL(df,coords)
           
                webbrowser.open(URL, new=0, autoraise=True)

        if event=="Find":
            df = dataFrame
            coordsOrigin = (values["latOrigin"],values["longOrigin"])
            coordsDestination = (values["latDestination"],values["longDestination"])

            if is_number(coordsOrigin[0]) and is_number(coordsOrigin[1]) and is_number(coordsDestination[0]) and is_number(coordsDestination[1]): 
                route = findRoute(df,coordsOrigin,coordsDestination)
                
                URLs = buildRouteURLs(route,coordsOrigin,coordsDestination)

                print(URLs)
                
        if len(URLs) > 0:
            if event=="r1":
                webbrowser.open(URLs[0], new=0, autoraise=True)

            if event=="r2":
                webbrowser.open(URLs[1], new=0, autoraise=True)
            
            if event=="r3":
                webbrowser.open(URLs[2], new=0, autoraise=True)

            if event=="r4":
                webbrowser.open(URLs[3], new=0, autoraise=True)
        else:
            df = dataFrame
            coordsOrigin = (values["latOrigin"],values["longOrigin"])
            coordsDestination = (values["latDestination"],values["longDestination"])

            if is_number(coordsOrigin[0]) and is_number(coordsOrigin[1]) and is_number(coordsDestination[0]) and is_number(coordsDestination[1]): 
                route = findRoute(df,coordsOrigin,coordsDestination)
                
                URLs = buildRouteURLs(route,coordsOrigin,coordsDestination)


    window.close()



def buildPlacesURL(dataFrame, coords):
    base = "https://www.google.com/maps/dir/"

    
    for index, row in dataFrame.iterrows():

        base += str(row["latitude"]) + "," + str(row["longitude"]) + "/"

    base += "/@" + str(coords[0]) + "," + str(coords[1]) + "z"

    

    
    return base

def buildRouteURLs(route, origin, dest):
    URLs = []
    base = "https://www.google.com/maps/dir/?api=1"
    URLs.append(base + "&origin=" + str(origin[0]) + "," + str(origin[1]) + "&destination=" + str(route[0][0]) + "," + str(route[0][1]) +  "&travelmode=walking")
    URLs.append(base + "&origin=" + str(route[0][0]) + "," + str(route[0][1]) + "&destination=" + str(route[1][0]) + "," + str(route[1][1]) + "&travelmode=bicycling")
    URLs.append(base + "&origin=" + str(route[1][0]) + "," + str(route[1][1]) + "&destination=" + str(dest[0]) + "," + str(dest[1]) + "&travelmode=walking") 
    URLs.append("https://www.google.com/maps/dir/" + str(origin[0]) + "," + str(origin[1]) + "/" + str(route[0][0]) + "," + str(route[0][1]) +"/" + str(route[1][0]) + "," + str(route[1][1]) + "/" + str(dest[0]) + "," + str(dest[1]))


    return URLs
    


def main():
    
    dataFrame = createDataFrame()    

    
    #print(findRoute(dataFrame,0,0))

    #print(findStationsWithDocks(50,dataFrame,(0,0)))
    #print(dataFrame[["latitude", "longitude"]])

    runGUI(dataFrame)
    







if __name__ == "__main__":
    main()






#https://www.google.com/maps/search/?api=1&query=34.14987%2C-118.37889/34.04554%2C-118.25667

#examples
#from
#34.041193200029845, -118.23615312955907

#to
#34.03121550947468, -118.33059356231782
