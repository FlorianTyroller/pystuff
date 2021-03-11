import win32ui
from PIL import ImageGrab, Image, ImageDraw
import time
from tkinter import *
import cv2
import numpy as np
import pyautogui

window_name = "Overwatch" # use EnumerateWindow for a complete list
wd = win32ui.FindWindow(None, window_name)
dc = wd.GetWindowDC() # Get window handle
while True:
    j = dc.GetPixel (60,20)
    c = True
    #a+=1
    im = ImageGrab.grab(bbox=(xBound,yBound,xBound+qLen,yBound+qLen))
    print(im.size)
    pixels = [[im.getpixel((x, y)) for x in range(0, qLen, step)] for y in range(0, qLen, step)]
    for y in range(len(pixels)):
        if c:
            for x in range(len(pixels[y])):  
                if pixels[y][x][2] < 40 and pixels[y][x][1] < 40 and pixels[y][x][0] > 100:
                    #print(pixels[y][x])
                    #if a%100==0:
                    pyautogui.click()
                    c=False
                    break
        else:
            break
dc.DeleteDC()