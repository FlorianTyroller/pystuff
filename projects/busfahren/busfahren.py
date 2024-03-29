import random as rd

ai_uses_perfect_logic = False
equal_as_third_option = False


class game:

    def __init__(self):
        # 0 = diamonds/hearts, 1 = spades/clubs
        self.c = ["♥","♠"]
        self.colors = [0,0,1,1]

        # 11 = j, 12 = q, 13 = K, 14 = A
        self.numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        self.deck = [(co,n) for co in self.colors for n in self.numbers]

        self.done = False
        self.open_cards = 0
        self.state = 0
        self.shotcount = 0
        self.selection = []
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))

    def reset_s(self):
        print("wrong...")
        self.open_cards += 1
        for i,s in enumerate(self.selection):
                if i < self.open_cards:
                    print(self.c[self.selection[i][0]],self.selection[i][1], end =" | ")
                else:
                    print("X", end =" | ")
        print()
        for i in range(self.state+1):
            self.selection[i] = self.deck.pop(rd.randint(0, len(self.deck)-1))
        self.open_cards = 0
        self.state = 0

            
    def go(self):
       
        # 0 = is index 0 black or red
        # 1 = is index 1 > or < than i 0
        # 2 = is index 2 inbetween i 1 and i 0 or not
        # 3 = is index 3 black or red

        

        while not self.done:
            for i,s in enumerate(self.selection):
                if i < self.open_cards:
                    print(self.c[self.selection[i][0]],self.selection[i][1], end =" | ")
                else:
                    print("X", end =" | ")
                
            print("    remaining cards in deck:", len(self.deck), " shotcount:", self.shotcount)
            if self.state == 4:
                self.done = True
                print("finished! shots to drink: %s" % (self.shotcount))
                break

            if self.state == 0:
                print("is 0 red or black? (0/1)")
                i = int(input())
                if i == self.selection[0][0]:
                    self.state += 1
                    self.open_cards += 1
                else:
                    self.reset_s()
                    self.shotcount += 1
            elif self.state == 1:
                print("is 1 higher or lower? (h/l)")
                i = input()
                if (i == "h" and self.selection[self.state][1] >= self.selection[0][1]) or (i == "l" and self.selection[self.state][1] <= self.selection[0][1]):
                    self.state += 1
                    self.open_cards += 1
                else:
                    self.reset_s()
                    self.shotcount += 2
            elif self.state == 2:
                print("is 2 between 1 and 0 or not? (y/n)")
                i = input()
                if (i == "y" and ((self.selection[0][1] <= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] >= self.selection[2][1] >= self.selection[1][1]))) \
                or (i == "n" and ((self.selection[0][1] >= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] <= self.selection[2][1] >= self.selection[1][1]))):
                    self.state += 1
                    self.open_cards += 1
                else:
                    self.reset_s()
                    self.shotcount += 3    
            elif self.state == 3:
                print("is 3 red or black? (0/1)")
                i = int(input())
                if i == self.selection[self.state][0]:
                    self.state += 1
                    self.open_cards += 1
                else:
                    self.reset_s()
                    self.shotcount += 4
    
    

def main():
    g = game()
    g.go()


if __name__ == "__main__":
    main()