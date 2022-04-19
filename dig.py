def inter(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

def union(a,b):
    return list(set(a+b))

def diff(a,b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    return c

def braces(string):
    s = string.replace("{","")
    s = s.replace("}","")
    s = s.split(";")
    s = [int(i) for i in s]
    return s

def brackets(string):
    a = 0
    b = 0
    if string[0] == "]":
        a+=1
    
    if string[-1] == "]":
        b+=1

    s = string.replace("[","")
    s = s.replace("]","")
    s = s.split(";")
    s = [int(i) for i in s]

    a += s[0]
    b += s[-1]

    return list(range(a,b))

def parse(s):
    e = []
    for i in s:
        if i  == "{":
            


print(brackets("[1;5]"))