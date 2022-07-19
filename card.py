import random


colors = ['d','s','h','c']
numbers = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
cards = [(n,c) for n in numbers for c in colors]
hand = []
def drawCards(number):
    global cards
    c = []
    if number > 0:
        for i in range(number):
            o = random.choice(cards)
            c.append(o)
            cards.remove(o)
    return c


def getHandValue(h):
    if len(h)>0:
        value = [0]
        for i in h:
            if i[0].isnumeric():
                for j in range(len(value)):
                    value[j] += int(i[0])
            elif i[0] != 'a':
                for j in range(len(value)):
                    value[j] += 10
            else:
                for j in range(len(value)):
                    value.append(value[j] + 11)
                    value[j] += 1
        return set(value)
    else:
        return {0}

def newDeck():
    global cards
    cards = [(n,c) for n in numbers for c in colors]


hands = {}
hs = 0
while True:
    
    newDeck()
    hand = []
    end = False
    hand.extend(drawCards(2))
    

    while not end:
        v = getHandValue(hand)
        if min(v) > 21:
            end = True
            #print("overdraw")
            #print(hand, min(v))
            hands[0] = hands.get(0,0) + 1
        elif 21 in v:
            end = True
            hands[len(hand)] = hands.get(len(hand),0) + 1
            hs+=1
            if hs%1000 == 0:
                print(hands)

        else:
            #print(hand, v)
            hand.extend(drawCards(1))
            




#player
'''
while not end:
    v = getHandValue(hand)
    if min(v) > 21:
        end = True
        print("overdraw")
        print(hand, min(v))
    elif 21 in v:
        end = True
        print("21 21 21 21")
        print(hand, "21")
    else:
        print(hand, v)
        a = input("draw more y/n ?")
        if a == "y":
            hand.extend(drawCards(1))
        else:
            end = True
            print("bail out", v)
'''

    


