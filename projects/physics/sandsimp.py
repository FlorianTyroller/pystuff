import os
import pygame
import time
import math
import random

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
    K_SPACE,
)

pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1500,900
cycletimes = [0,0,0,0,0,0]
scale = 10
types = {0:"Air",1:"Stone",2:"Gravel",3:"Sand",4:"Water"}
curr = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
height = SCREEN_HEIGHT//scale
width = SCREEN_WIDTH//scale

blocks = [[0 for i in range(height)] for j in range(width)]

def draw():
    screen.fill((255, 255, 255))
    for y in range(height):
        for x in range(width):
            if blocks[x][y] == 1:
                pygame.draw.rect(screen,(0,0,0),(x*scale,y*scale,scale,scale))
            elif blocks[x][y] == 2:
                pygame.draw.rect(screen,(100,90,90),(x*scale,y*scale,scale,scale))
            elif blocks[x][y] == 3:
                pygame.draw.rect(screen,(230,220,60),(x*scale,y*scale,scale,scale))
            elif blocks[x][y] == 4:
                pygame.draw.rect(screen,(80,120,240),(x*scale,y*scale,scale,scale))
    textsurface1 = myfont.render("current Block: " + types[curr], False, (0, 0, 0))
    textsurface2 = myfont.render("Avg Time: " + str((sum(cycletimes)/len(cycletimes))//10000), False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))
    screen.blit(textsurface2,(0,20))
    
    pygame.display.flip()

def update():
    for y in range(height-2,-1,-1):
        for x in range(width):
            #stone
            if blocks[x][y] == 1:
                None
            
            #gravel
            elif blocks[x][y] == 2:
                if blocks[x][y+1] == 0 or blocks[x][y+1] == 4:
                    blocks[x][y], blocks[x][y+1] = blocks[x][y+1], blocks[x][y]
            
            #sand
            elif blocks[x][y] == 3:
                if blocks[x][y+1] == 0 or blocks[x][y+1] == 4:   #below
                    blocks[x][y], blocks[x][y+1] = blocks[x][y+1], blocks[x][y]
                else:
                    if random.randint(0,1) == 1:
                        if x>0: #left
                            if (blocks[x-1][y] == 0 or blocks[x-1][y] == 4) and (blocks[x-1][y+1] == 0 or blocks[x-1][y+1] == 4):
                                blocks[x][y], blocks[x-1][y+1] = blocks[x-1][y+1], blocks[x][y]
                    else:
                        if x<width-1: #right
                            if (blocks[x+1][y] == 0 or blocks[x+1][y] == 4) and (blocks[x+1][y+1] == 0 or blocks[x+1][y+1] == 4):
                                blocks[x][y], blocks[x+1][y+1] = blocks[x+1][y+1], blocks[x][y]

            #water
            elif blocks[x][y] == 4:
                imp = False
                if x+1 < width:
                    imp = imp or (blocks[x+1][y] == 0)
                if x-1 >= 0:
                    imp = imp or (blocks[x-1][y] == 0)
                
                if blocks[x][y+1] == 0:   #below
                    blocks[x][y], blocks[x][y+1] = blocks[x][y+1], blocks[x][y]
                elif imp:
                    for i in range(width):
                        if random.randint(0,1) == 1:
                            if x+i < width:
                                if sum(a[y] for a in blocks[x+1:x+i+1]) == 0 and blocks[x+i][y+1] == 0:
                                    blocks[x][y], blocks[x+i][y+1] = blocks[x+i][y+1], blocks[x][y]
                                    break
                            if x-i >= 0: 
                                if sum(a[y] for a in blocks[x-i:x]) == 0 and blocks[x-i][y+1] == 0:
                                    blocks[x][y], blocks[x-i][y+1] = blocks[x-i][y+1], blocks[x][y]
                                    break
                        
                        else:
                            if x-i >= 0: 
                                if sum(a[y] for a in blocks[x-i:x]) == 0 and blocks[x-i][y+1] == 0:
                                    blocks[x][y], blocks[x-i][y+1] = blocks[x-i][y+1], blocks[x][y]
                                    break
                            if x+i < width:
                                if sum(a[y] for a in blocks[x+1:x+i+1]) == 0 and blocks[x+i][y+1] == 0:
                                    blocks[x][y], blocks[x+i][y+1] = blocks[x+i][y+1], blocks[x][y]
                                    break
                            
                        

    




def main():
    global blocks
    global curr    
    run = True
    fast = False
    global cycletimes
    draw()
    oldtime = time.time_ns()
    newtime = oldtime
    while run:
        newtime = time.time_ns()
        if fast:
            pos =  pygame.mouse.get_pos()
            gx = pos[0]//scale
            gy = pos[1]//scale
                
            if gx in range(width) and gy in range(height):
                blocks[gx][gy]=curr

        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_SPACE:
                    fast = not fast

            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos =  pygame.mouse.get_pos()
                gx = pos[0]//scale
                gy = pos[1]//scale
                
                if gx in range(width) and gy in range(height):
                    blocks[gx][gy]=curr
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                curr+=1
                curr%=len(types)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 5:
                curr-=1
                curr%=len(types)

        if newtime-oldtime > 10000:
            cycletimes.append(newtime-oldtime)
            if len(cycletimes) >= 10:
                cycletimes.pop(0)
            update()
            oldtime = newtime

        draw()
                
    pygame.quit()

if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")