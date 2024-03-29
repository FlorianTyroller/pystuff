from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()

chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\projects\\infinitecraft\\seleniumexploit")
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to open
url = "https://neal.fun/infinite-craft/"

if __name__ == "__main__":
    
    driver.get(url)
    time.sleep(999)