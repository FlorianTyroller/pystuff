import numpy as np
import random

random.seed()

c = 0
s = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],              
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


def test (x,y,n):
    global s
    #row
    for i in s[y]:
        if i == n:
            return False
    #col
    for i in range(0,9):
        if s[i][x] == n:
            return False
    #sq
    sx = (x // 3) * 3
    sy = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if s[sy+i][sx+j] == n:
                return False
    return True
def reset():
    global s
    s = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],              
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
def gen():
    z = 0
    nums = 0
    global s
    global c
    while True:
        #print(c)
        a = random.randint(0,8)
        b = random.randint(0,8)
        d = random.randint(1,9)
        if s[a][b] == 0:
            if test(b,a,d):
                s[a][b] = d
                nums += 1
        c = 0
        if nums >= 37:
            print("solving")
            solve()
            print("solved " + str(z))
            z+=1
            if c == 0:
                reset()
                nums = 0
                print("reset")
            elif c == 1:
                print(np.matrix(s))
                return


def solve():
    global s
    global c
    for y in range(0,9):
        for x in range(0,9):
            if s[y][x] == 0:
                for n in range(1,10):
                    if test(x,y,n) :
                        s[y][x] = n
                        solve()
                        s[y][x] = 0
                return
    #print(np.matrix(s))
    #input("More?")
    c+=1
    

#print(np.matrix(s))
gen()
print(c)


