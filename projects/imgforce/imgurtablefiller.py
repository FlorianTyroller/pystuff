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
from datetime import datetime

load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")
IMGUR_CLIENT_IDS = [os.getenv("IMGUR_CLIENT_ID_" + str(i) ) for i in range(1,3)]


config = {
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'host': MYSQL_HOST, 
    'database': MYSQL_DATABASE,
    'port': MYSQL_PORT
}

async def update_hash_in_db(hashs, response):
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

    # Formulate the SQL update statement
    q = """
    UPDATE imgurhashes 
    SET datetime = %s, type = %s, width = %s, height = %s, size = %s, views = %s,
        nsfw = %s, is_ad = %s, is_animated = %s, has_sound = %s, link = %s, 
        description = %s, title = %s
    WHERE hash = %s
    """

    # Tuple of parameters to pass to the query
    params = (datetime, itype, width, height, size, views, nsfw, is_ad, is_animated, has_sound, link, description, title, hashs)

    try:
        cursor.execute(q, params)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
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
    task_count_imgur = 5  # Adjust as needed
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
        
        uses_left = data["data"]["UserRemaining"]

        # if not enough uses skip client id, increment before anyways to cycle 
        curr_client_id += 1
        if uses_left < 20:
            print("Client Id:", curr_client_id%len(IMGUR_CLIENT_IDS), "has only", uses_left, "uses left. Sleeping for 40 seconds then skipping to next ...")
            time.sleep(40)
            continue
        
        number_of_loops = 10

        for _ in range(number_of_loops):
            # generate hashes list
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            cursor.execute("select hash from imgurhashes where link is NULL limit %s", (task_count_imgur,))
             # Fetch all results from the cursor.
            hl = cursor.fetchall() 

            # Close the cursor and connection.
            cursor.close()
            connection.close()

            # URL for imgur image get api
            url = "https://api.imgur.com/3/image/"

            async with httpx.AsyncClient() as client:
                reqs = [client.get(url + h[0], headers = {"Authorization": 'Client-ID %s' % client_id}, timeout = 30) for h in hl]
                responses = await asyncio.gather(*reqs, return_exceptions=True)

            for h, response in zip(hl, responses):
                if isinstance(response, httpx.Response):
                    rc = response.status_code
                    if rc == 200:
                        found += 1
                        await update_hash_in_db(h[0], response)
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
            time.sleep(5)

if __name__ == '__main__':
    asyncio.run(check_multiple_hashes())