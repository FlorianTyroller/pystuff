from turtle import *
import math
import random as rnd

speed(1)
penup()
setx(-300)
sety(200)
pendown()
def tree(size, level, angle):
    if level == 0:
        return
    
    forward(size)
    right(angle)

    tree(size * 0.8, level - 1, angle*rnd.random()+10)


    left(angle * 2)

    tree(size * 0.8, level - 1, angle*rnd.random()+10)

    right(angle)
    backward(size)


def star(size, level, angle):
  
    if level == 0: 
        forward(size)
        return
    
    size /= 3 + rnd.random()
    
    star(size, level - 1, angle)
    left(angle)
    star(size, level - 1, angle)
    right(angle * 2)
    star(size, level - 1, angle)
    left(angle)
    star(size, level - 1, angle)
    

def starS(size, level, angle):
    for i in range(3):
        star(size, level, angle)
        right(60*2)

def HK(size, level):
  
    if level == 0: 
        forward(size)
        return
    
    size /= 2
    
    HK(size, level - 1)
    right(90)
    HK(size, level - 1)
    backward(size)
    left(90)
    backward(size)

def HKs(size, level):
    for i in range(4):
        HK(size, level)
        right(90)

HKs(200, 2)
mainloop()
