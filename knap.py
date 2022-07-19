# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem
 
# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    print(res)
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break

        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            print(i - 1)

            res = res - val[i - 1]
            w = w - wt[i - 1]
 

hand_cards = [[0,0,0,0,3,1,4],[0,0,0,0,2,2,3],[0,0,0,0,2,2,3][0,0,0,0,1,2,2],[0,0,0,0,3,1,5],[0,0,0,0,2,4,1]]


val = [card[5] * card[6] for card in hand_cards]
wt = [card[4] for card in hand_cards]
W = 5
n = len(val)
print(printknapSack(W, wt, val, n))

