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


width = 20
height = 20

grid = [[0 for i in range(height)] for j in range(width)]

a = []

scale = 50

SCREEN_WIDTH, SCREEN_HEIGHT = width*scale,height*scale

myfont = pygame.font.SysFont("Times New Roman",(SCREEN_WIDTH)//40)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("scale: " + str(round(scale,1)), False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))



    #draw grid
    for i in range(height):
        pygame.draw.line(screen, (0,0,0), (0,i*scale), (SCREEN_WIDTH,i*scale), 1)

    for i in range(width):
        pygame.draw.line(screen, (0,0,0), (i*scale,0), (i*scale,SCREEN_HEIGHT), 1)

    #draw fields
    for i in range(width):
        for j in range(height):
            c = int(255*(0.8**grid[i][j]))
            pygame.draw.rect(screen,(c,c,c),(i*scale,j*scale,scale,scale))




    



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
                    print()


            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos =  pygame.mouse.get_pos()
                gx = pos[0]//scale
                gy = pos[1]//scale
                
                if gx in range(width) and gy in range(height):
                    grid[gx][gy]+=1
        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")