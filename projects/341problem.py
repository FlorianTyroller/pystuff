
import time
a = dict()

x = 1
while True:
    y = x
    c = 0
    while True:
        if y in a:
            print(x, "made", c , "new steps")
            break
        
        a[y]
        
        if y % 2 == 0:
            y //= 2
        else:
            y = y * 3 + 1
        c += 1
    # print(a)
    # time.sleep(1)
    x += 1
