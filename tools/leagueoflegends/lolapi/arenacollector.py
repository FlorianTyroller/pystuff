import os
import requests
from dotenv import load_dotenv
import time
import mysql.connector

MAX_RETRY_ATTEMPTS = 5

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
riot_api_key = os.getenv('API_KEY')

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")





# Check if the API key exists
if not riot_api_key:
    raise ValueError("Riot Games API key not found in the .env file")

# Function to make a request to the LoL Match API
def get_match_data(match_id, retry_attempt=0):
    base_url = "https://europe.api.riotgames.com/lol/match/v5/matches/"
    headers = {"X-Riot-Token": riot_api_key}
    time.sleep(0.5)
    try:
        response = requests.get(base_url + str(match_id), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}. Retrying in {2**(retry_attempt+2)} seconds...")
        time.sleep(2**(retry_attempt+2))
        return get_match_data(match_id, retry_attempt + 1)



# Function to print participant data
def add_participant_data(participant_data, matchid):
    MatchID = matchid
    PUUID = participant_data["puuid"]
    Placement = participant_data["placement"]
    subteamPlacement = participant_data["subteamPlacement"]
    Champion_Name = participant_data["championName"]
    Champion_ID =participant_data["championId"]
    Item0 = participant_data["item0"]
    Item1 = participant_data["item1"]
    Item2 = participant_data["item2"]
    Item3 = participant_data["item3"]
    Item4 = participant_data["item4"]
    Item5 = participant_data["item5"]
    Item6 = participant_data["item6"]
    Player_Augment_1 = participant_data["playerAugment1"]
    Player_Augment_2 = participant_data["playerAugment2"]
    Player_Augment_3 = participant_data["playerAugment3"]
    Player_Augment_4 = participant_data["playerAugment4"]

    query = "INSERT INTO matchdata (matchid, puuid, placement, subteamplacement, championname, championid, item0, item1, item2, item3, item4, item5, item6, playeraugment1, playeraugment2, playeraugment3, playeraugment4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (MatchID, PUUID, Placement, subteamPlacement, Champion_Name, Champion_ID, Item0, Item1, Item2, Item3, Item4, Item5, Item6, Player_Augment_1, Player_Augment_2, Player_Augment_3, Player_Augment_4)
    return (query, values)


def get_participants(match_data):
    return match_data["metadata"]["participants"]

def get_match_ids_by_puuid(puuid, retry_attempt=0):
    if retry_attempt > MAX_RETRY_ATTEMPTS:
        print("Max retry attempts reached. Unable to get match IDs.")
        return None

    base_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    headers = {"X-Riot-Token": riot_api_key}
    time.sleep(0.5)
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}. Retrying in {2**(retry_attempt+2)} seconds...")
        time.sleep(2**(retry_attempt+2))
        return get_match_ids_by_puuid(puuid, retry_attempt + 1)


def get_random_match_id(cursor, cnx):
    # Select a random row where checked is 0
    cursor.execute("SELECT matchid FROM matchids WHERE checked = 0 ORDER BY RAND() LIMIT 1")
    random_matchid = cursor.fetchone()

    # If a random matchid is found, update the checked column to 1
    if random_matchid:
        random_matchid = random_matchid[0]
        q = "UPDATE matchids SET checked = 1 WHERE matchid = %s"
        v = (random_matchid,)
        cursor.execute(q, v)
        cnx.commit()
        return random_matchid
    else:
        return 0
    

def insert_new_puuids(playerids_list,cursor, cnx):


    for playerid in playerids_list:
        try:
            q = "INSERT INTO puuids (puuid, checked) VALUES (%s, %s)"
            v = (playerid, 0)
            cursor.execute(q, v)
            cnx.commit()
        except:
            continue
    
    


def update_checked_puuids(cursor, cnx):
    cursor.execute("SELECT puuid FROM puuids WHERE checked = 0")
    unchecked_puuids = cursor.fetchall()

    for puuid in unchecked_puuids:
        q = "UPDATE puuids SET checked = 1 WHERE puuid = %s"
        v = (puuid[0],)
        cursor.execute(q, v)

    cnx.commit()

    return [up[0] for up in unchecked_puuids]

def insert_mids_to_db(match_ids_list):
    for match_id in match_ids_list:
        try:
            q = "INSERT INTO matchids (matchid, checked) VALUES (%s, %s)"
            v =  (match_id, 0)
            cursor.execute(q,v)
            cnx.commit()
        except:
            pass


# Example usage:
if __name__ == "__main__":
    # match_id = "EUW1_6508489259"  # Replace this with the actual match ID you want to query
    checked_ml = {"EUW1_6508489259",}
    checked_pl = set()
    match_list = {"EUW1_6508489259",}
    cnx = mysql.connector.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cnx.autocommit = True
    cursor = cnx.cursor()
    c = 0


    


    match_id = get_random_match_id(cursor, cnx)
    while match_id != 0:
        c +=1
        
        match_data = get_match_data(match_id)
    

        if match_data:
            if match_data["info"]["gameMode"] == "CHERRY" and match_data["info"]["gameType"] == "MATCHED_GAME":
                participants = match_data["info"]["participants"]
                for participant_data in participants:
                    q, v = add_participant_data(participant_data, match_id)
                    try:
                        cursor.execute(q, v)
                        cnx.commit()
                    except:
                        continue
                pl = get_participants(match_data)
                
                insert_new_puuids(pl, cursor, cnx);

                upl = update_checked_puuids(cursor, cnx)

                for p in upl:

                    ml = get_match_ids_by_puuid(p)
                    insert_mids_to_db(ml)



        match_id = get_random_match_id(cursor, cnx)


        if c % 400 == 0:
            cursor.close()
            cnx.close()
            cnx = mysql.connector.connect(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_password
            )
            cnx.autocommit = True
            cursor = cnx.cursor()
                

            



