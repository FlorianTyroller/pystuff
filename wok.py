import random as rd
wp = 0.03
lp = 0.025
wr = 0.50

v = 0.90
 
ss = 100
p = 0

e = 0
r = 0
cp = 0
a = True
for i in range(ss):
    e=0
    a = True
    while a:
        e+=1
        if rd.random() < wr:
            #win
            cp += wp
            if rd.random() <= cp:
                cp = 0
                p+=1
            
        else:
        #lose
            cp += lp 
        
        if cp >= v:
            r+=e
            a = False


print(ss, r, ss/r, v)


