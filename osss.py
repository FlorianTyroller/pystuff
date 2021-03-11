from PIL import ImageGrab, Image, ImageDraw
import time
from tkinter import *
import cv2
import numpy as np
import pyautogui
import win32ui
import win32gui


read = 915
a1 = 520
a2 = 660
a3 = 700
a4 = 840
ax = [a1,a2,a3,a4]
def rgbint2rgbtuple(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)


window_name = "osu!"  # use EnumerateWindow for a complete list
wd = win32gui.FindWindow(None, window_name)
dc = wd.GetWindowDC()  # Get window handle

try:
    while True:
        try:
            for a in ax:
                p = rgbint2rgbtuple(dc.GetPixel(a, read))
                if pixels[0] > 200 and pixels[1] > 200 and pixels[2] > 200:
                    print(p)
        except:
            pass

except KeyboardInterrupt:
    win32gui.ReleaseDC(wd, dc)
    exit()

