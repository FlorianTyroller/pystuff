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
)

class Node:
    def __init__(self,coords,vorgänger,type):
        self.type = type
        self.x, self.y = coords
        self.vorgänger = vorgänger
        self.g = 0


pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 820,820

scale = 20

c = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = [[Node((j,i),None,0) for j in range(SCREEN_WIDTH//scale)]for i in range(SCREEN_HEIGHT//scale)]



#generate maze

def generate(maze):
    global openQ
    global closedQ
    openQ  = {}
    openQ[0] = grid[0][0]
    closedQ = set()
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            maze[i][j].type = 0

    for i in range(len(grid)//2):
        for j in range(len(grid)//2):
            maze[i*2+1][j*2+1].type = 1
            d = random.choice(dir)
            if maze[i*2+1+d[0]][j*2+1+d[1]].type == 0:
                maze[i*2+1+d[0]][j*2+1+d[1]].type = 1
    for i in range(len(grid)//4):
        for j in range(len(grid)//4):
            maze[i*4+1][j*4+1].type = 1
            d = random.choice(dir)
            if maze[i*4+1+d[0]][j*4+1+d[1]].type == 0:
                maze[i*4+1+d[0]][j*4+1+d[1]].type = 1
    

    maze[0][0].type  = 2
    maze[-1][-1].type  = 3
    return maze


#solve maze
openQ  = {}
openQ[0] = grid[0][0]
closedQ = set()

def solveMaze():
    global openQ
    global closedQ
    openQ  = {}
    openQ[0] = grid[0][0]
    closedQ = set()

    while len(openQ) > 0 :
        #print(len(openQ))
        currentNode = openQ.pop(min(openQ))
        if currentNode.type == 3:
            markPath(grid)
            return
        closedQ.add(currentNode)
        expandNode(currentNode)
        #time.sleep(0.01)
        update()
    print("nopathFound")
    #draw

def markPath(g):
    u = g[-1][-1]
    while u.vorgänger is not None:
        print(u.vorgänger)
        u.type = 4
        u = u.vorgänger


def expandNode(n):
    global c
    succ = getSucc(n)
    for s in succ:
        if s in closedQ:
            continue

        tentative_g = n.g + 1

        if s in openQ.values() and tentative_g >= s.g:
            continue

        s.vorgänger = n
        s.g = tentative_g

        f = tentative_g + getH(s) + (c/100000)
        c += 1

        if s in openQ.values():
            for k, v in openQ.items():
                if v == s:
                    openQ.pop(k)
                    openQ[f] = v
                    break
        else:
            openQ[f] = s

def getH(n):
    a = (len(grid) - n.y) + (len(grid[0]) - n.x)
    return a

def getSucc(n):
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    succs = []
    for d in dir:
        nx = n.x + d[0]
        ny = n.y + d[1]
        if nx in range(len(grid)) and ny in range(len(grid)):
            if grid[ny][nx].type == 0 or grid[ny][nx].type == 3:
                succs.append(grid[ny][nx])
    return succs


def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("maze", False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))

    #draw maze
    for i in range(len(grid)):
        for j in range(len(grid)):
            color = (100,100,100)
            if grid[i][j].type  == 0:
                color = (255,255,255)
            elif grid[i][j].type  == 1:
                color = (0,0,0)
            elif grid[i][j].type  == 2:
                color = (255,0,0)
            elif grid[i][j].type  == 3:
                color = (0,255,0)

            
            
            if grid[i][j] in closedQ:
                color = (200,100,000)
            if grid[i][j] in openQ.values():
                color = (100,100,100)
            if grid[i][j].type  == 4:
                color = (102, 255, 153)
            pygame.draw.rect(screen,color,(j*scale,i*scale,scale,scale))


    #draw grid
    
    for i in range(SCREEN_HEIGHT//scale):
        pygame.draw.line(screen, (0,0,0), (0,i*scale), (SCREEN_WIDTH,i*scale), 1)
    
    for i in range(SCREEN_WIDTH//scale):
        pygame.draw.line(screen, (0,0,0), (i*scale,SCREEN_HEIGHT), (i*scale,0), 1)
    
    


    pygame.display.flip()

def main():
    global grid
    run = True
    spam = False
    update()
    grid = generate(grid)
    
    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_SPACE:
                    solveMaze()
                elif e == K_n:
                    grid = generate(grid)
               
                

            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos =  pygame.mouse.get_pos()
                gx = pos[0]//scale
                gy = pos[1]//scale
                if gx in range(SCREEN_WIDTH) and gy in range(SCREEN_HEIGHT):
                    grid[gy][gx].type  += 1
                    grid[gy][gx].type  %= 2
                


        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
#generate maze

#solve maze
