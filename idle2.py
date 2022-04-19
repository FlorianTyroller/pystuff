import math




r = 10000
li = []

for i in range(1,r):
    for j in range(1,r):
        li.append((i,j,math.e - (i/j)))

s = 1
t = ()

for l in li:
    if abs(l[2]) < s and abs(l[2]) > 0.0:
        s = abs(l[2])
        t = l


print(*t)
    


