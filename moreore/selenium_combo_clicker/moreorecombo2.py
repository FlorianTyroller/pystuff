import time
import clipboard
import win32api, win32con
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
# import pickle
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import random as rnd


driver = webdriver.Chrome(executable_path = r"C:/Program Files/Google/Chrome Beta/Application/chromedriver.exe")
driver.get("https://syns.studio/more-ore/")
driver.implicitly_wait(0)

time.sleep(4)

save_file = "C:/Users/Flori/Desktop/pypy/moreore/selenium_combo_clicker/latest_save.txt"

def check_exists_by_CSS(css):
    try:
        driver.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True

# press close
def press_close():
    close_button = driver.find_element(By.CLASS_NAME,'close-btn')
    ActionChains(driver).click(close_button).perform()

def open_settings():
    settings_button = driver.find_element(By.CSS_SELECTOR, '[alt="settings button"]')
    ActionChains(driver).click(settings_button).perform()

def import_save():
    open_settings()
    time.sleep(0.5)
    import_save_button = driver.find_element(By.XPATH, '//button[normalize-space()="import save"]')
    ActionChains(driver).click(import_save_button).perform()
    
    # read latest save from file and save it to variable save
    with open(save_file, "r") as f:
        save = f.read()
    time.sleep(1)
    import_save_textfield = driver.find_element(By.CSS_SELECTOR, '[rows="8"]')
    ActionChains(driver).click(import_save_textfield).perform()
    time.sleep(0.4)
    driver.execute_script("arguments[0].value = arguments[1]", import_save_textfield, save)
    time.sleep(0.4)
    import_button = driver.find_element(By.XPATH, '//button[normalize-space()="Import Save"]')
    ActionChains(driver).click(import_button).perform()
    time.sleep(4)
    try:
        press_close()
    except:
        pass

def export_save():
    open_settings()
    time.sleep(0.5)
    export_save_button = driver.find_element(By.CSS_SELECTOR, "body > div.page-container > div.modal-wrapper > div > div.modal-content > div:nth-child(3) > div:nth-child(3) > button:nth-child(1)")
    ActionChains(driver).click(export_save_button).perform()
    time.sleep(0.3)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    press_close()
    # write clipboard to file
    with open(save_file, "w") as f:
        f.write(clipboard.paste())
    
    time.sleep(1)

def click_combo(repetitions):
    # combo clicker
    weak_spot = driver.find_element(By.CSS_SELECTOR,'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-top > div.game-container-left-top-middle > div.ore-wrapper > div.ore-sprite-wrapper > div > div')
    # clicking = ActionChains(driver).click(weak_spot)
    for i in range(repetitions):
        location = weak_spot.location
        size = weak_spot.size
        w, h = size['width'], size['height']
        # click on the center of the element
        x = location['x'] + w//2
        x += 5 + rnd.randint(-2,2)
        y = location['y'] + h//2
        y += 120 + rnd.randint(-2,2)
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.04)

def disable_combo_shield():
    shield_check_box = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-top > div.game-container-left-top-top > div > div.combo-sign-wrapper.visible > div.combo-sign > div > input[type=checkbox]')
    ActionChains(driver).click(shield_check_box).perform()
    time.sleep(0.2)

def equip_speed_gear():
    artifact_slot_id = "slot-5440-2574-1886-4425"
    # if element with class name "tab tab-hero false tab-selected" is present, then equip artifact
    if check_exists_by_CSS('[class="tab tab-hero false tab-selected"]'):
        print("hero selected")
        pass
    else:
        hero_tab = driver.find_element(By.CSS_SELECTOR, '[class="tab tab-hero false"]')
        print("hero not selected")
        ActionChains(driver).click(hero_tab).perform()
        time.sleep(2)

    
    # click on element with id artifact_slot_id
    artifact_slot = driver.find_element(By.ID, artifact_slot_id)
    ActionChains(driver).click(artifact_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip"]')
    ActionChains(driver).click(equip_button).perform()

    # equip speed pets
    pet_tab = driver.find_element(By.XPATH, '//div[normalize-space()="Pets"]')
    ActionChains(driver).click(pet_tab).perform()
    time.sleep(0.5)
    # speed pet 1
    speed_pet_slot = driver.find_element(By.CSS_SELECTOR, '[id="pet-slot-1"]') 
    ActionChains(driver).click(speed_pet_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip to Slot 1"]')
    ActionChains(driver).click(equip_button).perform()
    time.sleep(0.2)
    # speed pet 2
    speed_pet_slot = driver.find_element(By.CSS_SELECTOR, '[id="pet-slot-2"]')
    ActionChains(driver).click(speed_pet_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip to Slot 2"]')
    ActionChains(driver).click(equip_button).perform()
    time.sleep(0.2)
    # press escape
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.2)

def equip_combat_gear():
    artifact_slot_id = "slot-5440-2574-1886-4425"
    # if element with class name "tab tab-hero false tab-selected" is present, then equip artifact
    if check_exists_by_CSS('[class="tab tab-hero false tab-selected"]'):
        print("hero selected")
        pass
    else:
        hero_tab = driver.find_element(By.CSS_SELECTOR, '[class="tab tab-hero false"]')
        print("hero not selected")
        ActionChains(driver).click(hero_tab).perform()
        time.sleep(2)

    
    # click on element with id artifact_slot_id
    artifact_slot = driver.find_element(By.ID, artifact_slot_id)
    ActionChains(driver).click(artifact_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip"]')
    ActionChains(driver).click(equip_button).perform()

    # equip hp pets
    pet_tab = driver.find_element(By.XPATH, '//div[normalize-space()="Pets"]')
    ActionChains(driver).click(pet_tab).perform()
    time.sleep(0.5)
    # hp pet 1
    hp_pet_slot = driver.find_element(By.CSS_SELECTOR, '[id="pet-slot-14"]') 
    ActionChains(driver).click(hp_pet_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip to Slot 1"]')
    ActionChains(driver).click(equip_button).perform()
    time.sleep(0.2)
    # hp pet 2
    hp_pet_slot = driver.find_element(By.CSS_SELECTOR, '[id="pet-slot-15"]')
    ActionChains(driver).click(hp_pet_slot).perform()
    time.sleep(0.2)
    equip_button = driver.find_element(By.XPATH, '//div[normalize-space()="Equip to Slot 2"]')
    ActionChains(driver).click(equip_button).perform()
    time.sleep(0.2)
    # press escape
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.2)

def kill_boss():
    # find element with class name "boss-approaching"
    boss_approaching = driver.find_element(By.CLASS_NAME, 'boss-approaching')
    # click on it
    ActionChains(driver).click(boss_approaching).perform()
    time.sleep(0.2)
    # click on class quest-skill quest-skill-ravenousStrikes
    ravenous_strikes = driver.find_element(By.CSS_SELECTOR, '[class="quest-skill quest-skill-ravenousStrikes"]')
    ActionChains(driver).click(ravenous_strikes).perform()
    time.sleep(0.2)
    manual_attack = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-bottom > div.boss-fight-container > div.manual-attacks-container > img');
    hp_value = driver.find_element(By.CSS_SELECTOR,"body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-bottom > div.boss-fight-container > div.bars-container > div.hero-bars-container > div.hp-bar-container > p");
    boss_hp_value = driver.find_element(By.CSS_SELECTOR,"body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-bottom > div.boss-fight-container > div.bars-container > div.boss-bars-container > div.hp-bar-container > p");
    # boss loop
    loop_counter = 0
    heal_available = True
    while True:
        loop_counter += 1
        if loop_counter % 10 == 0:
            hp, maxhp = hp_value.text.replace("K", "").replace(" ","").split("/")
            bosshp = boss_hp_value.text.replace("B", "").replace("M", "").replace("K", "").replace(" ","").split("/")[0]
            #print("hp: " + hp + " maxhp: " + maxhp)
            hp,maxhp,bosshp = float(hp),float(maxhp),float(bosshp)
            if heal_available and hp/maxhp < 0.23:
                print("hp is low, heal")
                heal = driver.find_element(By.CSS_SELECTOR, '[class="quest-skill quest-skill-heal"]')
                ActionChains(driver).click(heal).perform()
                heal_available = False

        
            if hp <= 0.1:
                print("quest failed")
                break
            if bosshp <= 0.1:
                print("boss killed")
                break
        # click on img with class manual-attack
        try:
            location = manual_attack.location
            size = manual_attack.size
            w, h = size['width'], size['height']
            # click on the center of the element
            x = location['x'] + w//2
            x += 5 + rnd.randint(-2,2)
            y = location['y'] + h//2
            y += 120 + rnd.randint(-2,2)
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        except:
            print("boss killed")
            break
        time.sleep(0.01)

def manage_loot():
    # get quest success element
    # check if element exists
    # if yes, click on it
    # if no, skip this step
    if check_exists_by_CSS('body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-bottom > div.quest-banner-container > h1'):
        quest_success = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-bottom > div.quest-banner-container > h1')
        location = quest_success.location
        size = quest_success.size
        w, h = size['width'], size['height']
        # click on the center of the element
        for i in range(3):
            x = location['x'] + w//2
            x += 5 + rnd.randint(-2,2) + (i-1) * 20
            y = location['y'] + h//2
            y += 120 + rnd.randint(-2,2)
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.2)
    

    # get loot container
    pause_on_loot = False
    pause_on_mythic = True
    if pause_on_loot:
        while True:
            if keyboard.is_pressed('m'):
                break
            time.sleep(0.1)
    elif pause_on_mythic:
        mythic = False
        loot_container = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.modal-wrapper > div > div.modal-content > div > div.equips-found-container')
        # iterate over every element in loot container
        
        for loot in loot_container.find_elements(By.CSS_SELECTOR, 'div'):
            # check if element is a div and class name contains mythic
            if loot.tag_name == "div" and "mythic" in loot.get_attribute("class"):
                # wait until the key m is pressed
                mythic = True
                break
        if mythic:
            print("mythic found")
            while True:
                if keyboard.is_pressed('m'):
                    break
                time.sleep(0.1)
                
        else:
            print("mythic not found")
    
    

    time.sleep(1)
    
    # click on redo quest button
    redo_quest = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.modal-wrapper > div > div.modal-actions > button:nth-child(1)')
    ActionChains(driver).click(redo_quest).perform()
    time.sleep(0.2)

def watch_ad():
    # get element of class reward-ad-container active
    ad_container = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-top > div.reward-ad-container.active')
    # click on it
    ActionChains(driver).click(ad_container).perform()
    time.sleep(0.3)
    # get heck yeah button
    heck_yeah = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.modal-wrapper > div > div.modal-actions > button:nth-child(2)')
    # click on it
    ActionChains(driver).click(heck_yeah).perform()
    time.sleep(22)
    win32api.SetCursorPos((150,150))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)
    # press escape
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.2)
    
def manage_pets():
    # get element
    pet_tab = driver.find_element(By.XPATH, '//div[normalize-space()="Pets"]')    # click on it
    ActionChains(driver).click(pet_tab).perform()
    time.sleep(0.4)
    incubator_tab = driver.find_element(By.XPATH, '//div[normalize-space()="Incubator"]') 
    ActionChains(driver).click(incubator_tab).perform()
    time.sleep(0.4)
    hatch_all_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > div.pets-modal-tab-content.incubator-tab-content-container > div.incubators-wrapper > div.section-header > div.hatch-all-btn')
    ActionChains(driver).click(hatch_all_btn).perform()
    time.sleep(0.4)
    if check_exists_by_CSS("body > div.page-container > div.game-container > div.modal-wrapper > div > div.pets-modal-tab-content.incubator-tab-content-container > div.eggs-wrapper > div > button"):
        hatch_all_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > div.pets-modal-tab-content.incubator-tab-content-container > div.eggs-wrapper > div > button')
        ActionChains(driver).click(hatch_all_btn).perform()
        time.sleep(0.4)
    pets_inner_tab = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > div.pets-modal-tabs-container > div.pets-modal-tab.pets-modal-overview-tab')
    # click on it
    ActionChains(driver).click(pets_inner_tab).perform()
    time.sleep(0.4)
    auto_merge_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > div.pets-modal-tab-content.overview-tab-content-container > div.all-pets-wrapper.box-shadowed > h3 > span.auto-merge-btn')
    ActionChains(driver).click(auto_merge_btn).perform()
    time.sleep(0.4)
    # press escape
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.4)

def auto_quester():
    # get element
    quester_tab = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.game-container-left > div.game-container-left-top > div.game-container-left-top-bottom > div.bottom-buttons-container > div.left > div.left-bottom-btn.quest-btn')    # click on it
    ActionChains(driver).click(quester_tab).perform()
    time.sleep(0.4)

    # get quest button
    quest_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > div > button')
    # click on it
    ActionChains(driver).click(quest_btn).perform()
    time.sleep(0.4)

    # get collect all button
    collect_all_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.page-container > div.game-container > div.modal-wrapper > div > button')
    # click on it
    ActionChains(driver).click(collect_all_btn).perform()
    time.sleep(0.4)

    # press escape
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.4)


# import save
press_close()
time.sleep(1)
import_save()
# export_save()
# main loop
auto_time = pets_time = export_time = time.time()
time.sleep(1)

disable_combo_shield()

while True:
    try:
        # if key g is pressed pause the script
        if keyboard.is_pressed('g'):
            print("paused")
            while True:
                if keyboard.is_pressed('u'):
                    break
                time.sleep(0.1)
            print("resumed")
        # if key b is pressed, break
        if keyboard.is_pressed('b'):
            # thrwo interrupt exception to break out of main loop
            raise KeyboardInterrupt
        # ever 20 minutes export save
        if time.time() - export_time > 1200:
            export_time = time.time()
            export_save()
        # check if boss is there
        if check_exists_by_CSS('[class="boss-approaching"]'):
            # kill boss
            equip_combat_gear()
            kill_boss()
            manage_loot()
            equip_speed_gear()
        if check_exists_by_CSS('[class="reward-ad-container active"]'):
            watch_ad()
        # every five minutes check if pet is available
        if time.time() - pets_time > 300 :
            pets_time = time.time()
            manage_pets()
        # every six minutes check autoquester
        if time.time() - auto_time > 360:
            auto_time = time.time()
            auto_quester()
        click_combo(15)
    except KeyboardInterrupt:
        print("b")
        export_save()
        break