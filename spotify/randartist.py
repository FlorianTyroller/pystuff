import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
import string
import random


cid = "7d26ad9f583e49819547f62271bc2da7"
secret = "ee3d5c1ebb974081bfb354914655600a"
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_random_term():
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

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

def main3():
    r = 100
    dupes = 0
    artist_ids = []
    artist_names = []
    for i in range(r):
        a_id, a_name = get_random_artist(get_random_term())
        if a_id not in artist_ids:
            artist_ids.append(a_id)
            artist_names.append(a_name)
        else:
            dupes += 1
            print("# of dupes: ", dupes)

    print(artist_names)




def main():
    # Define the playlist genres and their frequencies
    playlist_genres = {"pop": 20, "rock": 31, "edm": 120}

    # Define an example artist with genres
    artist_genres = ["rnb", "rock", "edm", "jazz"]

    # Calculate the genre score for the artist
    genre_score = calculate_genre_score(playlist_genres, artist_genres)

    # Print the genre score
    print(genre_score)

if __name__ == "__main__":
    main()