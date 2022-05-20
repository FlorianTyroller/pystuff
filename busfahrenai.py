import random as rd
from statistics import mean
from collections import defaultdict




class game:

    def __init__(self, equal_is_False, logic, debug, debug_dic = None):
        # 0 = diamonds/hearts, 1 = spades/clubs
        self.c = ["♥","♠"]
        self.colors = [0,0,1,1]
        self.logc = ""
        if logic in ["perfect","human","random"]:
            self.logic = logic
        else:
            self.logic = "random"

        self.equal_as_third_option = equal_is_False
        # 11 = j, 12 = q, 13 = K, 14 = A
        self.numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        self.deck = [(co,n) for co in self.colors for n in self.numbers]
        self.remixed = 0
        self.done = False
        self.open_cards = 0
        self.state = 0
        self.shotcount = 0
        self.cdump = defaultdict(int)
        self.selection = []
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.debug = debug
        self.debug_stats = debug_dic


    def reset_deck(self):
        self.remixed += 1
        self.cdump = defaultdict(int)
        self.deck = [(co,n) for co in self.colors for n in self.numbers]
        self.selection = []
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))
        self.selection.append(self.deck.pop(rd.randint(0, len(self.deck)-1)))


    def reset_s(self):
        if self.state + 1 > len(self.deck):
            self.reset_deck()
        else:
            for i in range(self.state+1):
                self.selection[i] = self.deck.pop(rd.randint(0, len(self.deck)-1))
        self.open_cards = 0
        self.state = 0

    def get_guess_state_0_random(self):
        return rd.choice([0,1])
        
    def get_guess_state_0_perfect(self):
        if self.cdump[0] > self.cdump[1]:
            return 1
        else:
            return 0
    
    def get_guess_state_0_human(self):
        return self.get_guess_state_0_perfect()
    
    def get_guess_state_1_random(self):
        if self.equal_as_third_option:
            return rd.choice(["h","l","e"])
        return rd.choice(["h","l"])
    
    def get_guess_state_1_human(self):
        if self.selection[0][1] > 8:
            return "l"
        else:
            return "h"
    
    def get_guess_state_1_perfect(self):
        
        c = []
        for i in range(self.state,4):
            c.append(self.selection[i])
        c += self.deck
        
        ht = 0
        lt = 0
        eq = 0

        if self.equal_as_third_option:
            for i in c:
                if i[1] > self.selection[0][1]:
                    ht += 1
                elif i[1] < self.selection[0][1]:
                    lt += 1
                elif i[1] == self.selection[0][1]:
                    eq += 1
            
            m = max([eq,ht,lt])
            if m == eq:
                return "e"
            elif m == lt:
                return "l"
            else:
                return "h"
        else:
            for i in c:
                if i[1] > self.selection[0][1]:
                    ht += 1
                elif i[1] < self.selection[0][1]:
                    lt += 1
            
            if lt > ht:
                return "l"
            else:
                return "h"


    def get_guess_state_3_random(self):
        return rd.choice([0,1])
    
    def get_guess_state_3_perfect(self):
        if self.cdump[0] > self.cdump[1]:
            return 1
        else:
            return 0
    
    def get_guess_state_3_human(self):
        return self.get_guess_state_3_perfect()

    def get_guess_state_2_random(self):
        if self.equal_as_third_option:
            return rd.choice(["y","n","e"])
        return rd.choice(["y","n"])
    
    def get_guess_state_2_perfect(self):
        
        c = []
        for i in range(self.state,4):
            c.append(self.selection[i])
        c += self.deck
        
        between = 0
        outside = 0
        eq = 0

        if self.equal_as_third_option:
            for i in c:
                if (i[1] == self.selection[0][1]) or (i[1] == self.selection[1][1]):
                    eq += 1
                elif (self.selection[0][1] > i[1] < self.selection[1][1]) or (self.selection[0][1] < i[1] > self.selection[1][1]):
                    outside += 1
                else:
                    between += 1

            m = max([eq,between,outside])
            if m == eq:
                return "e"
            elif m == between:
                return "y"
            else:
                return "n"
        else:
            for i in c:
                if (i[1] == self.selection[0][1]) or (i[1] == self.selection[1][1]):
                    eq += 1
                elif (self.selection[0][1] > i[1] > self.selection[1][1]) or (self.selection[0][1] < i[1] < self.selection[1][1]):
                    between += 1
                else:
                    outside += 1

            m = max([between,outside])
            if m == between:
                return "y"
            else:
                return "n"

    
    def get_guess_state_2_human(self):
        if self.equal_as_third_option:
            if abs(self.selection[0][1] - self.selection[1][1]) > 5:
                return "y"
            else:
                return "n"

        if abs(self.selection[0][1] - self.selection[1][1]) > 4:
            return "y"
        else:
            return "n"



    def go(self):
       
        # 0 = is index 0 black or red
        # 1 = is index 1 > or < than i 0
        # 2 = is index 2 inbetween i 1 and i 0 or not
        # 3 = is index 3 black or red

        

        while not self.done:
            if self.state == 4:
                self.done = True
                break

            if self.state == 0:
                if self.debug:
                    
                    p = self.get_guess_state_0_perfect()
                    
                    h = self.get_guess_state_0_human()
                    
                    i = self.get_guess_state_0_random()

                    self.cdump[self.selection[self.state][0]] += 1

                    if i == self.selection[0][0]:
                        if h == i:
                            self.debug_stats[self.state]["human"] += 1
                        if p == i:
                            self.debug_stats[self.state]["perfect"] += 1
                        self.state += 1
                        self.open_cards += 1
                    else:
                        self.reset_s()
                        self.shotcount += 1
                else:
                    if self.logic == "perfect":
                        i = self.get_guess_state_0_perfect()
                    elif self.logic == "human":
                        i = self.get_guess_state_0_human()
                    elif self.logic == "random":
                        i = self.get_guess_state_0_random()

                    self.cdump[self.selection[self.state][0]] += 1
                    if i == self.selection[0][0]:
                        self.state += 1
                        self.open_cards += 1
                    else:
                        self.reset_s()
                        self.shotcount += 1

                
            elif self.state == 1:
                if self.debug:
                    p = self.get_guess_state_1_perfect()
                    h = self.get_guess_state_1_human()
                    i = self.get_guess_state_1_random()

                    self.cdump[self.selection[self.state][0]] += 1

                    if self.equal_as_third_option:
                        if (i == "h" and self.selection[self.state][1] > self.selection[0][1]) or (i == "l" and self.selection[self.state][1] < self.selection[0][1]) or (i == "e" and self.selection[self.state][1] == self.selection[0][1]):
                            if h == i:
                                self.debug_stats[self.state]["human"] += 1
                            if p == i:
                                self.debug_stats[self.state]["perfect"] += 1
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 2
                    else:
                        if (i == "h" and self.selection[self.state][1] >= self.selection[0][1]) or (i == "l" and self.selection[self.state][1] <= self.selection[0][1]):
                            if h == i:
                                self.debug_stats[self.state]["human"] += 1
                            if p == i:
                                self.debug_stats[self.state]["perfect"] += 1
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 2
                else:
                    if self.logic == "perfect":
                        i = self.get_guess_state_1_perfect()
                    elif self.logic == "human":
                        i = self.get_guess_state_1_human()
                    elif self.logic == "random":
                        i = self.get_guess_state_1_random()

                    self.cdump[self.selection[self.state][0]] += 1

                    if self.equal_as_third_option:
                        if (i == "h" and self.selection[self.state][1] > self.selection[0][1]) or (i == "l" and self.selection[self.state][1] < self.selection[0][1]) or (i == "e" and self.selection[self.state][1] == self.selection[0][1]):
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 2
                    else:
                        if (i == "h" and self.selection[self.state][1] >= self.selection[0][1]) or (i == "l" and self.selection[self.state][1] <= self.selection[0][1]):
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 2




            elif self.state == 2:
                if self.debug:
                    p = self.get_guess_state_2_perfect()
                    h = self.get_guess_state_2_human()
                    i = self.get_guess_state_2_random()
                    
                    self.cdump[self.selection[self.state][0]] += 1

                    if self.equal_as_third_option:
                        if (i == "y" and ((self.selection[0][1] < self.selection[2][1] < self.selection[1][1]) or (self.selection[0][1] > self.selection[2][1] > self.selection[1][1]))) \
                        or (i == "n" and ((self.selection[0][1] > self.selection[2][1] < self.selection[1][1]) or (self.selection[0][1] < self.selection[2][1] > self.selection[1][1]))) \
                        or (i == "e" and ((self.selection[0][1] == self.selection[2][1]) or (self.selection[2][1] == self.selection[1][1]))):
                            if h == i:
                                self.debug_stats[self.state]["human"] += 1
                            if p == i:
                                self.debug_stats[self.state]["perfect"] += 1
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 3   
                    else: 
                        if (i == "y" and ((self.selection[0][1] <= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] >= self.selection[2][1] >= self.selection[1][1]))) \
                        or (i == "n" and ((self.selection[0][1] >= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] <= self.selection[2][1] >= self.selection[1][1]))):
                            if h == i:
                                self.debug_stats[self.state]["human"] += 1
                            if p == i:
                                self.debug_stats[self.state]["perfect"] += 1
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 3  
                else:
                    if self.logic == "perfect":
                        i = self.get_guess_state_2_perfect()
                    elif self.logic == "human":
                        i = self.get_guess_state_2_human()
                    elif self.logic == "random":
                        i = self.get_guess_state_2_random()
                    
                    self.cdump[self.selection[self.state][0]] += 1

                    if self.equal_as_third_option:
                        if (i == "y" and ((self.selection[0][1] < self.selection[2][1] < self.selection[1][1]) or (self.selection[0][1] > self.selection[2][1] > self.selection[1][1]))) \
                        or (i == "n" and ((self.selection[0][1] > self.selection[2][1] < self.selection[1][1]) or (self.selection[0][1] < self.selection[2][1] > self.selection[1][1]))) \
                        or (i == "e" and ((self.selection[0][1] == self.selection[2][1]) or (self.selection[2][1] == self.selection[1][1]))):
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 3   
                    else: 
                        if (i == "y" and ((self.selection[0][1] <= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] >= self.selection[2][1] >= self.selection[1][1]))) \
                        or (i == "n" and ((self.selection[0][1] >= self.selection[2][1] <= self.selection[1][1]) or (self.selection[0][1] <= self.selection[2][1] >= self.selection[1][1]))):
                            self.state += 1
                            self.open_cards += 1
                        else:
                            self.reset_s()
                            self.shotcount += 3  

            
            elif self.state == 3:
                if self.debug:
                    p = self.get_guess_state_3_perfect()
                    h = self.get_guess_state_3_human()
                    i = self.get_guess_state_3_random()

                    self.cdump[self.selection[self.state][0]] += 1
                    if i == self.selection[self.state][0]:
                        if h == i:
                            self.debug_stats[self.state]["human"] += 1
                        if p == i:
                            self.debug_stats[self.state]["perfect"] += 1
                        self.state += 1
                        self.open_cards += 1
                    else:
                        self.reset_s()
                        self.shotcount += 4
                else:
                    if self.logic == "perfect":
                        i = self.get_guess_state_3_perfect()
                    elif self.logic == "human":
                        i = self.get_guess_state_3_human()
                    elif self.logic == "random":
                        i = self.get_guess_state_3_random()

                    self.cdump[self.selection[self.state][0]] += 1
                    if i == self.selection[self.state][0]:
                        self.state += 1
                        self.open_cards += 1
                    else:
                        self.reset_s()
                        self.shotcount += 4
        return (self.shotcount, self.remixed)
    
    
    

def main():
    r = 10000000
    
    erg = []
    remixed = defaultdict(int)
    debug_dec = {0:{"human": 0, "perfect": 0},1:{"human": 0, "perfect": 0},2:{"human": 0, "perfect": 0},3:{"human": 0, "perfect": 0}}
    for i in range(r):
        g = game(equal_is_False = True,logic = "random", debug = False, debug_dic=None)
        e = g.go()
        erg.append(e[0])
        remixed[e[1]] += 1
        if i % 30000 == 0:
            print("games: %s, max: %s, avg: %s" %(i, max(erg), mean(erg)))
    
    print("games: %s, max: %s, avg: %s" %(r, max(erg), mean(erg)))
    print(remixed)


if __name__ == "__main__":
    main()