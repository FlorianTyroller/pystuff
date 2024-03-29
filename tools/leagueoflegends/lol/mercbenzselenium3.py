from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
import random
import time

# Define an empty dictionary to store questions and answers
qa_dict = {}

# Open the file and read questions and answers
with open('lol/qaa.txt', 'r') as file:
    lines = file.readlines()

# Process each line and populate the dictionary
for line in lines:
    # Split the line into question and answer using comma as separator
    try:
        question, answer = line.strip().split(',')
    except:
        print("error: ", line)
    # Store the question and answer in the dictionary
    qa_dict[question.strip()] = answer.strip()


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
    # while True:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#profile-box > div.button-container > button:nth-child(2)')))
    element.click()
    
    pattern = []
    t_pattern = -1
    pr = False
    sleep_time = 0.25
    while True:
        # Check the instruction text to determine the game phase
        sp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.inner > div.main-container > div > div > div.game-positioner > div > div.simon-box > div.instruction-text.bold > span')))
        instruction_text = sp.text

        if instruction_text == "Memorize the pattern":
            pr = False
            # Memorize the blinking pattern
            
            square_container = driver.find_element(By.CSS_SELECTOR, '#app > div.inner > div.main-container > div > div > div.game-positioner > div > div.simon-box > div.square-container')
            squares = square_container.find_elements(By.CLASS_NAME, 'simon-square')

            if len(pattern) <= 1:
                for i, square in enumerate(squares):
                    if 'blink' in square.get_attribute('class'):
                        pattern.append(i)

                # print(f"Memorized Pattern: {[square.text for square in pattern]}")
                time.sleep(0.3)  # Wait for a moment before the next phase
            else:
                for i, square in enumerate(squares):
                    if 'blink' in square.get_attribute('class'):
                        if t_pattern is not i:
                            t_pattern = i

                

        
        elif instruction_text == "Click the pattern!":
            if pr:
                continue
            if t_pattern >= 0:
                pattern.append(t_pattern)
            # print(pattern)
            # Repeat the memorized pattern
            a = sleep_time - 0.038 * (len(pattern)//7)
            squares = square_container.find_elements(By.CLASS_NAME, 'simon-square')
            for square in pattern:
                squares[square].click()
                if a > 0:
                    time.sleep(a)  # Wait between clicks

            # print("Pattern repeated")
            pr = True
            t_pattern = -1
            time.sleep(0.2)  # Wait for a moment before the next phase
        
        else:
            # print("Unknown game phase. Waiting for a moment.")
            time.sleep(0.2)  # Wait for a moment before checking the game phase again

    
    time.sleep(9999)





except Exception as e:
    print("An error occurred:", e)
    time.sleep(9999)
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




# container
# #app > div.inner > div.main-container > div > div > div.game-positioner > div > div.simon-box > div.square-container

# square
# #app > div.inner > div.main-container > div > div > div.game-positioner > div > div.simon-box > div.square-container > div:nth-child(1)

# disabled
# disabled="disabled"

# indicator
# #app > div.inner > div.main-container > div > div > div.game-positioner > div > div.simon-box > div.instruction-text.bold > span
# "Click the pattern!"
# "Memorize the pattern"

# blink
# class="simon-square"
# "simon-square blink"
