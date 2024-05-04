from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
import time
from selenium_stealth import stealth
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import json

service = Service(executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
# Set up ChromeOptions
chrome_options = webdriver.ChromeOptions()
#chrome_options = uc.ChromeOptions()
#user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"  # Example User-Agent string
ua = UserAgent()
proxy_server_url = "185.28.193.95"
chrome_options.add_argument(f'user-agent={ua.random}')
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\tools\\infinitecraft\\seleniumexploit3")
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument(f'--proxy-server={proxy_server_url}')
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

# URL to open
url = "https://neal.fun/infinite-craft/"





if __name__ == "__main__":
    
    driver.get(url)
    time.sleep(100)
    