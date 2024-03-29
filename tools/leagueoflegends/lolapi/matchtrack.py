import os
import dotenv
import requests
import time

dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')

BASE_URL = 'https://europe.api.riotgames.com'

def get_match_data(match_id):
    url = f"{BASE_URL}/lol/match/v5/matches/{match_id}"
    headers = {'X-Riot-Token': API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        match_data = response.json()
        participants = match_data['info']['participants']

        team1_picks = []
        team2_picks = []
        duplicate_picks = []
        
        for index, participant in enumerate(participants, start=1):
            champion_name = participant['championName']
            team_id = participant['teamId']
            
            if team_id == 100:
                team1_picks.append(champion_name)
            elif team_id == 200:
                team2_picks.append(champion_name)
            
            if champion_name in team1_picks and champion_name in team2_picks:
                duplicate_picks.append((index, champion_name))
        
        if duplicate_picks:
            print(f"Match {match_id} has duplicate champion picks. Skipping...")
        else:
            with open("champion_picks.txt", "a") as file:
                file.write(f"Match {match_id} - Champion Pick Order:\n")
                file.write("Team 1 Picks:\n")
                for index, champion_name in enumerate(team1_picks, start=1):
                    file.write(f"Pick {index}: {champion_name}\n")
                file.write("\nTeam 2 Picks:\n")
                for index, champion_name in enumerate(team2_picks, start=1):
                    file.write(f"Pick {index}: {champion_name}\n")
                file.write("\n")
        

        win = match_data['info']['participants'][0]['win']
        winning_team_id = 100 if win else 200
        if winning_team_id == 100:
            print("Team 1 won the match.")
        elif winning_team_id == 200:
            print("Team 2 won the match.")
        else:
            print("Match result: Unknown")
        
    elif response.status_code >= 400 and response.status_code < 500:
        print(f"Match {match_id} not found. Skipping...")
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting 10 seconds...")
        time.sleep(10)
    else:
        print(f"Error occurred while requesting match {match_id}. Status code: {response.status_code}")

def increment_match_id(match_id):
    prefix, number = match_id.split('_')
    incremented_number = str(int(number) + 1)
    return f"{prefix}_{incremented_number}"

def main():
    start_id = "EUW1_6406824480"  # Replace with your desired initial match ID

    while True:
        get_match_data(start_id)
        start_id = increment_match_id(start_id)

if __name__ == '__main__':
    main()