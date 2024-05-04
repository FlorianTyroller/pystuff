import cv2
import numpy as np
import os
import pyautogui
import time

# COORDINATES
SOUP_LOCATION = (850, 520)
FISH_LOCATION = (850, 620)
EGG_LOCATION = (850, 720)
ALG_LOCATION = (850, 820)

RICE_1_LOCATION = (1370, 640)
RICE_2_LOCATION = (1370, 740)

RICE_1_STATUS = (1345, 678)
RICE_2_STATUS = (1337, 779)

SOUP_STATUS = (900, 560)


# SCREENSHOT COORDINATES


# Define the cropping coordinates
# 
ORDERS_LOCATION = [881, 316, 1356, 359]


def main():
    # Load the images to find
    

    image_folder = "tools/shefshowdown/assets/sushi/"
    images_to_find = [image_file for image_file in os.listdir(image_folder) if image_file.endswith(".png")]


    while True:
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Crop the screenshot to the specified coordinates
        orders_rgb = screenshot[ORDERS_LOCATION[1]:ORDERS_LOCATION[3], ORDERS_LOCATION[0]:ORDERS_LOCATION[2]]

        #img_rgb = cv2.imread("tools/shefshowdown/assets/screenshot.png")


        orders = []
        for image in images_to_find:

            template = cv2.imread(image_folder + image)
            w, h = template.shape[:-1]

            res = cv2.matchTemplate(orders_rgb, template, cv2.TM_CCOEFF_NORMED)
            threshold = .8
            loc = np.where(res >= threshold)
            lastxs = set()
            for pt in zip(*loc[::-1]):  # Switch columns and rows
                newx, newy = pt[0] + ORDERS_LOCATION[0], pt[1] + ORDERS_LOCATION[1]
                if newx // 100 not in lastxs:
                    lastxs.add(newx // 100)
                    orders.append((image, newx, newy))
        print(orders)

        for order in orders:
            handleOrder(order, screenshot)

def handleOrder(order, screenshot):
    image, x, y = order
    if image == "soup.png":
        if soupReady(screenshot):
            collectSoup()
            click((x,y))
    elif image == "rice.png":
        rc = getRiceContainer(screenshot)
        if rc > 0:
            collectRice(rc)
            click((x,y))

    elif image == "riceegg.png":
        rc = getRiceContainer(screenshot)
        if rc > 0:
            collectRice(rc)
            collectEgg()
            collectAlg()
            click((x,y), sleep=1.2)
    elif image == "ricefish.png":
        rc = getRiceContainer(screenshot)
        if rc > 0:
            collectRice(rc)
            collectFish()
            click((x,y))
    elif image == "whatever.png":
        if soupReady(screenshot):
            collectSoup()
            click((x,y))
        else:
            rc = getRiceContainer(screenshot)
            if rc > 0:
                collectRice(rc)
                click((x,y))
            else:
                return

    


def collectAlg():
    click(ALG_LOCATION)



def collectFish():
    click(FISH_LOCATION)


def collectEgg():
    click(EGG_LOCATION)


def collectRice(j):
    if j == 1:
        click(RICE_1_LOCATION)
        click(RICE_1_LOCATION, iterations=2, sleep=0.1 )
        
    elif j == 2:
        click(RICE_2_LOCATION)
        click(RICE_2_LOCATION, iterations=2, sleep=0.1 )


def collectSoup():
    click(SOUP_LOCATION)


def soupReady(sc):
    p_color = sc[SOUP_STATUS[1], SOUP_STATUS[0]]
    print("soup status:", p_color)
    # check if white
    if p_color[2] < 90 and p_color[1] > 110 and p_color[0] > 170:
        return True
    return False

def getRiceStatus(sc, x, y):
    p_color = sc[y,x]
    print("rce status:", p_color)
    if p_color[2] < 170 and p_color[1] > 180 and p_color[0]> 50:
        return True
    return False
    
def getRiceContainer(sc):
    if getRiceStatus(sc, RICE_1_STATUS[0], RICE_1_STATUS[1]):
        return 1
    elif getRiceStatus(sc, RICE_2_STATUS[0], RICE_2_STATUS[1]):
        return 2
    else:
        return 0

def click(l, pause = False, duration = 0.01, sleep = 1, iterations = 15):
    for i in range(iterations):
        pyautogui.click((l[0],l[1]), _pause=pause, duration=duration)
    time.sleep(sleep)

if __name__ == "__main__":
    main()