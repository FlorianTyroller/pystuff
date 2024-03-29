import random
import time
chickens = 1
chicks0 = 0
chicks7 = 0
chicks14 = 0
c = 0
e_to_c = 20

while True:
    c += 1
    if c % 7 == 0:
        temp = chicks14
        chicks14 = chicks7
        chicks7 = chicks0
        new_c = chickens * chickens + 1
        if new_c < 1:
            if random.randint(1, 8) <= e_to_c * 0:
                chicks0 += 1
        else:
            chicks0 += int(new_c)
        chickens += temp
        print("minute: ", c, "chickens: ", chickens, "chicks (0,7,14): (" + str(chicks0), "," , chicks7, "," , str(chicks14) + ")")

