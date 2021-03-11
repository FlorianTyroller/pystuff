
import pyautogui
import time


starttime = time.time()
while True:
    print("tick")
    time.sleep(5.0 - ((time.time() - starttime)
    im = pyautogui.screenshot()

    pix = im.getpixel((1670, 1055))
    su = pix[0]+pix[1]+pix[2]
    if(su != 75):
        pyautogui.click(1670, 1055)
    print(pix[0]+pix[1]+pix[2])