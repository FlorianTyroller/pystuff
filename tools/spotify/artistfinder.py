import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
import string
import random

from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)




def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks



def get_analyse_playlist(playlist_URI):
    genres = defaultdict(int)
    artists = []
    for i, track in enumerate(get_playlist_tracks(playlist_URI)):

        if i % 10 == 0:
            print(f"Processing track {i}")

        #Main Artist
        
        try:
            artist_id = track["track"]["artists"][0]["id"]
            if artist_id not in artists:
                artists.append(artist_id)
            artist_info = sp.artist(artist_id)
        except:
            artist_id = "None"
            artist_info = "None"
        
        
        #Name, popularity, genre
        try:
            artist_name = track["track"]["artists"][0]["name"]
            artist_pop = artist_info["popularity"]
            artist_genres = artist_info["genres"]
            # add to dictionary
            for genre in artist_genres:
                genres[genre] += 1
        except:
            artist_name = "None"
            artist_pop = "None"
            artist_genres = "None"
    
    return artists, genres


def get_random_term():
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.ascii_letters + string.digits + string.punctuation

    # Generate a random search term of length 2 or 3
    search_term_length = random.choice([2, 3])
    search_term = ''.join(random.choice(characters) for _ in range(search_term_length))

    return search_term

def get_random_artist(search_term):

    # Search for artists using the random search term
    results = sp.search(q=search_term, type='artist')
    artists = results['artists']['items']

    # Choose a random artist from the search results
    if len(artists) == 0:
        print("No artists found for search term: {}".format(search_term))
        return None, None

    random_index = random.randint(0, len(artists)-1)
    artist = artists[random_index]

    # Get the full artist information using the artist's ID
    artist_id = artist['id']

    full_artist_info = sp.artist(artist_id)

    
    return artist_id, full_artist_info['name']


def calculate_genre_score(playlist_genres, artist_genres):
    """
    Calculates a score based on how well an artist's genres match the genres of the playlist.

    Args:
    playlist_genres (dict): A dictionary of playlist genres and their frequencies.
    artist_genres (list): A list of genres for the artist.

    Returns:
    float: A score between 0 and 1 representing how well the artist's genres match the genres of the playlist.
    """
    # Initialize variables for the total score and the number of genre matches
    total_score = 0
    num_matches = 0
    
    # Calculate the sum of frequencies of all genres in the playlist
    playlist_freq_sum = sum(playlist_genres.values())
    
    # Loop over each genre in the artist's list of genres
    for genre in artist_genres:
        # Check if the genre is in the playlist
        if genre in playlist_genres:
            # Calculate the score for this genre as the product of the artist's frequency and the normalized frequency of the genre in the playlist
            score = (playlist_genres[genre]/playlist_freq_sum)
            # Add the score to the total score and increment the number of matches
            total_score += score
            num_matches += 1
    
    # Return the average score per match, or 0 if there are no matches
    return total_score - (len(artist_genres) - num_matches) * 0.02 


def main():
    playlist_link = "https://open.spotify.com/playlist/21MJznW4JcFMu05FJnJ5F8?si=f6608f6478694b8c" # boi
    # playlist_link = "https://open.spotify.com/playlist/2qjvCnMRqXKbaMrQ5sQmK5?si=bf637615fddb4d55" # Premium
    # playlist_link = "https://open.spotify.com/playlist/1jaCtU6WldNGgi9LDfdPvE?si=f3661484a7334e03" # chillflex

    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    # track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

    artists, genres = get_analyse_playlist(playlist_URI)
    print(genres)
    r = 100
    dupes = 0
    c = 0
    artist_stats = []
    while r > 0:
        c += 1
        if c % 10 == 0:
            print("loop: ", c)
        a_id, a_name = get_random_artist(get_random_term())
        if a_id is None:
            continue
        if a_id in artists:
            dupes += 1
            print("# of dupes: ", dupes, " name:", a_name)
            continue

        gs = sp.artist(a_id)["genres"]
        if len(gs) > 0:
            a_score = calculate_genre_score(genres, gs)
            artists.append(a_id)
            artist_stats.append((a_name, a_score))
            if a_score > 0.1:
                print("new artist: ", a_name, " score: ", a_score)
                r -= 1

            

    # sort by score
    artist_stats.sort(key=lambda x: x[1], reverse=True)
    print(artist_stats)




if __name__ == "__main__":
    main()