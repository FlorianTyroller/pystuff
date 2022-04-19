s = dict()

s[1] = 231233356
s[2] = 23123345673
s[3] = 231236
s[4] = 23123567
s[5] = 23123736
s[6] = 231236
s[7] = 1

print(len(s.values()), len(set(s.values())))

if 7 in s.keys():
    print(s[7])
else:
    print("e")


e = [[1,2,3,4,5],[3,4,5,1,1],"x"]

print(e)

e.remove("x")

print(e)