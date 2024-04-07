
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium_stealth import stealth

service = Service(
    executable_path='C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=service)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


url = "https://neal.fun/infinite-craft/"

if __name__ == "__main__":
    
    driver.get(url)
    # Print HTML
    print(driver.page_source)

    time.sleep(2)

    script = f"""
    fetch('https://neal.fun/api/infinite-craft/pair?first=Dust&second=Dust', {{
        method: 'GET'
    }})
    .then(response => {{
        if (response.status === 429) {{
            // Extract retry-after header (if present)
            const retryAfterSeconds = response.headers.get('Retry-After');
            window.__selenium_error__ = {{code: 429, retryAfter: retryAfterSeconds}};
        }} else {{
            window.__selenium_data__ = response.json();
        }}
    }});
    """
    driver.execute_script(script)
    time.sleep(0.15)
    # Wait for the data to be available
    try:
        result = WebDriverWait(driver, 10, poll_frequency=0.02).until(lambda driver: driver.execute_script("return window.__selenium_data__"))
        # print(f"after wait: {time.time() - start_time} seconds")
    except Exception as e:
        print("Timeout: Response data was not retrieved.", e)
    
    print(result)
    time.sleep(101)