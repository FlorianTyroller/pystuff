import os
import praw
import urllib.request
from PIL import Image

# Set up your Reddit API credentials
reddit = praw.Reddit(client_id='E0NnFV0q8LK30Arvx44qlA', client_secret='lvwXkHKAAXZoV5sPoNDoYVr9eamjhw', user_agent='face ai')

# Specify the subreddit and number of posts to download
names=  ['transadorable', 'trans', 'transpositive']
for subreddit_name in names:

    num_posts = 1000

    # Get the top x posts from the subreddit
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(limit=num_posts)

    # Create a directory to store the downloaded images
    os.makedirs(subreddit_name, exist_ok=True)

    # Loop through the top posts and download and convert their images to JPEG
    for post in top_posts:
        if post.url.endswith('.jpg') or post.url.endswith('.png') or post.url.endswith('.webp'):
            image_url = post.url
            file_name = os.path.join(subreddit_name, os.path.basename(image_url))
            try:
                urllib.request.urlretrieve(image_url, file_name)
                print(f"Downloaded {file_name}")
                with Image.open(file_name) as im:
                    rgb_im = im.convert('RGB')
                    new_file_name = os.path.splitext(file_name)[0] + '.jpg'
                    rgb_im.save(new_file_name, quality=95)
                    print(f"Converted {file_name} to JPEG format")
            except:
                print(f"Failed to download or convert {file_name}")
