import os
import pygame
import time
import math
import win32ui
from PIL import ImageGrab, Image, ImageDraw
from tkinter import *
import cv2
import numpy as np
import pyautogui
import win32gui


#long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_PLUS,
    K_MINUS,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def getHandle():
    thelist = []
    def findit(hwnd,ctx):
        if win32gui.GetWindowText(hwnd) == "Blizzard Battle.net": # check the title
            thelist.append(hwnd)

    win32gui.EnumWindows(findit,None)
    return thelist



pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400,400

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

radius = int((min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2) * 0.9)
zoom = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():

  

    run = True

    #window_name = "Snipping Tool" # use EnumerateWindow for a complete list
    #wd = win32ui.FindWindow(None, window_name).GetWindowDC()
    #print(wd)
    #dc = wd.GetWindowDC() # Get windo
    #i_desktop_window_id = wd
    i_desktop_window_dc = win32gui.GetWindowDC(getHandle()[0])
    print(i_desktop_window_dc)
    #pixels = [[im.getpixel((x, y)) for x in range(0, qLen, step)] for y in range(0, qLen, step)]

    while run:
        #im = ImageGrab.grab(bbox=(0,0,SCREEN_WIDTH//zoom,SCREEN_HEIGHT//zoom))
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                e = event.key 
                if e == K_ESCAPE:
                    run = False
                
             
            elif event.type == pygame.QUIT:

                run = False
    
        textsurface1 = myfont.render("zoom: " + str(zoom), False, (0, 0, 0))
        
        for y in range(SCREEN_HEIGHT//zoom):
            for x in range(SCREEN_WIDTH//zoom):
                color = win32gui.GetPixel(i_desktop_window_dc, x, y)
                #print(color)
                #pygame.draw.rect(screen,color,(x*zoom,y*zoom,zoom,zoom))

        pygame.display.flip()

    pygame.quit()
    #dc.DeleteDC()

if __name__ == '__main__':
    
    main()
