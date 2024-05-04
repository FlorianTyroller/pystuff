import asyncio
import time
import random
import string
import base64
import threading
import httpx
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")
IMGUR_CLIENT_IDS = [os.getenv("IMGUR_CLIENT_ID_" + str(i) ) for i in range(1,21)]


config = {
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'host': MYSQL_HOST, 
    'database': MYSQL_DATABASE,
    'port': MYSQL_PORT
}

async def download_image(url):
   # Extract the filename from the URL
    filename = os.path.basename(url)

    # Create a client and send a GET request to the URL
    with httpx.Client() as client:
        response = client.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary write mode using the extracted filename
        with open("images/" + filename, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully as {filename}.")
        return True
    else:
        print("Failed to retrieve the image. Status code:", response.status_code)
        return False


async def insert_hash_in_db(hashs, response):
    rj = response.json()
    rdata = rj['data']
    datetime = rdata['datetime']
    itype = rdata['type']
    width = rdata['width']
    height = rdata['height']
    size = rdata['size']
    views = rdata['views']
    nsfw = rdata['nsfw']
    is_ad = rdata['is_ad']
    is_animated = rdata['animated']
    has_sound = rdata['has_sound']
    link = rdata['link']
    downloaded = await download_image(link)
    try:
        description = rdata['description'][:150]
    except:
        description = None
    
    try:
        title = rdata['title'][:90]
    except:
        title = None
    
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Formulate the SQL insert statement
    q = """
    INSERT INTO imgurhashes (hash, datetime, type, width, height, size, views, nsfw, is_ad, 
                             is_animated, has_sound, link, description, title, downloaded)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Tuple of parameters to pass to the query
    params = (hashs, datetime, itype, width, height, size, views, nsfw, is_ad, is_animated, has_sound, link, description, title, downloaded)

    try:
        cursor.execute(q, params)
        connection.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as error:
        print("Failed to insert record to database: {}".format(error))
    finally:
        cursor.close()
        connection.close()
    
# Function to generate random base64 string
def generate_random_base64(length):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ha = ""
    for i in range(length):
        ha += random.choice(chars)
    return ha


async def check_multiple_hashes():
    task_count_imgur = 20  # Adjust as needed
    checked = 0
    found = 0
    timeout = 1
    curr_client_id = 0
    while True:
        headers = dict()
        # headers['Authorization'] = 'Client-ID %s' % IMGUR_CLIENT_IDS[curr_client_id%len(IMGUR_CLIENT_IDS)]


        # select client id
        client_id = IMGUR_CLIENT_IDS[curr_client_id%len(IMGUR_CLIENT_IDS)]

        # check how many uses the id has left

        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.imgur.com/3/credits", headers={"Authorization": 'Client-ID %s' % client_id}, timeout = 30)
            if response.status_code == 429:
                print("rate limted, sleeping for 20 seconds...")
                time.sleep(20)
                continue
            data = response.json()
        
        uses_left = data["data"]["ClientRemaining"]

        # if not enough uses skip client id, increment before anyways to cycle 
        curr_client_id += 1
        if uses_left < 200:
            print("Client Id:", curr_client_id%len(IMGUR_CLIENT_IDS), "has only", uses_left, "uses left. Sleeping for 10 seconds then skipping to next ...")
            time.sleep(10)
            continue
        
        number_of_loops = 10

        for _ in range(number_of_loops):
            # generate hashes list
            hl = [generate_random_base64(7) for i in range(task_count_imgur)]


            # URL for imgur image get api
            url = "https://api.imgur.com/3/image/"

            async with httpx.AsyncClient() as client:
                reqs = [client.get(url + h, headers = {"Authorization": 'Client-ID %s' % client_id}, timeout = 30) for h in hl]
                responses = await asyncio.gather(*reqs, return_exceptions=True)

            for h, response in zip(hl, responses):
                if isinstance(response, httpx.Response):
                    rc = response.status_code
                    if rc == 200:
                        found += 1
                        await insert_hash_to_db(h, response)
                    elif rc == 404:
                        #print(response)
                        #print(response.content)
                        pass
                    elif rc == 429:
                        print("rate limted, sleeping for 20 seconds...")
                        time.sleep(20)
                    else:
                        print("response code:",rc)
                elif isinstance(response, Exception):
                    print("EXCEPTION:", response)
        
            checked += task_count_imgur 
            print("found:", found, "checked:", checked)
            time.sleep(1.5)

if __name__ == '__main__':
    asyncio.run(check_multiple_hashes())