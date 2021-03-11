import random
n = 6178552
tries = 0
lens = 0

try:
    while True:
        enc = []
        o = 1
        while o not in enc:
            enc.append(o) 
            o = random.randint(1,n)
        lens += len(enc)
        tries += 1

        if tries % 1000 == 0:
            print("Tries:",tries,"average len:",lens/tries)

except KeyboardInterrupt:
        print("Tries:",tries,"average len:",lens/tries)   