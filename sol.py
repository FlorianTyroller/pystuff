import math


x=0
try:
    while True:
        a = x*x
        b = 2**x
        if a == b:
            print("x = " + str(x))
        x+=1      
except KeyboardInterrupt:
    print("end")