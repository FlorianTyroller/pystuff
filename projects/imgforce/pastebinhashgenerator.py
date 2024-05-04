from imgurpython import ImgurClient
import asyncio
import time
import random
import string
import base64
import threading
#import requests
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

config = {
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'host': MYSQL_HOST, 
    'database': MYSQL_DATABASE,
    'port': MYSQL_PORT
}

async def insert_hash_to_db(hashs):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    q = "INSERT INTO pastebinhashes (hash) VALUES (%s)"
    try:
        cursor.execute(q, (hashs,))
        connection.commit()
    finally:
        cursor.close()
    
# Function to generate random base64 string
def generate_random_base64(length):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ha = ""
    for i in range(length):
        ha += random.choice(chars)
    return ha


async def check_multiple_hashes():
    task_count_pastebin = 10  # Adjust as needed
    checked = 0
    found = 0

    while True:
        hl = [generate_random_base64(8) for i in range(task_count_pastebin)]
        
        url = "https://pastebin.com/"

        async with httpx.AsyncClient() as client:
            reqs = [client.get(url + h) for h in hl]
            responses = await asyncio.gather(*reqs, return_exceptions=True)

        ratelimit = 0
        for h, response in zip(hl, responses):
            if isinstance(response, httpx.Response):
                rc = response.status_code
                if rc == 200:
                    found += 1
                    await insert_hash_to_db(h)
                elif rc == 429:
                    ratelimit += 1
                elif rc == 404:
                    # print(h,rc)
                    pass
            elif isinstance(response, Exception):
                print(response)
        if ratelimit == 0:
            task_count_pastebin += 1
        else:
            task_count_pastebin -= ratelimit
            if task_count_pastebin <= 0:
                task_count_pastebin = 1
        checked += task_count_pastebin - ratelimit
        print("ratelimited:", ratelimit, "new task_count_pastebin:", task_count_pastebin, "found:", found, "checked:", checked)

if __name__ == '__main__':
    asyncio.run(check_multiple_hashes())