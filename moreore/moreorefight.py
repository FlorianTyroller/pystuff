# import all necessary modules
import sys
import os
import time
from PIL import Image, ImageGrab, ImageChops
import win32api, win32con
import keyboard


top_left = (360,895)
bottom_right = (1140,998)

flip = True
maxy = 0
maxx = 0
miny = 9999
minx = 9999
t_end = time.time() + 60 * 1 # 1 minute from now
while True:
    if keyboard.is_pressed('q'):
        break
    # make a screen shot of the screen with top left and bottom right cqqqoordinates
    screen_shot = ImageGrab.grab(bbox=(top_left[0],top_left[1],bottom_right[0],bottom_right[1]))
    data = screen_shot.load()
    widht, height = screen_shot.size

    spac = 3

    for ox in range(widht//spac):
        for oy in range(height//spac):
            x = ox*spac
            y = oy*spac
            if data[x,y][0] >= 120 and data[x,y][1] >= 120 and data[x,y][2] <= 50:
                cx = x + top_left[0]
                cy = y + top_left[1]
                win32api.SetCursorPos((cx-2,cy-2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                p = False
                if cx < minx:
                    minx = cx
                    p = True
                if cx > maxx:
                    maxx = cx
                    p = True
                if cy < miny:
                    miny = cy
                    p = True
                if cy > maxy:
                    maxy = cy
                    p = True
                if p:
                    print(minx,maxx,miny,maxy)
                break

    