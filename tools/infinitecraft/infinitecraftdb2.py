from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
import time
from selenium_stealth import stealth
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import json
import os
import mysql.connector
import random
import urllib.parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from dotenv import load_dotenv
import traceback
import urllib.parse

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

service = Service(
    executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()
#chrome_options = uc.ChromeOptions()
# Example User-Agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
ua = UserAgent()
chrome_options.add_argument(f'user-agent={user_agent}')
# Path to your Chrome executable
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chrome_options.add_argument(
    "user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\tools\\infinitecraft\\seleniumexploitdb")
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(service=service, options=chrome_options)
driver = Chrome(service=service, options=chrome_options)


stealth(driver,
        languages=["en-US", "en"],
        vendor="Apple Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )



url = "https://neal.fun/infinite-craft/"


def insert_element(name, isNew):
    cursor = conn.cursor()

    # Check if the element already exists
    check_query = "SELECT id FROM elements WHERE name = %s"
    cursor.execute(check_query, (name,))
    result = cursor.fetchone()

    if result:  # Element exists
        element_id = result[0]  # Extract the ID
        # print("Element already exists!")
    else:  # Element doesn't exist
        try:
            query = "INSERT INTO elements (name, isNew) VALUES (%s, %s)"
            values = (name, isNew)
            cursor.execute(query, values)
            conn.commit()
            element_id = cursor.lastrowid  # Get the ID of the inserted row
            # print("Element inserted successfully!")
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
        # print("Craft inserted successfully!")
    except mysql.connector.Error as err:
        print("Error inserting Craft:", err)
    finally:
        cursor.close()


def send_request_through_browser2(api_url, params):
    start_time = time.time()  # Record the start time

    params_str = urllib.parse.urlencode(params)
    full_url = f"{api_url}?{params_str}"
    script = f"""
    fetch('{full_url}', {{
        method: 'GET'
    }})
    .then(response => {{
        if (response.status === 429) {{
            // Extract retry-after header (if present)
            const retryAfterSeconds = response.headers.get('Retry-After');
            window.__selenium_error__ = {{code: 429, retryAfter: retryAfterSeconds}};
        }} else {{
            window.__selenium_data__ = response.json();
        }}
    }});
    """
    driver.execute_script(script)
    time.sleep(0.15)
    # Wait for the data to be available
    try:
        result = WebDriverWait(driver, 10, poll_frequency=0.02).until(lambda driver: driver.execute_script("return window.__selenium_data__"))
        # print(f"after wait: {time.time() - start_time} seconds")
    except Exception as e:
        print("Timeout: Response data was not retrieved.", e)
        return None

    if result:
        if 'code' in result and result['code'] > 200:

            print("Code:", result['code'])
            time.sleep(1)
            return None
        else:
            print(result, params)
            # print(f"Before delete: {time.time() - start_time} seconds")
            # driver.execute_script("delete window.__selenium_data__;")
            end_time = time.time()  # Record the end time
            # print(f"Execution time: {end_time - start_time} seconds")
            return result  # Return the data if available

    return None

def selenium_cookies_to_requests(cookies):
    requests_cookies = {}
    for cookie in cookies:
        requests_cookies[cookie['name']] = cookie['value']

    # Prepare INSERT INTO query with ON DUPLICATE KEY UPDATE
    insert_query = "INSERT INTO cookies (proxiename, cjson) VALUES (%s, %s) ON DUPLICATE KEY UPDATE cjson = VALUES(cjson)"

    # Convert cookies dictionary to JSON string
    cjson = json.dumps(requests_cookies)

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(insert_query, (proxiename, cjson))

    # Commit the changes
    conn.commit()
    print("inserted Cookies")

    return requests_cookies

def get_cookies_from_mysql(proxiename):
    # Prepare SELECT query
    select_query = "SELECT cjson FROM cookies WHERE proxiename = %s"

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(select_query, (proxiename,))

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


    cookies_for_requests = selenium_cookies_to_requests(driver.get_cookies())
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



def test_combintaion(first_item, second_item, result_item):
    params = {"first": first_item[1], "second": second_item[1]}
    api_url = "https://neal.fun/api/infinite-craft/pair"
    response_dict = send_request_through_browser4(api_url, params)

    if response_dict["result"] == result_item[1]:
        print("Test passed:", first_item, second_item, result_item)
    else:
        print("Test failed:", first_item, second_item, result_item, response_dict["result"])
        # fix mistake

        e_id = insert_element(response_dict["result"], response_dict["isNew"])

        sql = "Update crafts set depth = Null, result_id = %s where item_1_id = %s and item_2_id = %s"
        cursor.execute(sql, (e_id, first_item[0], second_item[0]))
        conn.commit()

        sql = "Update elements set depth = Null where id = %s"
        cursor.execute(sql, (e_id,))
        conn.commit()






def combine_items(first_item, second_item, tries=1):
    params = {"first": first_item[1], "second": second_item[1]}
    api_url = "https://neal.fun/api/infinite-craft/pair"
    

    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        response_dict = send_request_through_browser4(api_url, params)
        driver.execute_script("delete window.__selenium_data__;")

        if response_dict is not None:
            #print("Request successful:", result)
            break
        else:
            return
            print(f"Retry attempt {attempt + 1}...")

    if response_dict is None:
        print(f"Failed after {MAX_RETRIES} attempts.")

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

    driver.get(url)
    # Wait for manual input
    input("Press Enter in the console to continue...")

    try:
        r_id = 60
        element_names = {}
        while True:
            # input("Press Enter in the console to continue...")
            cursor = conn.cursor()
            
            cursor.execute("SELECT id,name FROM elements where id = %s", (r_id,))
            r_id += 1
            # Fetch the first (and only) result
            res = cursor.fetchone()
            random_element_id = res[0]
            r_element_name = res[1]

            # Build the query with the random element_id
            query = """
            SELECT DISTINCT e.id
            FROM elements e
            LEFT JOIN crafts c1 ON e.id = c1.item_1_id
            LEFT JOIN crafts c2 ON e.id = c2.item_2_id
            WHERE e.id < 2900 and NOT EXISTS (
                SELECT 1
                FROM crafts
                WHERE (%s = item_1_id AND e.id = item_2_id)
                OR (%s = item_2_id AND e.id = item_1_id)
            ) limit 2900;
            """
            # Execute the query
            cursor.execute(query, (random_element_id, random_element_id))

            # Get the results
            uncrafted_element_ids = cursor.fetchall()

            # Print the results
            # print("Uncrafted element IDs:")
            for i,result in enumerate(uncrafted_element_ids):
                if i % 20 == 0:
                    # test random craft
                    cursor.execute("SELECT * FROM crafts order by RAND() limit 1")
                    craft = cursor.fetchone()
                    if craft[0] > 0:
                        if craft[0] not in element_names:
                            cursor.execute("SELECT name FROM elements WHERE id = %s LIMIT 1", (craft[0],))
                            r_name = cursor.fetchone()[0]
                            element_names[craft[0]] = r_name
                        else:
                            r_name = element_names[craft[0]]
                        
                        if craft[1] not in element_names:
                            cursor.execute("SELECT name FROM elements WHERE id = %s LIMIT 1", (craft[1],))
                            i_1_name = cursor.fetchone()[0]
                            element_names[craft[1]] = i_1_name
                        else:
                            i_1_name = element_names[craft[1]]
                        
                        if craft[2] not in element_names:
                            cursor.execute("SELECT name FROM elements WHERE id = %s LIMIT 1", (craft[2],))
                            i_2_name = cursor.fetchone()[0]
                            element_names[craft[2]] = i_2_name
                        else:
                            i_2_name = element_names[craft[2]]
                        
                        test_combintaion([craft[1], i_1_name], [craft[2], i_2_name], [craft[0], r_name])


                    
                
                element_id = result[0]
                # Check if the element ID exists in the dictionary
                if element_id not in element_names:
                    # If not, execute the SELECT statement and fetch the name
                    cursor.execute("SELECT name FROM elements WHERE id = %s LIMIT 1", (element_id,))
                    element_name = cursor.fetchone()[0]
                    # Save the name in the dictionary
                    element_names[element_id] = element_name
                else:
                    # If the name is already in the dictionary, retrieve it from there
                    element_name = element_names[element_id]
                combine_items([element_id, element_name],[random_element_id,r_element_name] )

            cursor.close()
    except Exception as e:
        print(e)
        traceback.print_exc() 
        time.sleep(1000)
