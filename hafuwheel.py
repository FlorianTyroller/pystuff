import random

w1 = [(1,"r"), (0,"c"), (1,"n"), (2,"n"), (2, "n"), (2, "r"), (1,"h"), (1,"r")]

w2 = [(5, "r"), (5, "r"), (5, "r"),  (10,"n"), (0,"c"), (10, "a"), (0,"c"), (10, "r")]

w3 = [(20, "f"), (0,"c"), (15, "n"), (0,"c"), (12, "r"), (0,"c"), (15, "r"), (18, "r")]

w4 = [(50, "r"), (100, "u"), (75, "c"), (100, "c"), (75,"c")]

w5 = [(200,"c"), (300,"c"), (400,"c"), (500,"c")]


wheels = [w1, w2, w3, w4, w5]

es = []
ws = []
for i in range(100000):
    wheelc = 0

    earning = 0

    respawn = True

    ls = []

    while True:
        t = random.choice(wheels[wheelc])
        earning += t[0]
        if t[1] == "n":
            wheelc += 1
        
        if t[1] == "c":
            if earning < 10 and respawn:
                respawn = False
            else:
                break
        if t[1] in ["h", "a", "f", "u"]:
            ls.append(t[1])
            if t[1] == "u":
                # check if h a f and u are in the ls
                if "h" in ls and "a" in ls and "f" in ls and "u" in ls:
                    wheelc += 1
                else:
                    break
    
    ws.append(wheelc)
    es.append(earning)

# print average of ws and es
print(sum(ws)/len(ws))
print(sum(es)/len(es))


# print the count 4 in ws
print(ws.count(0), ws.count(1), ws.count(2), ws.count(3), ws.count(4), len(ws))


