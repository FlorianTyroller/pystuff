import random

abc = "abcdefghijklmnopqrstuvwxyz"
word = "affentheater"
wc = 0
print()

c = 0
hc = 0
while True:
    if wc == len(word):
        break
    c+=1
    r = random.choice(abc)
    if r == word[wc]:
        wc += 1
    else:
        if wc > hc:
            hc = wc
            print(c,hc)
        wc = 0

    if c % 100000000 == 0:
        print(c,hc)

print(c,"finished")