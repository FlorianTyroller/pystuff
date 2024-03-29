#! python3

from lcu_driver import Connector
import random
import json

connector = Connector()




@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-lobby/v2/lobby')
    data = await summoner.json()
    data = data["gameConfig"]
    t1 = data["customTeam100"]
    t2 = data["customTeam200"]
    print("Team 1")
    for e in t1:
        print("name: ", e["summonerName"])
    print("Team 2")
    for e in t2:
        print("name: ", e["summonerName"])

    print('LCU API is ready to be used.')



@connector.close
async def disconnect(_):
    print('[INFO] The client has been closed')

if __name__ == "__main__":
    connector.start()