from PIL import ImageGrab, Image, ImageDraw
import time
from tkinter import *
import cv2
import numpy as np
import pyautogui
width=1920
height=1080
q=10
qLen = q*3
step = 1
xBound = width//2 - qLen//2
yBound = height//2 - qLen//2
b=0

def count(arr):
    c=0
    for i in arr:
        for j in i:
            if j[2] < 40 and j[1] < 40 and j[0] > 100:
                c+=1
    return c

def count1 (arr):
    return sum(arr)


while True:
    b+=1
    
    im = ImageGrab.grab(bbox=(xBound,yBound,xBound+qLen,yBound+qLen))
    pixels=[0,0,0,0,0,0,0,0,0]
    ind=0
    for u in range(3):
        for t in range(3):      
            for x in range(0, qLen//3, step):
                for y in range(0, qLen//3, step):
                    pp=im.getpixel((y+(t*q), x+(u*q)))
                    if pp[2] < 40 and pp[1] < 40 and pp[0] > 100:
                        pixels[ind]+=1

        ind+=1

    ind = pixels.index(max(pixels))
    if b % 10 == 0:
        print(ind)
        print(pixels[0],pixels[1],pixels[2])
        print(pixels[3],pixels[4],pixels[5])
        print(pixels[6],pixels[7],pixels[8])