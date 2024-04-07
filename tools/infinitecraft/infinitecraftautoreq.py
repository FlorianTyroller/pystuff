from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
import random
import time
import pyautogui
import random
import pydirectinput
import requests

service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=chrome_options)



# URL to open
url = "https://neal.fun/infinite-craft/"

def combine_items(driver, first_item, second_item):
    base_url = "https://neal.fun/api/infinite-craft/pair"
    params = {"first": first_item, "second": second_item}
    headers = {
        "Authority": "neal.fun",
        "Method": "GET", 
        "Path": "/api/infinite-craft/pair?first=Abominable%20Snowman&second=Yeti", 
        "Scheme": "https",
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6",
        "Referer": "https://neal.fun/infinite-craft/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty", 
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(base_url, params=params, headers=headers)
    print(response)


def get_discovered_items(driver):
    container = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.sidebar > div.sidebar-inner > div')
    item_elements = container.find_elements(By.CLASS_NAME, "item")  # Adjust the class name if needed
    return [item.text for item in item_elements]


if __name__ == "__main__":
    driver.get(url)
    time.sleep(3)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button')))
    element.click()
    time.sleep(1)
    while True:
        discovered_items = get_discovered_items(driver)
        if len(discovered_items) >= 2:
            first_item, second_item = random.sample(discovered_items, 2) 
            combine_items(driver, first_item, second_item)
        else:
            print("Not enough items discovered yet")
            time.sleep(2)

    driver.quit()