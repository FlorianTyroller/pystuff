from PIL import ImageGrab, Image, ImageDraw
import time
from tkinter import *
import cv2
import numpy as np
import pyautogui
import win32ui
import win32gui


def rgbint2rgbtuple(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)


window_name = "Overwatch"  # use EnumerateWindow for a complete list
wd = win32ui.FindWindow(None, window_name)
dc = wd.GetWindowDC()  # Get window handle

try:
    while True:

        sq = wd.GetWindowRect()
        x = (sq[2]-sq[0])//2
        y = (sq[3]-sq[1])//2
        pixels = rgbint2rgbtuple(dc.GetPixel(x, y))
        #print(pixels)
        if pixels[0] < 40 and pixels[1] < 40 and pixels[2] > 100:
            pyautogui.click()


except KeyboardInterrupt:
    win32gui.ReleaseDC(wd, dc)
    exit()

