from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import time
url = "https://lolalytics.com/lol/tierlist/"

champs = dict()
rankings = []

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the page to load (you may need to adjust the waiting time)
driver.implicitly_wait(10)

# Get the HTML content after JavaScript has loaded
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the container div for champions
champions_container = soup.select_one("#root > div:nth-child(6) > div > div")

# Check if champions_container is found
if champions_container:
    # Iterate over each champion div
    for champion_div in champions_container.find_all("div", class_="ListRow_name__b5btO"):
        # Extract champion name and link
        champion_name = champion_div.find("a").text
        champion_link = champion_div.find("a")["href"]

        # Store the data in the dictionary
        champs[champion_name] = champion_link
else:
    print("Champions container not found.")

# Iterate over the champions and roles
for champion_name, champion_link in champs.items():
    print(f"Champion: {champion_name}")
    c_url = "https://lolalytics.com" + champion_link

    # click on the 5 roles 
    lanes = ["#root > div.NavBar_navbar__08b77 > div > div > div.NavBar_left__CPTXU > div.LanePicker_wrapper__5qZwP > div > a:nth-child(1)", 
            "#root > div.NavBar_navbar__08b77 > div > div > div.NavBar_left__CPTXU > div.LanePicker_wrapper__5qZwP > div > a:nth-child(2)",
            "#root > div.NavBar_navbar__08b77 > div > div > div.NavBar_left__CPTXU > div.LanePicker_wrapper__5qZwP > div > a:nth-child(3)",
            "#root > div.NavBar_navbar__08b77 > div > div > div.NavBar_left__CPTXU > div.LanePicker_wrapper__5qZwP > div > a:nth-child(4)",
            "#root > div.NavBar_navbar__08b77 > div > div > div.NavBar_left__CPTXU > div.LanePicker_wrapper__5qZwP > div > a:nth-child(5)"]

    l_names = ["top", "jgl", "mid", "bot", "sup"]

    c_driver = webdriver.Chrome()
    c_driver.get(c_url)
    c_driver.implicitly_wait(10)

    for u, lane in enumerate(lanes):
        # Click on the lane link
        element = WebDriverWait(c_driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, lane)))
        element.click()

       #  ranking_container = WebDriverWait(c_driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.Wrapper_small__CiAB2 > div.ChampionSideBar_double__guKw8 > div:nth-child(2) > div.Stats_champstats__9o3Fa")))
        # time.sleep(5)
        # Iterate over the divs in the ranking container
        for i in range(2,15):
            
            t_1 = WebDriverWait(c_driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.Wrapper_small__CiAB2 > div.ChampionSideBar_double__guKw8 > div:nth-child(2) > div.Stats_champstats__9o3Fa > div:nth-child("+str(i)+") > div:nth-child(1)")))
            t_1_div = t_1.text

            t_2 = WebDriverWait(c_driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.Wrapper_small__CiAB2 > div.ChampionSideBar_double__guKw8 > div:nth-child(2) > div.Stats_champstats__9o3Fa > div:nth-child("+str(i)+") > div:nth-child(2) > div:nth-child(1)")))
            t_2_div = t_2.text

            t_3 = WebDriverWait(c_driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.Wrapper_small__CiAB2 > div.ChampionSideBar_double__guKw8 > div:nth-child(2) > div.Stats_champstats__9o3Fa > div:nth-child("+str(i)+") > div:nth-child(3)")))
            t_3_div = t_3.text
   
            if "?" in t_3_div:
                print(l_names[u], "is not suitable for", champion_name)
                break
            rankings.append([champion_name, l_names[u], t_1_div, t_2_div, t_3_div])

            # Print or use the extracted text as needed
            

            print(rankings[-1])

f_path = "rankings.txt"
with open(f_path, "w") as file:
    # Iterate over the list and write each item to a new line
    for item in rankings:
        file.write(f"{item}\n")