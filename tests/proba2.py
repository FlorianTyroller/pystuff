import random



crit_c = 20  # percentage
lucky_c = 50  # percentage
h_passive = True

samplesize = 100000
crits = 0
last_c = False
for i in range(samplesize):
    crit = False
    if last_c and h_passive:
        last_c = False
        crit = True
        crits += 1
        continue
    
    if random.randint(0, 100) < crit_c:
        crit = True
    else:
        if random.randint(0, 100) < lucky_c:
            if random.randint(0, 100) < crit_c:
                crit = True
    if crit:
        last_c = True
        crits += 1

print(crits / samplesize, crits, samplesize)
