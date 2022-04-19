import random
import numpy

c = 872
egg = (1,12)
rod = (2,2)
powder = (3,1)
eye = (4,1)
frame = (5,1)
l = []
le = 0
while True:

    eyes = 0
    d = 0

    while eyes < 12:
        r = random.randint(1,872) 
        d+=1
        if r == egg[0]:
            eyes += egg[1]
            #print("egg at ",d)
        elif r == rod[0]:
            eyes += rod[1]
            #print("rod at ",d)
        elif r == powder[0]:
            eyes += powder[1]
            #print("powder at ",d)
        elif r == eye[0]:
            eyes += eye[1]
            #print("powder at ",d)


    #print("tries: ",d)

    l.append(d)
    le = len(l)
    if le % 500 == 0:
        print("average: ", sum(l)/le, " tries: ", le, " max: ", max(l))