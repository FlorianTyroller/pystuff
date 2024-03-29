#! python3

from lcu_driver import Connector
import random
import asyncio
import aiohttp
import time

connector = Connector()

def get_all_combs(length):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 1
    s = [""]
    for i in range(length):
        print("LEN:", i)
        ss = []
        for a in s:
            for cx in abc:
                ss.append(a+cx)
        s = ss
    return s

def get_full_api_url(connection, endpoint):
    scheme = connection._protocols[0]  # Likely 'https'
    host = '127.0.0.1' 
    port = connection._port  # Assuming you have access to the port this way

    base_url = f"{scheme}://{host}:{port}"  # Construct the base URL
    if not base_url.endswith("/"):
        base_url += "/"
    return base_url + endpoint 

def split_list_equally(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

async def create_lobby_withoutmap(connection, mode):
    start_id = 0
    max_id = 100
    while start_id < max_id:
        data = {
            "customGameLobby": {
                "configuration": {
                    "gameMode": mode,
                    "gameMutator": "",
                    "gameServerRegion": "",
                    "mapId": start_id,
                    "mutators": {
                        "id": 1
                    },
                    "spectatorPolicy": "AllAllowed",
                    "teamSize": 8,
                },
                "lobbyName": "test",
                "lobbyPassword": ""
            },
            "isCustom": True,
        }

        # print('[INFO] Creating 5v5 Practice Tool Lobby')
        lobby = await connection.request('post', '/lol-lobby/v2/lobby', data=data)

        if lobby.status == 200:
            print('[INFO] Lobby created')
            return
        elif lobby.status != 500:
            print('[ERROR] Failed to create lobby',
                  lobby.status, start_id, mode)
        start_id += 1


async def create_lobby(connection):
    data = {
        "customGameLobby": {
            "configuration": {
                "gameMode": "TFT",
                "gameMutator": "",
                "gameServerRegion": "",
                "mapId": 11,
                "mutators": {
                    "id": 1
                },
                "spectatorPolicy": "AllAllowed",
                "teamSize": 5,
            },
            "lobbyName": "test",
            "lobbyPassword": ""
        },
        "isCustom": True,
    }

    print('[INFO] Creating 5v5 Practice Tool Lobby')
    lobby = await connection.request('post', '/lol-lobby/v2/lobby', data=data)

    if lobby.status == 200:
        print('[INFO] Lobby created')
    else:
        print('[ERROR] Failed to create lobby', lobby.status)


async def create_lobby2(connection):
    # modes = ["CLASSIC", "ARAM", "URF", "PRACTICETOOL", "TFT", "NEXUSBLITZ", "ONEFORALL"]
    modes2 = [
        "DOMINIONREWORK",
        "ASCENSIONREDUX",
        "PROJECTOVERCHARGE",
        "NEXUSSIEGE",
        "TWILIGHTISLES",
        "LEGACYCLASSIC",
        "MIRRORMATCH",
        "CHAOSDRAFT",
        "HITBOXTEST",
        "SPELLFXLAB",
        "JUNGLETUNING",
        "SERVERSTRESSTEST",
        "ANTICHEATSANDBOX",
        "ESPORTSSIM",
        "OBJTEST",  # Short for objective test
        "DMGTEST",  # Focused on damage scaling & testing
        "TESTREALM",
        "TEST",
        "DEV",
        "RIOT",
        "LOL",
        "RITO",
        "SKIN",
        "SKINS"
    ]
    max_id = 100
    cid = 0
    while cid < max_id:
        for mode in modes2:
            data = {
                "customGameLobby": {
                    "configuration": {
                        "gameMode": mode,
                        "gameMutator": "",
                        "gameServerRegion": "",
                        "mapId": cid,
                        "mutators": {
                            "id": 1
                        },
                        "spectatorPolicy": "AllAllowed",
                        "teamSize": 5,
                    },
                    "lobbyName": "test",
                    "lobbyPassword": ""
                },
                "isCustom": True,
            }

            lobby = await connection.request('post', '/lol-lobby/v2/lobby', data=data)

            if lobby.status == 200:
                print('[INFO] Lobby created mode:', mode, "ID:", cid)
            else:
                print('[ERROR] Failed to create lobby',
                      lobby.status, mode, "ID:", cid)
        cid += 1


async def create_lobby_mt(connection, mode, semaphore):
    async with semaphore:
        data = {
            "customGameLobby": {
                "configuration": {
                    "gameMode": mode,
                    "gameMutator": "",
                    "gameServerRegion": "",
                    "mapId": 11,
                    "mutators": {
                        "id": 1
                    },
                    "spectatorPolicy": "AllAllowed",
                    "teamSize": 5,
                },
                "lobbyName": "test",
                "lobbyPassword": ""
            },
            "isCustom": True,
        }
        lobby = await connection.request('post', '/lol-lobby/v2/lobby', data=data)

        if lobby.status == 200:
            print('[INFO] Lobby created mode:', mode, "ID:", 11)
        elif lobby.status != 500:
            print('[!!!!!] FOUND MODE', lobby.status, mode, "ID:", 11)
        else:
            print('[ERROR] Failed to create lobby', lobby.status, mode)

async def create_lobby_bruteforce_mode_concurrent(connection):
    b_combs = get_all_combs(3)
    s_combs = split_list_equally(b_combs, len(b_combs) // 10)

    semaphore = asyncio.Semaphore(5)  # Limit concurrent requests to 5

    tasks = []
    for sublist in s_combs:
        sublist_tasks = [create_lobby_mt(connection, mode, semaphore) for mode in sublist]
        tasks.append(asyncio.gather(*sublist_tasks))

    await asyncio.gather(*tasks)

async def process_sublist(connection, sublist):
    for mode in sublist:
        await create_lobby_mt(connection, mode, semaphore)


async def create_lobby_bruteforce_mode(connection):
    max_id = 100
    cid = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    c = 1

    s = [""]

    for i in range(5):
        print("LEN:", i)
        ss = []
        for a in s:
            for cx in abc:
                ss.append(a+cx)
        s = ss
        random.shuffle(s)
        if i > 1:
            for mode in s:
                cid += 1
                data = {
                    "customGameLobby": {
                        "configuration": {
                            "gameMode": mode,
                            "gameMutator": "",
                            "gameServerRegion": "",
                            "mapId": 11,
                            "mutators": {
                                "id": 1
                            },
                            "spectatorPolicy": "AllAllowed",
                            "teamSize": 5,
                        },
                        "lobbyName": "test",
                        "lobbyPassword": ""
                    },
                    "isCustom": True,
                }
                
                lobby = await connection.request('post', '/lol-lobby/v2/lobby', data=data)

                if lobby.status == 200:
                    print('[INFO] Lobby created mode:', mode, "ID:", cid)
                elif lobby.status != 500 or cid % 100 == 0:
                    if lobby.status != 500:
                        print('[!!!!!] FOUND MODE', lobby.status, mode, "ID:", 11) 
                    else:
                        print('[ERROR] Failed to create lobby', lobby.status, mode) 






async def delete_lobby(connection):
    lobby = await connection.request('delete', '/lol-lobby/v2/lobby')

    if lobby.status == 204:
        print('[INFO] Lobby deleted')
    else:
        print('[ERROR] Failed to delete lobby')

async def add_scuffed_bots(connection, ids):
    maxb = 100000000
    added = [2, 4, 5, 6, 17, 23, 29, 37, 38, 39, 40, 55, 56, 57, 61, 67, 68, 74, 78, 82, 83, 84, 85, 90, 103, 105, 106, 110, 111, 112, 113, 117, 120, 121, 127, 131, 145, 147, 201, 254, 266, 497, 711, 875, 876, 901, 902]
    added_c = 0
    c = 900
    while added_c < 5:
        while (c in ids) or (c in added):
            c += 1
        data = {
            "botDifficulty": "UBER",
            "championId": c,
            "teamId": "200"
        }
        res = await connection.request('post', '/lol-lobby/v1/lobby/custom/bots', data=data)
        if res.status == 204:
            print('[INFO] Bot added')
            added.append(c)
            print('Added ids:', added)
            added_c += 1
        else:
            print("FAILED TO ADD:", c)
        if c > maxb:
            print("END")
            return
        c+= 1

async def add_scuffed_bots2(connection, ids):
    c = 0
    
    difficulty_levels = [
    "GODLIKE", "IMPOSSIBLE", "NIGHTMARE", "INSANE", "BRUTAL", "UNFAIR",
    "CRUSHING", "OPPRESSIVE", "PUNISHING", "OVERPOWERED", "DOMINANT",
    "UNSTOPPABLE", "MERCILESS", "HARDCORE", "TOUGH", "EXTREME", "VICIOUS",
    "CHALLENGING", "RELENTLESS", "DIFFICULT", "FORMIDABLE", "SKILLFUL",
    "ADVANCED", "DEMANDING", "COMPETENT", "AGGRESSIVE", "TRICKY", "CLEVER",
    "UNPREDICTABLE", "DECEPTIVE", "EXPERT", "ADAPTIVE", "PRESSURING",
    "INTIMIDATING", "THREATENING", "FRIGHTENING", "LETHAL", "DEADLY",
    "DOOM", "DESTRUCTIVE", "UNBEATEN", "UNDEFEATED", "SIMPLE",
    "BEGINNER", "NOVICE", "CASUAL", "BASIC", "RELAXED", "MELLOW", "FORGIVING",
    "PASSIVE", "AFK", "IDLE", "HARMLESS", "WEAK", "PATHETIC", "USELESS",
    "BROKEN", "BUGGY", "GLITCHED", "LAGGY", "JANKY", "LAGGY", "RANDOM",
    "CHAOTIC", "WILD", "UNSTABLE", "FRANTIC", "BERSERK", "CRAZY", "MANIACAL",
    "INFURIATING", "ANNOYING", "BIZARRE", "WEIRD", "ODD", "UNORTHODOX" 
    ]
    while c < 5:
        diff = random.choice(difficulty_levels)
        bid = random.choice(ids)
        data = {
            "botDifficulty": diff,
            "championId": bid,
            "teamId": "200"
        }
        res = await connection.request('post', '/lol-lobby/v1/lobby/custom/bots', data=data)
        if res.status == 204:
            print('[INFO] Bot added')
            print('Added diff:', diff, 'bot id:', bid)
            c+=1
        else:
            # print("FAILED TO ADD:", bid, "WITH DIFF:", diff)
            pass

async def add_scuffed_bots3(connection, ids):
    # UBER EASY HARD
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    c = 1

    s = [""]

    for i in range(5):
        print("LEN:", i)
        ss = []
        for a in s:
            for cx in abc:
                ss.append(a+cx)
        s = ss
        if i < 3:
            continue
        for dif in s:
            bid = random.choice(ids)
            data = {
                "botDifficulty": dif,
                "championId": bid,
                "teamId": "200"
            }
            res = await connection.request('post', '/lol-lobby/v1/lobby/custom/bots', data=data)
            if res.status == 204:
                print('[INFO] Bot added')
                print('Added diff:', dif, 'bot id:', bid)
                c+=1

async def do_add_bots(connection, data):
    res = await connection.request('post', '/lol-lobby/v1/lobby/custom/bots', data=data)
    if res.status == 204:
        print('[INFO] Bot added')
    else:
        print('[ERROR] Failed to add bot')

async def add_bots(connection, ids):
    for i,id in enumerate(ids):
        data = {
            "botDifficulty": "HARD",
            "championId": id,
            "teamId": "200"
        }

        print('[INFO] Adding bot to enemy\'s team')
        await do_add_bots(connection, data)

async def test1(connection):
    print('[INFO] LCU API connected')
    """
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    

    if summoner.status != 200:
        print('[ERROR] Couldn\'t fetch summoner\'s profile')
    else:
        champions = []

        while not champions:
            print('[INFO] Fetching champions list')
            champions = await (await connection.request('get', '/lol-lobby/v2/lobby/custom/available-bots')).json()

            if not champions:
                print('[INFO] Creating dummy lobby')
                await create_lobby(connection)
                await delete_lobby(connection)
        
        await create_lobby(connection)
    """
    """
    print([champion['id'] for champion in champions])
    ids = random.sample([champion['id'] for champion in champions], 5)
    
    
    await add_bots(connection, ids)
    """
    await create_lobby2(connection)
    ids = [1, 3, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 26, 30, 31, 32, 33, 36, 44, 45, 48, 51, 53, 54, 58, 62, 63, 69, 75, 76, 81, 86, 89, 96, 98, 99, 102, 104, 115, 122, 143, 236]

    secret_ids = [2, 4, 5, 6, 17, 23, 29, 37, 38, 39, 40, 55, 56, 57, 61, 67, 68, 74, 78, 82, 83, 84, 85, 90, 103, 105, 106, 110, 111, 112, 113, 117, 120, 121, 127, 131, 145, 147, 201, 254, 266, 497, 711, 875, 876]
    ids = random.sample(secret_ids, 5)
    # await add_bots(connection, ids)
    # await add_scuffed_bots(connection, ids)
    # await add_scuffed_bots3(connection, ids)
    # await add_bots(connection, ids)

async def test2(connection):
    print('[INFO] LCU API connected')

    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    

    if summoner.status != 200:
        print('[ERROR] Couldn\'t fetch summoner\'s profile')
    else:
        champions = []

        """while not champions:
            print('[INFO] Fetching champions list')
            champions = await (await connection.request('get', '/lol-lobby/v2/lobby/custom/available-bots')).json()
            print(champions)"""
        # await create_lobby_withoutmap(connection, "zzz")
        #await create_lobby_bruteforce_mode_concurrent(connection)



@connector.ready
async def connect(connection):
    await create_lobby_bruteforce_mode_concurrent(connection)
    # print(connection._port)
    # print(get_all_combs(1))
    # await test1(connection)
    # await test2(connection)
    # await create_lobby_bruteforce_mode(connection)
    

@connector.close
async def disconnect(_):
    print('[INFO] The client has been closed')

if __name__ == "__main__":
    connector.start()