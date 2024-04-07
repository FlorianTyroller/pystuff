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
chrome_options.add_argument(f'user-agent={ua.random}')
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
chrome_options.add_argument("user-data-dir=C:\\Users\\Flori\\Desktop\\pypy\\tools\\infinitecraft\\seleniumexploit3")
chrome_options.add_argument("start-maximized")  # Maximize the browser window
chrome_options.add_argument('--ignore-certificate-errors')
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



def send_request_through_browser(api_url, params):
    # Convert params to a JSON string
    params_json = json.dumps(params)
    script = f"""
    fetch('{api_url}', {{
        method: 'GET'
    }})
    .then(response => console.log(response)) 
    """
    driver.execute_script(script)



if __name__ == "__main__":
    
    driver.get(url)
    # Wait for manual input
    while True:
        input("Press Enter in the console to continue...") 

        # Send the request directly through Selenium
        api_url = "https://neal.fun/api/infinite-craft/pair?first=Aluminum%20Oxide&second=Alvin"
        params = {'first': 'Bigfoot', 'second': 'Puddle'}
        a = send_request_through_browser(api_url, params)
        print(a)

    