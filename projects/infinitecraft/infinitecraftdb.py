import mysql.connector
import requests
import os
import json
import httpx
import random
import time
from fake_useragent import UserAgent

# Connect to your MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='ruser',
    password='root',
    database='infinitecraft'
)
COUNTER_FILE = "projects/infinitecraft/counter_file.json"
PROXY_FILE = "projects/infinitecraft/proxies.json"
proxy_list = {}


# URL to open
url = "https://neal.fun/infinite-craft/"

def save_counter_file(counter_file):
    with open(COUNTER_FILE, "w") as f:
        json.dump(counter_file, f)

def load_counter_file():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def load_proxies(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if the file is not found or corrupt

def save_proxies(filename, proxies):
    with open(filename, 'w') as f:
        data = {} 
        for proxy, score in proxies.items():
            data[proxy] = score
        json.dump(data, f, indent=2) 


def insert_element(name, isNew):
    cursor = conn.cursor()

    # Check if the element already exists
    check_query = "SELECT id FROM elements WHERE name = %s"
    cursor.execute(check_query, (name,))
    result = cursor.fetchone()

    if result:  # Element exists
        element_id = result[0]  # Extract the ID
        print("Element already exists!")
    else:  # Element doesn't exist
        try:
            query = "INSERT INTO elements (name, isNew) VALUES (%s, %s)"
            values = (name, isNew)
            cursor.execute(query, values)
            conn.commit() 
            element_id = cursor.lastrowid  # Get the ID of the inserted row 
            print("Element inserted successfully!")
        except mysql.connector.Error as err:
            print("Error inserting element:", err)
            return None  # Indicate failure
    
    cursor.close()
    return element_id 

    

    

def insert_craft(result_id, item_1_id, item_2_id):
    # item_1_id should always be smaller 
    if item_1_id > item_2_id:
        item_1_id, item_2_id = item_2_id, item_1_id

    cursor = conn.cursor()

    # SQL query using placeholders for security
    query = "INSERT INTO crafts (result_id, item_1_id, item_2_id) VALUES (%s, %s, %s)"
    values = (result_id, item_1_id, item_2_id)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Craft inserted successfully!")
    except mysql.connector.Error as err:
        print("Error inserting Craft:", err)
    finally:
        cursor.close()

def req_combination(params):
    ua = UserAgent()
    base_url = "https://neal.fun/api/infinite-craft/pair"
    headers = {
        "Referer": "https://neal.fun/infinite-craft/",
        "User-Agent": ua.random,
        "Connection": "keep-alive"
    }


    while True:  # Loop to handle potential proxy failures
        try:
            """# random choice with weight
            proxy = random.choices(population=list(proxy_list.keys()), weights=list(proxy_list.values()), k=1)[0]
            if proxy == "no proxy":
                proxies = None
            else:
                proxies = {
                    'https://': proxy  # Format the proxy for httpx
                }"""


            #with httpx.Client(proxies=proxies, verify=True) as client:
            with httpx.Client(verify=True) as client:
                response = client.get(base_url, params=params, headers=headers, timeout=5)

                if response.status_code == 200: 
                    try:
                        response_string = response.content
                        # Decode from bytes to a string
                        response_str = response_string.decode('utf-8')
                        # Load the JSON string into a dictionary
                        response_dict = json.loads(response_str)
                        proxy_list[proxy] += 0.1
                        return response_dict  # Successful request
                    except Exception as err:
                        proxy_list[proxy] *= 0.9
                        print(f"Error decoding response: {err}. Trying another...")
                else:
                    proxy_list[proxy] *= 0.9
                    print(response.status_code)
                    print(f"Proxy failed ({proxy}). Trying another...")

        except httpx.ProxyError as err:
            proxy_list[proxy] *= 0.9
            print(f"Proxy error ({proxy}): {err}. Trying another...")
        except Exception as err:
            proxy_list[proxy] *= 0.9
            print(f"Connection error ({proxy}): {err}. Trying another...")



def combine_items(first_item, second_item, tries = 1):
    params = {"first": first_item[1], "second": second_item[1]}


    response_dict = req_combination(params)

    if response_dict["result"] != "Nothing":
        e_id = insert_element(response_dict["result"], response_dict["isNew"])
        if e_id:
            insert_craft(e_id, first_item[0], second_item[0])
        else:
            print("no valid e_id")
            return -1
    else:
        insert_craft(-1, first_item[0], second_item[0])
    return 0



if __name__ == "__main__":
    proxy_list = load_proxies(PROXY_FILE)
    print(proxy_list)
    cf = load_counter_file()
    counter = 0
    if "counter" in cf:
        counter = cf["counter"]
    while True:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM elements Limit %s" % counter)
        
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("No elements selected")
            counter += 1
            cf["counter"] = counter
            save_counter_file(cf)
            exit()
        item1 = rows[-1]
        if item1[0] < counter:
            print("not enough elements to process")
            exit()

        for row in rows:
            if combine_items(row, item1):
                print("error")
                exit()


        counter += 1
        cf["counter"] = counter
        cursor.close()
        save_counter_file(cf)
        save_proxies(PROXY_FILE, proxy_list)
