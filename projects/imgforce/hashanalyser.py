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

count_dict = dict()

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for c in chars:
    count_dict[c] = 0


config = {
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'host': MYSQL_HOST, 
    'database': MYSQL_DATABASE,
    'port': MYSQL_PORT
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

q = "select hash from imgurhashes"
cursor.execute(q)

result = cursor.fetchall()
for r in result:
    for c in r[0]:
        count_dict[c] += 1

print(count_dict)

cursor.close()
connection.close()