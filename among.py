import random

total = 10
imps = 2
state = 0
iWin = 0
cWin = 0
def checkwin():
    #0 = undecided, 1 = crew, 2 = impo
    if imps == 0:
        return 1
    if imps == (total-imps):
        return 2
    return 0

try:
    while True:
        
        while (state := checkwin()) == 0:

            vote = random.randint(1,total)
            if vote <= imps:
                imps -= 1
                total -= 1
            else:
                total -= 1

        if state == 1:
            cWin += 1
        else:
            iWin += 1
        total = 10
        imps = 4
        state = 0

        if (cWin+iWin)%1000000 == 0:
            print("cWins:",cWin, "iWins:",iWin,"cWinperc:",cWin/(cWin+iWin))

except KeyboardInterrupt:
        print("cWins:",cWin, "iWins:",iWin,"cWinperc:",cWin/(cWin+iWin))    
    
