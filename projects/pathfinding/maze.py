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

class Node:
    def __init__(self,coords,vorgänger,type):
        self.type = type
        self.x, self.y = coords
        self.vorgänger = vorgänger
        self.g = 0
        self.visited = False


pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 820,820

scale = 20

c = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = [[Node((j,i),None,0) for j in range(SCREEN_WIDTH//scale)]for i in range(SCREEN_HEIGHT//scale)]


start = grid[0][0]
goal = grid[-1][-1]
#generate maze
def generate(maze):
    return generateD(maze)

def generateA(maze):
    global openQ
    global closedQ
    openQ  = {}
    openQ[0] = start
    closedQ = set()
    stack = []
    lastL = []
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            maze[i][j].type = 1
            maze[i][j].visited = False
    for i in range(len(grid)//2+1):
        for j in range(len(grid)//2+1):
            maze[i*2][j*2].type = 0
    
    u = getUCells()
    c = random.choice(u)
    while len(u) > 0:
        
        lastL.append(len(u))
        if len(lastL) > 100:
            lastL.pop(0)
            if lastL[0] == lastL[-1]:
                return maze
        n = getNei(c.x,c.y,2)
        if len(n) > 0:
            ne = random.choice(n)
            if ne in u:
                ne.visited = True
                grid[(c.x + ne.x)//2][(c.y + ne.y)//2].type = 0
                c = ne
        else:
            c = random.choice(u)
        u = getUCells()
        update()
    return maze

def getUCells():
    u = []
    for i in range(len(grid)//2+1):
        for j in range(len(grid)//2+1):
            if not grid[i*2][j*2].visited:
                u.append(grid[i*2][j*2])
    return u
        
def generateD(maze):
    global openQ
    global closedQ
    global start
    global goal
    openQ  = {}
    openQ[0] = start
    closedQ = set()
    stack = []
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            maze[i][j].type = 1
            maze[i][j].visited = False
    
    for i in range(len(grid)//2+1):
        for j in range(len(grid)//2+1):
            maze[i*2][j*2].type = 0

    stack.insert(0,grid[0][0])
    while len(stack) > 0:
        print(len(stack))
        current = stack.pop(0)
        current.visited = True
        n = getNei(current.x,current.y,2)
        
        if len(n) > 0:
            stack.insert(0,current)
            a = random.choice(n)
            a.visited = True
            grid[(current.x + a.x)//2][(current.y + a.y)//2].type = 0
 
            stack.insert(0,a)
            update()
            

    start.type  = 2
    goal.type  = 3
    return maze



def getNei(x,y,d):
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    n = []
    for di in dir:
        nx = x + d * di[0]
        ny = y + d * di[1]
        if nx in range(len(grid)) and ny in range(len(grid[0])):
            if grid[ny][nx].type == 0 and not grid[ny][nx].visited:
                n.append(grid[ny][nx])

    return n




   

def generateR(maze):
    global openQ
    global closedQ
    global start
    global goal
    openQ  = {}
    openQ[0] = start
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
                update()
                #time.sleep(0.1)
    '''
    for i in range(len(grid)//4):
        for j in range(len(grid)//4):
            maze[i*4+1][j*4+1].type = 1
            d = random.choice(dir)
            if maze[i*4+1+d[0]][j*4+1+d[1]].type == 0:
                maze[i*4+1+d[0]][j*4+1+d[1]].type = 1
                update()
                #time.sleep(0.1)
    '''

    start.type  = 2
    goal.type  = 3
    return maze


#solve maze
openQ  = {}
openQ[0] = start
closedQ = set()

def solveMaze():
    global openQ
    global closedQ
    openQ  = {}
    openQ[0] = start
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
    u = goal
    while u.vorgänger is not None:
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
    a = abs((goal.y - n.y)) + abs((goal.x - n.x))
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
    global start
    global goal
    run = True
    spam = False
    update()
    goal.type = 3
    t = 0
    
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
                elif e == K_r:
                    spam = not spam
                elif e == K_0:
                    t = 0
                elif e == K_1:
                    t = 1
                elif e == K_2:
                    t = 2
                elif e == K_3:
                    t = 3
                

            elif event.type == pygame.QUIT:
                run = False

            elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                pos =  pygame.mouse.get_pos()
                gx = pos[0]//scale
                gy = pos[1]//scale
                if gx in range(SCREEN_WIDTH) and gy in range(SCREEN_HEIGHT):
                    grid[gy][gx].type  = t
                    if t == 3:
                        grid[goal.y][goal.x].type = 0
                        goal = grid[gy][gx]
                    if t == 2:
                        grid[start.y][start.x].type = 0
                        start = grid[gy][gx]
                        openQ[0] = start
                    
        if spam:
            pos =  pygame.mouse.get_pos()
            gx = pos[0]//scale
            gy = pos[1]//scale
            if gx in range(SCREEN_WIDTH) and gy in range(SCREEN_HEIGHT):
                grid[gy][gx].type  = t
                if t == 3:
                    grid[goal.y][goal.x].type = 0
                    goal = grid[gy][gx]
                if t == 2:
                    grid[start.y][start.x].type = 0
                    start = grid[gy][gx]
                    openQ[0] = start

                
            

        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
#generate maze

#solve maze
