import math
import random

import time

radius = 1
len = 1
innen = 0
outen = 0
score = 1
t = 0
erg = 0
z = 0
x = 0
y = 0
dist = 0
try: 
    while True:
        z+=1
        x = random.random() * 2 -1 
        y = random.random() * 2 -1 
        dist = math.sqrt(x*x+y*y)
 
        if dist <= len:
            score+=1
            len = math.sqrt(len*len - dist*dist)

        else:
            erg += score
            score = 1
            t += 1
            len = 1
 
        if z%1000000 == 0:
            print(erg/t,t)
             
except KeyboardInterrupt:
    print("end",erg/t,t)