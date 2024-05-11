import random
import json
width = 50
height = 50


mp = []
c = 0
even = False
for i in range(-height//2, height//2-1):
    for j in range(-c,width-c):
        mp.append((j, i))

    if even:
        c+=1
        even = False
    else:
        even = True

rs = ["ore", "brick", "lumber", "desert", "wool", "grain"]
aa = []
bb = []
for a in range(width*height):
    aa.append(random.choice(rs))
    bb.append(None)

print(len(mp))
e = dict()
e['resources'] = aa
e['numbers'] = bb
e['layout'] = mp

with open("C:/Users/Flori/Desktop/pypy/projects/catan/test.json", "w") as file:
    json.dump(e,file,indent=4)