import os
import pygame
import time
import math
import numpy as np
import random

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
    QUIT,
)


class M():

    def __init__(self):
        self.mr = [] 
        self.ma = 0
        self.s = 500
        self.scale = 4
        self.s = (self.s//self.scale) * self.scale
        self.rat = self.s//self.scale
        self.grid = [[random.randint(0, 1) for i in range(self.rat)] for j in range(self.rat)]
        pygame.font.init() 
        self.myfont = pygame.font.SysFont("Times New Roman",40)

        # Initialize pygame
        pygame.init()

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.s,self.s

        self.CENTER = (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))



    def findMostDense(self,size = 2):
        if size > self.rat:
            print("invalid size")
            return
        for size in range(2,self.rat):
            #t = 1/(self.rat-size)**2
            m = 0
            max = 0
            mx, my = 0, 0
            for i in range(0,self.rat-size+1):
                for j in range(0,self.rat-size+1):
                    self.paint()
                    #pygame.draw.rect(self.screen, (255,0,0), (i*self.scale-m,j*self.scale-m,size*self.scale+m,size*self.scale+m),width=int(self.scale*0.2))
                    s = 0
                    for k in range(size):
                        for l in range(size):
                            #print(grid[i+k][j+l], end="")
                            s += self.grid[i+k][j+l]
                        #print()
                    #print(s)#
                    if s > max:
                        max = s
                        mx = i
                        my = j


                    pygame.display.flip()
                    #print("rect")
                    #time.sleep(t)
            

            self.mr.append((mx*self.scale-m,my*self.scale-m,size*self.scale+m,size*self.scale+m))
            self.ma = max
        #print(mr)
        


    def paint(self):

        self.screen.fill((255, 255, 255))

        for i in range(self.rat):
            for j in range(self.rat):
                st = self.grid[i][j]
                if st == 1:
                    pygame.draw.rect(self.screen, (0,0,0), (i*self.scale,j*self.scale,self.scale,self.scale))

        if self.mr is not 0:
            for i,r in enumerate(self.mr):
                pygame.draw.rect(self.screen, (0,255,(255//len(self.mr))*i), r ,width=5)
            t = self.myfont.render("" + str(self.ma) , False, (0, 255, 0))
            self.screen.blit(t,(0,0))
        pygame.display.flip()


    def main(self):
        clicked = False
        run = True

        
        rotate = False

        while run:
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    e = event.key 
                    if e == K_ESCAPE:
                        run = False
                    elif e == K_SPACE:
                        self.mr = []
                        self.findMostDense()

    
                elif event.type == pygame.QUIT:
                    run = False
            #print(self.mr)
            self.paint()
                    
        
            

        pygame.quit()
            


if __name__ == '__main__':
    print("start rendering")
    main = M()
    main.main()
    print("complete")