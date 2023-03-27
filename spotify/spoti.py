import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict


cid = "7d26ad9f583e49819547f62271bc2da7"
secret = "ee3d5c1ebb974081bfb354914655600a"
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
# playlist_link = "https://open.spotify.com/playlist/21MJznW4JcFMu05FJnJ5F8?si=f6608f6478694b8c" # boi
# playlist_link = "https://open.spotify.com/playlist/2qjvCnMRqXKbaMrQ5sQmK5?si=bf637615fddb4d55" # Premium
playlist_link = "https://open.spotify.com/playlist/1jaCtU6WldNGgi9LDfdPvE?si=f3661484a7334e03" # chillflex

playlist_URI = playlist_link.split("/")[-1].split("?")[0]
# track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

genres = defaultdict(int)

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


for i, track in enumerate(get_playlist_tracks(playlist_URI)):
    # print a status message every 10 tracks
    if i % 10 == 0:
        print(f"Processing track {i}")

    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]

    
    
    #Main Artist
    
    try:
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
    except:
        artist_uri = "None"
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
    
    #Album
    try:
        album = track["track"]["album"]["name"]
    except:
        album = "None"
    
    #Popularity of the track
    try:
        track_pop = track["track"]["popularity"]
    except:
        track_pop = "None"

# graph the genres, only shot the top 10 genres and sort them by occurence
import matplotlib.pyplot as plt
import numpy as np

genres = dict(sorted(genres.items(), key=lambda item: item[1], reverse=True)[:10])
plt.bar(genres.keys(), genres.values())
plt.xticks(rotation=90)
plt.show()


