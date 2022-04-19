import random


lens = []
e = 0
while True:
    a =[1 for i in range(20)]

    c = 0
    o = 0
    while len(a) > 0:
        #print(a)
        if a[c] == 0:
            a.pop(c)
        else:
            a[c] = 0
            for i in range(len(a)):
                if i != c:
                    a[i] = 1

        
        if len(a) > 0:
            d = random.randint(0,len(a)-1)

            if a[d] == 0:
                a.pop(d)
            else:
                a[d] = 0
                for i in range(len(a)):
                    if i != d:
                        a[i] = 1

            if len(a) > 0:
                c += 1
                c %= len(a)
        o+=16
    lens.append(o)
    if e % 10 == 0:
        print("max: ", max(lens), " avg: ", sum(lens)/len(lens))
    e+=1
