import random
import string
import base64
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from multiprocessing import Process, freeze_support

# Function to initialize the WebDriver
def init_driver():
    webdriver_log = logging.getLogger('webdriver')
    webdriver_log.setLevel(logging.ERROR)
    service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    # chrome_options.add_argument("user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\tools\\infinitecraft\\seleniumexploitdb")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to generate random base64 string
def generate_random_base64(length):
    characters = string.ascii_letters + string.digits + '+/'
    random_string = ''.join(random.choices(characters, k=length))
    return base64.b64encode(random_string.encode()).decode()

# Function to handle each instance of the headless browser
def run_headless_browser():
    driver = init_driver()
    while True:
        random_base64 = generate_random_base64(7)[:7]
        url = "https://imgur.com/" + random_base64
        driver.get(url)
        wait_time = 0.3
        try:
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, "image-placeholder"))
            )
            print("Page loaded successfully!")
            print(url)
            with open("projects/imgforce/loaded_urls.txt", "a") as file:
                file.write(url + "\n")  # Write the URL to the file
            continue
        except:
            continue
            # print("Page did not load successfully. Trying another link...")
    driver.quit()

if __name__ == '__main__':
    freeze_support()

    # Number of parallel instances to run
    num_instances = 1

    # Create and start processes for each instance
    processes = []
    for _ in range(num_instances):
        process = Process(target=run_headless_browser)
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
