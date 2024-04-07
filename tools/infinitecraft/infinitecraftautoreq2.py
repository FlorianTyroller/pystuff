import random
import time
import pyautogui
import random
import pydirectinput
import requests



def combine_items(first_item, second_item):
    base_url = "https://neal.fun/api/infinite-craft/pair"
    params = {"first": "Fog", "second": "Tea"}
    headers = {
        "Authority": "neal.fun",
        "Method": "GET", 
        "Path": "/api/infinite-craft/pair?first=Fog&second=Tea", 
        "Scheme": "https",
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "_ga=GA1.1.1675636985.1708101793; _ga_L7MJCSDHKV=GS1.1.1709062441.14.0.1709062441.0.0.0",
        "If-Modified-Since": "Mon, 26 Feb 2024 09:46:36 GMT",
        "Referer": "https://neal.fun/infinite-craft/",
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Opera GX\";v=\"107\", \"Chromium\";v=\"121\"",
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty", 
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
    }
    response = requests.get(base_url, params=params, headers=headers)
    print(response)


if __name__ == "__main__":
    item1 = "Fog"
    item2 = "Tea"
    combine_items(item1, item2)
       
