import os
import pygame
import time
import math
import random
import heapq
from queue import PriorityQueue

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_PLUS,
    K_MINUS,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    K_n,
    K_r,
    QUIT,
    K_0,
    K_1,
    K_2,
    K_3
)

pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SIZE = 800
SCREEN_WIDTH, SCREEN_HEIGHT = SIZE, SIZE


scale = 20
off = (SIZE//scale)//2
r = 400//scale
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = [[[1 if math.sqrt((i-off)*(i-off)+(j-off)*(j-off)+(k-off)*(k-off)) < math.sqrt(r) else 0 for k in range(SIZE//scale)] for j in range(SIZE//scale)] for i in range(SIZE//scale)]

def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("circle", False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))


    for i in range(SIZE//scale):
        for j in range(SIZE//scale):
            m = sum(grid[i][j])/r
            print(m)
            c = int(255 * m)
            color = (c,c,c)
            pygame.draw.rect(screen,color,(j*scale,i*scale,scale,scale))
    #draw grid
    
    for i in range(SCREEN_HEIGHT//scale):
        pygame.draw.line(screen, (0,0,0), (0,i*scale), (SCREEN_WIDTH,i*scale), 1)
    
    for i in range(SCREEN_WIDTH//scale):
        pygame.draw.line(screen, (0,0,0), (i*scale,SCREEN_HEIGHT), (i*scale,0), 1)
    
    


    pygame.display.flip()

def main():
    run = True
    update()

    
    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False

                

            elif event.type == pygame.QUIT:
                run = False

                    

            

        update()

if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")