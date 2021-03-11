#Blackjack
colors =  ['♦','♥','♣','♠']
zahlen = [str(i) for i in range(2,11)]
bilder = ['B','Q','K','A']

deck = []
for c in colors:
    for z in zahlen:
        deck.append(c+' '+z)
    for b in bilder:
        deck.append(c+' '+b)

print(colors)
print(zahlen)
print(bilder)
print(deck)