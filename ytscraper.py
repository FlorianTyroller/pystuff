import requests

api_key = "AIzaSyA8ECBVlPq98_ZQsurlLeDyggAMXKfeOHw"
video_id = "V9qjgnn7LdU"

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

response = requests.get(url)

data = response.json()

print(data)
