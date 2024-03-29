import random as rd
import time
ai_uses_perfect_logic = False
equal_as_third_option = False


class game:

    def __init__(self):
        # 0 = diamonds/hearts, 1 = spades/clubs
        self.c = ["♥","♠"]
        self.colors = [0,0,1,1]

        # 11 = j, 12 = q, 13 = K, 14 = A
        self.numbers = [7,8,9,10,11,12,13,14]

        self.deck = [(co,n) for co in self.colors for n in self.numbers]
        self.open_cards = []
        self.done = False
        self.shotcount = 0
        self.dealerChanges = 0
        self.randomGuesses = True

    def reset_s(self):
        self.deckll = [(co,n) for co in self.colors for n in self.numbers]
        self.open_cards = []

    def print_open_cards(self):

        card = ["╔══╗","║  ║","╚══╝","   x"]

        
        for i,c in enumerate(card):
            for n in self.numbers:
                e = self.open_cards.count(n)
                if e == 0:
                    print("    ",end="")
                else:
                    if i == 1:
                        if n <= 9:
                            print(c[:2] + str(n) + c[3:], end="")
                        else:
                            print(c[:1] + str(n) + c[3:], end="")
                    elif i == 3:
                        if e <= 9:
                            print(c[:2] + str(e) + c[3:], end="")
                        else:
                            print(c[:1] + str(e) + c[3:], end="")
                    else:
                        print(c, end="")
            print()


            
    def go(self):

        lossCount = 0
        while not self.done:
            self.print_open_cards()
            print("\n")
            print("\n")
            if self.randomGuesses:
                # guess is a random number out of self.numbers
                guess = rd.choice(self.numbers)
                print("Guess:", guess)
                # wait for 1 second
                time.sleep(1)
                
            else:
                guess = input("Choose a number: ")
                # if guess is not a number ask again untill a number is given
                while not guess.isdigit():
                    guess = input("not a valid number, choose a number: ")
                guess = int(guess)

            randomCard = self.deck.pop(rd.randint(0,len(self.deck)-1))

            if randomCard[1] == guess:
                print("Correct!")
                lossCount = 0
            else: 
                if guess < randomCard[1]:
                    print("dealers card is higher")
                elif guess > randomCard[1]:
                    print("dealers card is lower")
                if self.randomGuesses:
                    # guess is a random number out of self.numbers
                    guess2 = rd.choice(self.numbers)
                    print("Guess2:", guess2)
                    # wait for 1 second
                    time.sleep(1)
                else:
                    guess2 = input("Choose a number: ")
                    # if guess is not a number ask again untill a number is given
                    while not guess2.isdigit():
                        guess2 = input("not a valid number, choose a number: ")
                    guess2 = int(guess2)
                if guess2 == randomCard[1]:
                    print("Correct!")
                    lossCount = 0
                else:
                    print("Incorrect!")
                    lossCount += 1
            self.open_cards.append(randomCard[1])
            
            # if deck is empty end the game
            if len(self.deck) == 0:
                self.done = True
                print("game over") 
                print("dealerchanges: " + str(self.dealerChanges))

            if lossCount == 3:
                self.dealerChanges += 1
                print("next Dealer")
                lossCount = 0
    
    

def main():
    g = game()
    g.go()


if __name__ == "__main__":
    main()