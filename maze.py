
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
)

pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800,800

scale = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = [[0 for j in range(SCREEN_WIDTH//scale)]for i in range(SCREEN_HEIGHT//scale)]


#generate maze

def generate(maze):
    for i in range(len(grid)):
        for j in range(len(grid)):
            maze[i][j] = random.randint(0,1)
    maze[0][0] = 2
    maze[-1][-1] = 3
    return maze
#draw

def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("maze", False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))

    #draw maze
    for i in range(len(grid)):
        for j in range(len(grid)):
            color = (100,100,100)
            if grid[i][j] == 0:
                color = (255,255,255)
            elif grid[i][j] == 1:
                color = (0,0,0)
            elif grid[i][j] == 2:
                color = (255,0,0)
            elif grid[i][j] == 3:
                color = (0,255,0)
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
    update()
    grid = generate(grid)
    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                

            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos =  pygame.mouse.get_pos()
                gx = pos[0]//scale
                gy = pos[1]//scale
                if gx in range(SCREEN_WIDTH) and gy in range(SCREEN_HEIGHT):
                    grid[gy][gx] += 1
                    grid[gy][gx] %= 2
                


        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
#generate maze

#solve maze
