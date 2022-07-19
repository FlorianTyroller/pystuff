# import all necessary modules
import sys
import os
import time
from PIL import Image, ImageGrab, ImageChops
import win32api, win32con
import keyboard


top_left = (670,380)
bottom_right = (980,710)

flip = True
maxy = 0
maxx = 0
miny = 9999
minx = 9999
t_end = time.time() + 60 * 1 # 1 minute from now
while True:
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
