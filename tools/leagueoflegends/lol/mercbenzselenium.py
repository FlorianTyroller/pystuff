from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
import random
import time
import re



service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=chrome_options)



# URL to open
url = "https://join.stagecast.io/?code=2590"

try:

    # Open the website
    driver.get(url)
    
    # wait
    time.sleep(3)
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "stagecast-loyalty-program")))
    time.sleep(0.5)
    # insert email
    print("inside 2nd iframe")
    input_field = driver.find_element(By.CSS_SELECTOR, '#sc-signup-form > div > input')
    input_field.send_keys('flori-spam@web.de')
    print("inserted")
    time.sleep(0.5)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sc-signup-form > label > span.mc-checkmark')))
    element.click()
    time.sleep(2)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div.popup > div.popup-container > div > div.popup-content > div > div.box-footer > div:nth-child(2) > button.sc-btn.main-button')))
    element.click()
    code = input("enter code: ")
    input_field = driver.find_element(By.CSS_SELECTOR, '#app > div > div.popup > div.popup-container > div > div.popup-content > div > div.box-body.pt-0.text-center > div.additional-content.mt-6 > div:nth-child(2) > div:nth-child(1) > input')
    input_field.send_keys(code)
    time.sleep(0.5)
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))
    print("inside 2 22 2 2 22  2")
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.inner > div.help-section > span.cta-box > div > div.popup-container > div > div.popup-header > button')))
    element.click()
    print("öwfledkjösladfkjöasdflkj")
    time.sleep(1.5)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.inner > div.help-section > span.help-button-container > div > div.popup-container > div > div.popup-content > div > div.start-bottom-overlay > div > label > span.mc-checkmark')))
    element.click()
    time.sleep(3)
    """element = driver.find_element(By.CSS_SELECTOR, '#app > div.inner > div.help-section > span.help-button-container > div > div.popup-container > div > div.popup-content > div > div.start-bottom-overlay > button')
    element.click()"""
    time.sleep(1.5)
    # start der loop
    max_g = 5
    h_score = 0
    while True:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#profile-box > div.button-container > button:nth-child(2)')))
        element.click()
        
        
        try:
            g_count = 0
            while True:
                whack_a_mole_container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#whack-a-mole-box > div.mole-container")))
                g_button = whack_a_mole_container.find_elements(By.CSS_SELECTOR, 'div.mole-container button.mole.shown.golden')
                if len(g_button) > 0:
                    #print(g_count)
                    if g_count < max_g:
                        g_button[0].click()
                        g_count += 1
                else:
                    g_count = 0
                buttons = whack_a_mole_container.find_elements(By.CSS_SELECTOR, 'div.mole-container button.mole.shown:not(.golden)')
                for button in buttons:
                    button.click()
        except:
            pass
            # print("end try")

        # press x button 
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.inner > div.help-section > span.cta-popup-container > div > div.popup-container > div > div.popup-header > button')))
        element.click()
        element = driver.find_element(By.CSS_SELECTOR, '#profile-box > div.bg-grey.border-top-radius > div:nth-child(2) > span.right-info')
        text = element.text
        cleaned_text = text.replace(" ", "").replace(".", "").replace("p", "")
        integer_part = int(cleaned_text)
        print("score:", integer_part, "highscore:" , h_score, "max_g:", max_g)
        if integer_part > h_score:
            h_score = integer_part
        else: 
            max_g += 1
        time.sleep(1)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the browser window
    driver.quit()

"""
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '')))
element.click()
"""



# Function to check the existence of an element by CSS selector
def check_exists_by_CSS(css):
    try:
        driver.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True

# Function to check the existence of an element by CSS selector
def check_exists_by_XPATH(xpa):
    try:
        driver.find_element(By.XPATH, xpa)
    except NoSuchElementException:
        return False
    return True

