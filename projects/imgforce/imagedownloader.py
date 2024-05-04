import requests
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






def download_image_and_update_db():
    # Connect to the database using the connection parameters in 'config'.
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    form = ".png"
    url = "https://i.imgur.com/"

    # Define custom User-Agent header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    try:
        while True:
            # Get a hash from the database where the 'downloaded' flag is NULL
            cursor.execute("SELECT hash FROM imgurhashes WHERE downloaded IS NULL ORDER BY RAND() LIMIT 1")
            r = cursor.fetchall()

            if not r:
                print("No more images to download.")
                break

            hs = r[0][0]

            # Send a GET request to the URL with custom User-Agent
            response = requests.get(url + hs + form, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                # Open a file in binary write mode
                with open("images/" + hs + form, 'wb') as file:
                    file.write(response.content)

                # Update the database to mark this image as downloaded
                cursor.execute("UPDATE imgurhashes SET downloaded = TRUE WHERE hash = %s", (hs,))
                connection.commit()

                print("Image downloaded and database updated successfully.")
            else:
                print("Failed to retrieve the image. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    download_image_and_update_db()

if __name__ == "__main__":
    download_image_and_update_db()