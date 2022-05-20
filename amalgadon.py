import random as rd


a = [1,2,3,4,"t","wf","d","p"]


pc = 0
s = 10000
max_aaa = 100 
for aas in range(max_aaa):
    pc = 0
    for j in range(s):
        ada = []
        for i in range(aas):
            c = rd.choice(a)
            while (c == "d" and "d" in ada) or (c == "p" and "p" in ada)or (c == "wf" and "wf" in ada)or (c == "t" and "t" in ada):
                c = rd.choice(a)
            ada.append(c)

        if "d" in ada and "p" in ada:
            pc += 1


    print("out of %s dons with %s adapts, %s are perfect -> %s" %(s,aas,pc,(pc/s)*100))