import pyautogui
import time
from PIL import Image
from threading import Thread

x1, y1 = 2303-1920, 854
x2, y2 = 2886-1920, 855
width = x2-x1
w4 = width//4
k_to_kb = {1: 'a', 2: 's', 3: 'l', 4: 'ö'}
im = None

def get_image():
    im = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    return im

def check_key(k):
    global im
    xc = w4*(k-1) + w4//2
    pressed = False
    while True:
        # time.sleep(0.11)
        if not im:
            continue
        color = im.getpixel((xc, 0))
        # print(color)
        if color[0] >= 200 and color[1] >= 200 and color[2] >= 200:
            # print(k, color)
            # hold key
            if not pressed:
                pyautogui.keyDown(k_to_kb[k])
                pressed = True
        else:
            if pressed:
                pyautogui.keyUp(k_to_kb[k])
                pressed = False
            
            

    
def main():
    global im
    im = get_image()


    for k in range(1, 5):
        Thread(target=check_key, args=(k,)).start()
    

    while True:
        print('new image')
        im = get_image()
        

if __name__ == '__main__':
    main()

        


