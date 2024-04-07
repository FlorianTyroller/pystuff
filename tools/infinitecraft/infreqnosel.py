import requests
import mysql.connector
import json
import urllib.parse
from dotenv import load_dotenv
import os
import time
# Load environment variables from .env file
load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

proxiename = "noproxie"
# Connect to the database
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

def get_cookies_from_mysql(pname):
    # Prepare SELECT query
    select_query = "SELECT cjson FROM cookies WHERE proxiename = %s"

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(select_query, (pname,))

    # Fetch the result
    result = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Check if result exists
    if result:
        # Convert JSON string to dictionary
        cookies_dict = json.loads(result[0])
        return cookies_dict
    else:
        return None

def send_request_through_browser4(api_url, params):
    first_item = urllib.parse.quote(params['first'])
    second_item = urllib.parse.quote(params['second'])


    cookies_for_requests = get_cookies_from_mysql(proxiename)
    path = f"/api/infinite-craft/pair?first={first_item}&second={second_item}"
    params_h = {"first": first_item, "second": second_item}
    headers = {
        "Authority": "neal.fun",
        "Method": "GET", 
        "Path": path, 
        "Scheme": "https",
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://neal.fun/infinite-craft/",
        "Sec-Fetch-Dest": "empty", 
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    #print(params_h, params, headers, api_url)
    response = requests.get(api_url, params=params, headers=headers, cookies=cookies_for_requests)
    time.sleep(0.15)
    #print(response.status_code)
    if response.status_code != 200:
        print(response.status_code)
        return None
    
    response_bytes = response.content
    try:
        

        # Find the position of the first '{' and the last '}' in the bytes response
        start_index = response_bytes.find(b'{')
        end_index = response_bytes.rfind(b'}')

        # Extract the JSON part from the bytes response
        json_bytes = response_bytes[start_index:end_index + 1]

        # Decode the JSON bytes into a string
        json_str = json_bytes.decode('utf-8')

        # Parse the JSON string into a Python dictionary
        response_json = json.loads(json_str)
        print(response_json, params)
        return response_json
    except Exception as e:
        print("Error parsing JSON:", e)
        print("Error parsing JSON:", response_bytes)
        #print(response.json())
        return None

if __name__ == "__main__": 
    print(send_request_through_browser4("https://neal.fun/api/infinite-craft/pair", {'first': 'Ocean', 'second': 'Ocean'}))