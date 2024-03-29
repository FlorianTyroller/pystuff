import requests
from datetime import datetime, timezone, timedelta
import json
import os
import dotenv
import time


dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')


def read_summoner_info():
    summoners = {}
    try:
        with open("lolapi/summoner_info.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Summoner Name: "):
                    summoner_name = line.replace("Summoner Name: ", "")
                    puuid = f.readline().strip().replace("PUUID: ", "")
                    sid = f.readline().strip().replace("ID: ", "")
                    summoners[summoner_name] = [puuid, sid]
    except FileNotFoundError:
        print("File not found.")
    return summoners




def get_summoner_rank(summoner_id):
    # Define the base URL for retrieving summoner's ranked league information
    SUMMONER_RANK_URL = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"

    # Send a request to the API to retrieve summoner's ranked league information
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(SUMMONER_RANK_URL, headers=headers)

    # Parse the response and return the rank information if the response status code is 200
    if response.status_code == 200:
        rank_info = response.json()
        if rank_info:
            return rank_info
    return None


def has_played_recent_game(summoner_name, puuid, summoner_id, last_game_id, rank_stats):
    # Define the base URL for retrieving match history
    MATCH_HISTORY_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid"

    # Send a request to the API to retrieve match history
    url_str = f"{MATCH_HISTORY_URL}/{puuid}/ids"
    # put api key in header
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url_str, headers=headers)

    # Parse the response and check if any matches were played within the last 24 hours
    if response.status_code == 200:
        match_history = response.json()
        last_game = match_history[0]
        # check if the last game is the same as the last game checked
        if last_game == last_game_id:
            return None
        
        MATCH_CHECK_URL = f"https://europe.api.riotgames.com/lol/match/v5/matches/{last_game}"
        
        response = requests.get(MATCH_CHECK_URL, headers=headers)

        if response.status_code == 200:
            
            match = response.json()
            end_time = match["info"]["gameEndTimestamp"]
            
            won_last_game = False
            # check if it the player with the puuid won the game
            for participant in match["info"]["participants"]:
                if participant["puuid"] == puuid:
                    if participant["win"]:
                        won_last_game = True
            
            game_mode = match["info"]["gameMode"]

            # get the summoner's rank
            summoner_info = get_summoner_rank(summoner_id)
            rank_keys = ["tier", "rank", "leaguePoints", "wins", "losses", "hotStreak"]
            rank_info = {"solo": {}, "flex": {}}
            if summoner_info:
                for r_infos in summoner_info:
                    if r_infos["queueType"] == "RANKED_SOLO_5x5":
                        for key in rank_keys:
                            rank_info["solo"][key] = r_infos[key]
                    elif r_infos["queueType"] == "RANKED_FLEX_SR":
                        for key in rank_keys:
                            rank_info["flex"][key] = r_infos[key]

            # compare with rank_stats
            if rank_stats:
                for qtype in ["solo", "flex"]:
                    c = False
                    if "tier" in rank_stats[qtype] and "tier" in rank_info[qtype]:
                        if rank_stats[qtype]["tier"] != rank_info[qtype]["tier"]:
                            c = True
                    if "rank" in rank_stats[qtype] and "rank" in rank_info[qtype]:
                        if rank_stats[qtype]["rank"] != rank_info[qtype]["rank"]:
                            c = True
                    if "leaguePoints" in rank_stats[qtype] and "leaguePoints" in rank_info[qtype]:
                        if rank_stats[qtype]["leaguePoints"] != rank_info[qtype]["leaguePoints"]:
                            c = True
                    
                    if c:
                        print(f"summmoner {summoner_name} has changed rank in {qtype} queue")
                        print(f"old rank: {rank_stats[qtype]['tier']} {rank_stats[qtype]['rank']}, {rank_stats[qtype]['leaguePoints']} LP")
                        print(f"new rank: {rank_info[qtype]['tier']} {rank_info[qtype]['rank']}, {rank_info[qtype]['leaguePoints']} LP")



            timestamp = datetime.fromtimestamp(end_time / 1000, timezone.utc)

            return {"summoner_name": summoner_name,"sid": summoner_id, "puuid": puuid, "last_game": last_game, "last_game_time": timestamp.isoformat(), "won_last_game": won_last_game, "game_mode": game_mode, "rank_info": rank_info}
            
    return None


def initialize_summoner_data(summoners):

    summoners = read_summoner_info()

    # Create an empty list to store the summoner data
    summoner_data = []

    # Check if each summoner has played a game within the last 24 hours
    for summoner_name, info in summoners.items():
        data = has_played_recent_game(summoner_name, info[0], info[1], None, None)
        
        if data:
            summoner_data.append(data)
        
        # sleep for 1.2 seconds to avoid rate limiting
        time.sleep(1.2)
    

def save_summoner_data(JSON_FILENAME, summoner_data):
    # Save the summoner data as JSON
    with open(JSON_FILENAME, "w") as f:
        json.dump(summoner_data, f, indent=4)


def check_for_new_games(JSON_FILENAME):
    # Read the summoner data from the JSON file
    new_summoner_data = []
    # read summoners from summoner_info.txt
    summoner_ids = read_summoner_info()
    checked_summoners = []
    with open(JSON_FILENAME, "r") as f:
        try:
            summoner_data = json.load(f)
        except json.decoder.JSONDecodeError:
            summoner_data = []
        for summoner in summoner_data:
            puuid = summoner["puuid"]
            sid = summoner["sid"]
            summoner_name = summoner["summoner_name"]
            last_game = summoner["last_game"]
            rank_stats = summoner["rank_info"]
            data = has_played_recent_game(summoner_name, puuid, sid, last_game, rank_stats)
            if data:
                new_summoner_data.append(data)
            else:
                new_summoner_data.append(summoner)
            
            checked_summoners.append(summoner_name)
            # sleep for 1.2 seconds to avoid rate limiting
            time.sleep(1.2)
        # check if any new summoners have been added to the summoner_info.txt file
        for summoner_name, info in summoner_ids.items():
            if summoner_name not in checked_summoners:
                print(f"Checking new summoner: {summoner_name}")
                data = has_played_recent_game(summoner_name, info[0], info[1], None, None)
                if data:
                    new_summoner_data.append(data)
                    print(f"{summoner_name} has played a new game.")
                else:
                    new_summoner_data.append(summoner)
                # sleep for 1.2 seconds to avoid rate limiting
                time.sleep(1.2)
    # Save the summoner data as JSON
    save_summoner_data(JSON_FILENAME, new_summoner_data)

def main():
    JSON_FILENAME = "lolapi/summoner_data.json"
    check_for_new_games(JSON_FILENAME)


if __name__ == '__main__':
    main()
    
