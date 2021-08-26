import math


def pi(x):
    return math.pow(x, (1/math.pi))

def e(x):
    return math.pow(x, (1/math.e))


r = 2000
li = []

for i in range(r):
    for j in range(r):
        li.append((i,j,pi(i)-e(j)))

s = 1
t = ()

for l in li:
    if abs(l[2]) < s and abs(l[2]) > 0.0:
        s = abs(l[2])
        t = l


print(t)
    


