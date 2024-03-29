a = []
def appIfNotIn(a, e):
    if e not in a:
        a.append(e)
    return a


a = appIfNotIn(a, [1])
a = appIfNotIn(a, [1])
a = appIfNotIn(a, [1,2])
a = appIfNotIn(a, [1,2])
a = appIfNotIn(a, [1,2,3])

def comtest(l):
    print(l[2::][::-1])
    print(l[:1:-1])

def conv(n):
    a = ""
    s = 2**23
    while s > 0:
        if n >= s:
            a += "1"
            n -= s
        else:
            a += "0"
        s //=2
    return a



if __name__ == "__main__":
    # s = Solution()
    # comtest('0b0011')
    # print(conv(10**7))
    print()
    print(10**7)
    pass