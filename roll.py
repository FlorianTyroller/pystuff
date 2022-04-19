import random as rd

a = (0.01,77777)
b = (0.1, 1000)
c = (0.05, 2500)
d = (0.5, 100)
l = [a,b,c,d]
cube = [a,a,a,a,a,a]

su = 0
r = 5000000

g = True


max = 0
bestC = []
t = 0
while (True):
    t += 1
    cube = [] 
    for i in range(6):
        cube.append(rd.choice(l))
    
    lw = False
    su = 0
    for i in range(r):
        s = rd.choice(cube)
        if lw:
            su += s[1]
            lw = False
        else:
            if rd.random() <= s[0]:
                su += s[1]
                if g:
                    lw = True

    if su > max:
        max = su
        bestC = cube
        print(max, bestC, "Tries:", t)

    