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
import pickle
import os
import json

service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()

chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\projects\\infinitecraft\\seleniumexploit")
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=chrome_options)
COMBINE_LIST_FILE = "projects/infinitecraft/combine_list_exploit.json"
style_mods = {
    'translate': '439.74px 389.903px',
}

MAX_RETRIES = 10

# URL to open
url = "https://neal.fun/infinite-craft/"
"""
def save_combine_list(combine_list):
    with open(COMBINE_LIST_FILE, "wb") as f:
        pickle.dump(combine_list, f)

def load_combine_list():
    if os.path.exists(COMBINE_LIST_FILE):
        with open(COMBINE_LIST_FILE, "rb") as f:
            e = pickle.load(f)
            print(e)
            return e
    else:
        return {}  # Return an empty dictionary if the file doesn't exist
"""
def save_combine_list(combine_list):
    with open(COMBINE_LIST_FILE, "w") as f:
        json.dump(combine_list, f)

def load_combine_list():
    if os.path.exists(COMBINE_LIST_FILE):
        with open(COMBINE_LIST_FILE, "r") as f:
            return json.load(f)
    else:
        return {}
def save_cookies(driver):
    with open(COOKIE_FILE, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver):
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

def add_overlap_to_divs(driver, container_element, style_modifications):
    div_elements = container_element.find_elements(By.TAG_NAME, "div")
    for div in div_elements:
        for property, value in style_modifications.items():
            driver.execute_script(
                f"arguments[0].style.{property} = '{value}';", div)
                
def add_hover_class_to_divs(driver, container_element):
    div_elements = container_element.find_elements(By.TAG_NAME, "div")
    for div in div_elements:
        driver.execute_script("arguments[0].classList.add('instance-hover');", div)

def add_class_to_element(driver, element, class_to_add):
    driver.execute_script("arguments[0].classList.add(arguments[1]);", element, class_to_add)

def sort_elements(driver):
    actions = ActionChains(driver)
    actions.release().perform()
    clear_b = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.sidebar > div.sidebar-controls > div.sidebar-sorting > div.sidebar-sort.sidebar-sorting-item')
    actions.click(clear_b).perform()
    
def clear_canvas(driver):
    actions = ActionChains(driver,duration=0)
    actions.release().perform()
    clear_b = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.side-controls > img.clear')
    clear_b.click()

def mute_canvas(driver):
    actions = ActionChains(driver)
    actions.release().perform()
    m_b = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.side-controls > img.sound')
    actions.click(m_b).perform()

def get_discovered_items(driver):
    container = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.sidebar > div.sidebar-inner > div')
    item_elements = container.find_elements(By.CLASS_NAME, "item")  # Adjust the class name if needed
    return item_elements

def combine_and_replace(driver, item1, item2):
    actions = ActionChains(driver)
    item1.click()
    time.sleep(0.2)
    item2.click()

    item2_instance = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div[2]") # Adjust the selector if needed
    item1_instance = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div[1]") # Adjust the selector if needed

    actions.drag_and_drop(item2_instance, item1_instance).perform()
    time.sleep(0.2)

def attempt_combination(driver, item_i, other_item_i):
    for _ in range(MAX_RETRIES):
        try:
            combine_and_replace2(driver, item_i, other_item_i)
            return  # Success, exit the retry loop
        except Exception as e:
            print(f"Combination failed, retrying")
            time.sleep(0.2)
            clear_canvas(driver) 
            time.sleep(0.3)  # Delay before retry

def combine_and_replace2(driver, item1_index, item2_index):
    actions = ActionChains(driver,duration=0)


    item1 = driver.find_element(By.CSS_SELECTOR, f"#__layout > div > div > div.sidebar > div.sidebar-inner > div > div:nth-child({item1_index}) > span")
    driver.execute_script("arguments[0].scrollIntoView(true);", item1)
    item1.click()


    item2 = driver.find_element(By.CSS_SELECTOR, f"#__layout > div > div > div.sidebar > div.sidebar-inner > div > div:nth-child({item2_index}) > span")
    driver.execute_script("arguments[0].scrollIntoView(true);", item2)
    item2.click()
    i_parent = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.instances > div')
    i_parent_childs = i_parent.find_elements(By.XPATH, "*")
    actions.drag_and_drop(i_parent_childs[-2], i_parent_childs[-1]).perform()

def iterate1(driver,combine_list):
    clear_canvas(driver)
    discovered_items = get_discovered_items(driver)
    for j, item in enumerate(discovered_items):


        if item.text in combine_list:
            d_i = get_discovered_items(driver)
            while len(d_i) > combine_list[item.text]:
                for i in range(combine_list[item.text], len(d_i)):
                    clear_canvas(driver)
                    attempt_combination(driver, j+1, i+1)
                combine_list[item.text] = len(d_i)
                save_combine_list(combine_list)
                d_i = get_discovered_items(driver)
                print(len(d_i))
        else:
            
            for i in range(j, len(discovered_items)):
                clear_canvas(driver)
                attempt_combination(driver, j+1, i+1)
            combine_list[item.text] = len(discovered_items)
            save_combine_list(combine_list)
        print(len(get_discovered_items(driver)))
    save_combine_list(combine_list)

def iterate2(driver,combine_list):
    clear_canvas(driver)
    discovered_items = get_discovered_items(driver)
    for j, item in enumerate(discovered_items):
        clear_canvas(driver)
        if item.text in combine_list:
            attempt_combination(driver, j+1, combine_list[item.text]+1)
            combine_list[item.text] += 1
        else:
            
            attempt_combination(driver, j+1, j+1)
            combine_list[item.text] = j+1
        if j % 100 == 0:
            save_combine_list(combine_list)
            print(len(get_discovered_items(driver)))

def iterate3(driver,combine_list):
    clear_canvas(driver)
    discovered_items = get_discovered_items(driver)
    for j, item in enumerate(discovered_items):
        clear_canvas(driver)
        if item.text in combine_list:
            for i in range(combine_list[item.text], len(discovered_items)):
                clear_canvas(driver)
                attempt_combination(driver, j+1, i+1)
            combine_list[item.text] = len(discovered_items)
        else:
            combine_list[item.text] = j
            for i in range(combine_list[item.text], len(discovered_items)):
                clear_canvas(driver)
                attempt_combination(driver, j+1, i+1)
            combine_list[item.text] = len(discovered_items)
        if j % 100 == 0:
            save_combine_list(combine_list)
            print(len(get_discovered_items(driver)))
            




if __name__ == "__main__":
    
    driver.get(url)
    time.sleep(3)
    # load_cookies(driver)
    # only when first time launch
    #time.sleep(3)
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button')))
    #element.click()
    #time.sleep(1)
    combine_list = load_combine_list()
    time.sleep(0.2)
    mute_canvas(driver)
    #time.sleep(0.2)
    #sort_elements(driver)
    while True:
        #iterate1(driver,combine_list)
        iterate3(driver,combine_list)


    driver.quit()
