import os
import requests
from dotenv import load_dotenv
import time
import json
from datetime import datetime


# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
riot_api_key = os.getenv('API_KEY')
riot_api_key_2 = os.getenv('API_KEY2')
riot_api_key_3 = os.getenv('API_KEY3')
riot_api_key_4 = os.getenv('API_KEY4')

keys = [riot_api_key,riot_api_key_2,riot_api_key_3,riot_api_key_4]


def check_match(mid):
    global counter
    counter += 1

    headers = {"X-Riot-Token": keys[counter%4]}
 

    MATCH_CHECK_URL = f"https://europe.api.riotgames.com/lol/match/v5/matches/{mid}"
            
    response = requests.get(MATCH_CHECK_URL, headers=headers)
    if response.status_code == 429:
        print("rate limited, sleeping for 5 seconds")
        time.sleep(5)
        return check_match(mid)
    time.sleep(0.2)
    if response.status_code == 200:
        responseJ = response.json()
        gamemode = responseJ["info"]["gameMode"]
        date = responseJ["info"]["gameCreation"]
        timestamp = date / 1000
        real_date = datetime.utcfromtimestamp(timestamp)
        #print("Real Date:", real_date)
        #print(gamemode)
        part_list = []
        for participant in responseJ["info"]["participants"]:
            part_list.append(participant["championName"])

        return(real_date, timestamp, part_list, gamemode)
    elif response.status_code == 404:
        return None
    else:
        print(response.status_code)
    return None

if __name__ == "__main__":
    counter = 0
    region = "EUW1_"
    offset = 10
    step = 10000
    start_id = 6900459787
    champ_1 = "Teemo"
    champ_2 = "Tryndamere"
    while offset < step:
        curr_id = start_id + offset - step
        while True:
            data = check_match(region + str(curr_id))
            if data:
                date, timestamp, champs, mode = data
                if date.day < 14 or date.hour < 14:
                    offset += 1
                    print("new offset:", offset)
                    break

                if mode not in ["ARAM", "ONEFORALL"]:
                    print(curr_id, date, champs, mode)
                    if champ_1 in champs and champ_2 in champs:
                        with open("tools/leagueoflegends/lolapi/founds.txt", "a") as file:
                            file.write("POTENTIAL FIND:" + str(curr_id) + str(data) + "\n")
                        print("POTENTIAL FIND:", curr_id, date, champs, mode)
            
            curr_id -= step

# 87
