import os
import pygame
import time
import math
import random
import timeit
from typing import List

import numpy as np

cum_max = np.maximum.accumulate

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
pygame.font.init() 


# Initialize pygame
pygame.init()


width = 200
maxHeight = 100

grid = [[0 for i in range(maxHeight)] for j in range(width)]

a = []

scale = 5

SCREEN_WIDTH, SCREEN_HEIGHT = width*scale,maxHeight*scale

myfont = pygame.font.SysFont("Times New Roman",(SCREEN_WIDTH)//40)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def generate_grid(g):

    g = [[0 for i in range(maxHeight)] for j in range(width)]
    g = fill_grid(g)
    return g

def fill_grid(g):
    global a
    a = []
    for i in range(width):
        a.append(random.randint(0,maxHeight))
    a = np.array(a)

    for i in range(width):
        for j in range(maxHeight):
            if maxHeight - j <= a[i]:
                g[i][j] = 1

    return g



def water_grid(g):
    for i in range(width):
        for j in range(maxHeight):
            if g[i][j] == 0:
                x = i
                left = False
                right = False
                #left
                x -= 1
                while x >= 0:
                    if g[x][j] == 1:
                        left = True
                    x -= 1
                #right
                x = i
                x += 1
                while x < width :
                    if g[x][j] == 1:
                        right = True
                    x += 1
                if left and right:
                    g[i][j] = 2

    return g

def getWaterCount():
    s = [0 for i in range(width)]
    su = 0
    for i in a:
        for j in range(i):
            if s[j] > 0:
                su += s[j]-1
            s[j] = 1
        for k in range(i,maxHeight):
            if s[k] != 0:
                s[k]+=1
    return su

def getWaterCount5():
    s = np.array([0 for i in range(width)])
    su = 0
    for i in np.nditer(a):
        for j in np.arange(stop = i):
            if s[j] > 0:
                su += s[j]-1
            s[j] = 1
        for k in np.arange(start = i,stop = maxHeight):
            if s[k] != 0:
                s[k]+=1
    return su

def getWaterCount2():
    global grid
    s = 0
    for i in range(width):
        for j in range(maxHeight):
            if grid[i][j] == 0:
                x = i
                left = False
                right = False
                #left
                x -= 1
                while x >= 0:
                    if grid[x][j] == 1:
                        left = True
                    x -= 1
                #right
                x = i
                x += 1
                while x < width :
                    if grid[x][j] == 1:
                        right = True
                    x += 1
                if left and right:
                    s += 1
    return s
    
def getWaterCount3():
    global a
    b = np.array(a)
    m_idx = np.argmax(b)
    return int(np.sum(cum_max(b[:m_idx]) - b[:m_idx], dtype=np.int64) + \
                np.sum(cum_max(b[:m_idx:-1]) - b[:m_idx:-1], dtype=np.int64))

def getWaterCount4(g = grid):
    s = 0
    for i in range(width):
        for j in range(maxHeight):
            if grid[i][j] == 2:
                s += 1
    return s



def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("scale: " + str(round(scale,1)), False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))



    #draw grid
    for i in range(maxHeight):
        pygame.draw.line(screen, (0,0,0), (0,i*scale), (SCREEN_WIDTH,i*scale), 1)

    for i in range(width):
        pygame.draw.line(screen, (0,0,0), (i*scale,0), (i*scale,SCREEN_HEIGHT), 1)

    #draw fields
    for i in range(width):
        for j in range(maxHeight):
            if grid[i][j] == 1:
                pygame.draw.rect(screen,(0,0,0),(i*scale,j*scale,scale,scale))
            elif grid[i][j] == 0:
                None
            elif grid[i][j] == 2:
                pygame.draw.rect(screen,(0,0,200),(i*scale,j*scale,scale,scale))



    



    pygame.display.flip()

def main():

    global grid
    global a
    run = True
    update()
    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_DOWN:
                    grid = water_grid(grid)
                elif e == K_UP:
                    grid = generate_grid(grid)
                elif e == K_RIGHT:
                    #print("get count 1: ", getWaterCount())
                    #print("get count 2: ", getWaterCount2())
                    #print("get count 1: ", timeit.timeit(getWaterCount,number = 1),getWaterCount())
                    print("get count 5: ", timeit.timeit(getWaterCount5,number = 1),getWaterCount5())
                    #print("get count 2: ", timeit.timeit(getWaterCount2,number = 1),getWaterCount2())
                    print("get count 3: ", timeit.timeit(getWaterCount3,number = 1),getWaterCount3())
                    print()
                elif e == K_LEFT:
                    times1 = []
                    times2 = []

                    while True:
                        grid = generate_grid(grid)
                        times1.append()


            elif event.type == pygame.QUIT:
                run = False

        #update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")