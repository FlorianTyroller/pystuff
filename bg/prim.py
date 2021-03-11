import math
i = 3267000013


prime = True
for j in range(2,math.ceil(math.sqrt(i))):
    if prime:
        if i % j == 0:
            prime = False
if prime == True:
    print(i, " is prime")
else:
    print(i, " is not prime")

