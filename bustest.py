import random
# "1" 5/5
# "4" = divine
a = ["1",2,3,4]

ot = 20

c = 1000000
pc = 0

for i in range(c):
    perfect = False
    a = ["1",2,3,4]
    for j in range(ot):
        ad = random.choice(a)
        if ad == 4:
            perfect = True
            break
        if ad != "1":
            a.remove(ad)
    if perfect:
        pc +=1

    


print("count: %s, perfect: %s, ratio: %s" %(c,pc,pc/c))