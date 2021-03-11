from PIL import ImageGrab, Image, ImageDraw
import time
from tkinter import *
import cv2
import numpy as np
import pyautogui

start = (817,474)
pyautogui.click(start[0],start[1])
gap = 100
size = 4
l = [[(i,j) for i in range(size)] for j in range(size)]

visited = []

def getNeighbours(x,y,l):
    a = []
    for i in range(-1,2):
        for j in range(-1,2):
            if j != 0 or i != 0:
                nx = x+j
                ny = y+i
                if nx in range(size) and ny in range(size):
                    u = (nx,ny)
                    if u not in l:
                        a.append(u)
    return a

def getFields(x,y,iterations):
    global visited
    a = getNeighbours(x,y)
    r = []
    for i in a:
        u = getNeighbours(i[0],i[1],[i])
        r.append()
    



for i in range(size):
    for j in range(size): 
        x,y = l[i][j]
        #get next fields with steps
        fields = getFields(x,y,1)
        for f in fields:
            #move to starting square
            pyautogui.moveTo(start[0]+x*gap,start[1]+y*gap)
            for ff in f:
                pyautogui.dragTo(start[0]+ff[0]*gap, start[1]+ff[1]*gap, button='left',duration=0.2)

            
      
        
 