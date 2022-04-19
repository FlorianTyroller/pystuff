
a = [1,4,56,2,63,78,12] 
def insert (a):
    i = 0
    j = 0
    key = 0

    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1

        a[i+1] = key

    return a

print(a)
print(insert(a))