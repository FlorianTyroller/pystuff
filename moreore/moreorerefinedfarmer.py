# import all necessary modules
import sys
import os
import time
from PIL import Image, ImageGrab, ImageChops
import win32api, win32con
import keyboard
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.6)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.6)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.6)

def exit_pop_up():
    exx = 1980 - 1920
    exy = 150
    click(exx,exy)

def escape_pop_up():
    time.sleep(0.5)
    keyboard.press_and_release('esc')
    time.sleep(0.8)


def check_boss(data, width, height):
    px = 2712 - width
    py = 970
    tries = 10
    for i in range(tries):
        # check if pixel is red
        if data[px, py][0] >= 130 and data[px, py][1] <= 28 and data[px, py][2] <= 28:
            return True
        else:
            # wait for 100 ms and check again
            time.sleep(0.1)
    return False

def kill_boss(w):
    px = 2712 - w
    py = 970
    top_left = (370,875)
    bottom_right = (1130,988)
    bx = 2755 - w
    by = 900
    bx -= top_left[0]
    by -= top_left[1]
    flip = True
    t_end = time.time() + 60 * 1 # 1 minute from now
    # click to start fight
    win32api.SetCursorPos((px,py))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    no_sword = 0
    while True:
        if keyboard.is_pressed('q'):
            break
        if no_sword > 20:
            break
        # make a screen shot of the screen with top left and bottom right cqqqoordinates
        screen_shot = ImageGrab.grab(bbox=(top_left[0],top_left[1],bottom_right[0],bottom_right[1]))
        data = screen_shot.load()
        width, height = screen_shot.size
        # check if boss alive
        if data[bx, by][0] <= 10 and data[bx, by][1] <= 10 and data[bx, by][2] <= 10:
            print("boss killed")
            break

        spac = 3
        attack = False
        for ox in range(width//spac):
            if attack:
                break
            for oy in range(height//spac):
                x = ox*spac
                y = oy*spac
                if data[x,y][0] >= 120 and data[x,y][1] >= 120 and data[x,y][2] <= 50:
                    cx = x + top_left[0]
                    cy = y + top_left[1]
                    win32api.SetCursorPos((cx-2,cy-2))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    attack = True
                    break
        no_sword += 1

def farm_combo(sec):
    top_left = (670,380)
    bottom_right = (980,710)

    flip = True
    t_end = time.time() + sec # 1 minute from now
    while True:
        if time.time() > t_end:
            break
        if keyboard.is_pressed('q'):
            break
        # make a screen shot of the screen with top left and bottom right coordinates
        screen_shot = ImageGrab.grab(bbox=(top_left[0],top_left[1],bottom_right[0],bottom_right[1]))
        # take another screen shot of the screen with top left and bottom right coordinates and compare it to the first screen shot
        screen_shot2 = ImageGrab.grab(bbox=(top_left[0],top_left[1],bottom_right[0],bottom_right[1]))

        # highlight the differences between the two screen shots
        diff = ImageChops.difference(screen_shot, screen_shot2)

        data = diff.load()

        widht, height = diff.size

        ds = []

        spac = 13

        for ox in range(widht//spac):
            for oy in range(height//spac):
                x = ox*spac
                y = oy*spac
                if data[x,y] != (0,0,0):
                    ds.append((x,y))

        # move mouse to each coordinate in the list
        if len(ds) > 50:
            continue
        if flip:
            ds = ds[::-1]
            flip = False
        else:
            flip = True
        d = 5
        spac2 = 4
        clicked = False
        ys = []
        for x,y in ds:
            if clicked:
                break
            if y in ys:
                continue
            ys.append(y)
            cx = top_left[0]+x
            cy = top_left[1]+y
            win32api.SetCursorPos((cx,cy))
            sc = ImageGrab.grab(bbox=(top_left[0]+x-d,top_left[1]+y-d,top_left[0]+x+d,top_left[1]+y+d))
            data2 = sc.load()
            widht, height = sc.size
            for ox in range(widht//spac2):
                if clicked:
                    break
                for oy in range(height//spac2):
                    x = ox*spac2
                    y = oy*spac2
                    # check if data2[x,y] is red
                    if data2[x,y][0] >= 100 and data2[x,y][1] <= 100 and data2[x,y][2] <= 100:
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        clicked = True
                        break
loopcount = 0

while True: # main loop
    loopcount += 1
    if keyboard.is_pressed('q'):
        break
    # make a screen shot of the entire screeen
    screen_shot = ImageGrab.grab()
    data = screen_shot.load()
    width, height = screen_shot.size

    # check if boss is there
    boss_found = check_boss(data,width,height)
    # if boss is there kill boss
    if boss_found:
        print("boss found")
        kill_boss(width)
        # click on boss defeated
        time.sleep(0.5)
        win32api.SetCursorPos((2712-width,970))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        win32api.SetCursorPos((2612-width,970))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        win32api.SetCursorPos((2812-width,970))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        # wait for a short amount of time
        time.sleep(1.5)
        # check if artifact found
        ax = 2600 - width
        ay = 888
        """
        if data[ax, ay][0] >= 140 and data[ax, ay][1] <= 25 and data[ax, ay][2] <= 25:
            print("artifact found")
            # trash artifact
            win32api.SetCursorPos((ax,ay))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(0.5)
        else: 
            print("artifact not found", str(data[ax, ay]))
            win32api.SetCursorPos((ax,ay))
            time.sleep(0.2)
        """
        # trash artifact
        win32api.SetCursorPos((ax,ay))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.5)
        # click on redo quest
        win32api.SetCursorPos((2860-width,715))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    # collect auto quester loot
    if loopcount % 9 == 0:
        time.sleep(0.5)
        aqx = 2090 - width
        aqy = 811
        win32api.SetCursorPos((aqx,aqy))
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.5)
        # click button 
        cbx = 2888 - width
        cby = 888
        win32api.SetCursorPos((cbx,cby))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)
        # exit
        exx = 1980 - width
        exy = 150
        win32api.SetCursorPos((exx,exy))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(1)
        continue

    # collect ad loot if possible
    if loopcount % 7 == 0:
        adx = 2000 - width
        ady = 740
        win32api.SetCursorPos((adx,ady))
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        # check if pop up is there
        time.sleep(1)
        popx = 2937 - width
        popy = 767
        screen_shot2 = ImageGrab.grab()
        data2 = screen_shot2.load()
        if data2[popx, popy][0] >= 180 and data2[popx, popy][1] >= 180 and data2[popx, popy][2] <= 90:
            print("ad available")
            # click on yes
            win32api.SetCursorPos((popx,popy))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            # wait until ad is over
            time.sleep(20)
            exit_pop_up()
            escape_pop_up()
            time.sleep(2)
            continue
    
    # incubate and hatch and merge pets
    if loopcount % 10 == 0:
        petx = 2222 - width
        pety = 822
        click(petx,pety)
        # press on incubator
        incx = 2700 - width
        incy = 256
        click(incx, incy)
        # press on hatch
        hatx = 2900 - width
        haty = 430 
        click(hatx, haty)
        # press on incubate all
        incax = 3200 - width
        incay = 490
        click(incax, incay)
        # press on pets
        petsx = 2500 - width
        petsy = 380
        click(petsx,petsy)
        # press on merge
        merx = 2738 - width
        mery = 461
        click(merx, mery)
        # close pop up
        exx = 1980 - width
        exy = 150
        click(exx,exy)
    farm_combo(10)
    


