import numpy
import random
import sys
import PySimpleGUI as sg

#randomfunc

def getRandom(a):
    i = random.randint(0, len(a)-1)
    return a[i]

#classes
#players

class Player:
    def __init__(self,id):
        self.id = id
        self.board = ["","","","","","",""]
        self.boardI = 0
        self.attackI = 0
    def addMinion(self,m):
        if self.boardI < 7:
            while self.board[self.boardI] != "" and self.boardI < 6:
                self.boardI+=1
            self.board[self.boardI] = m

    def swapMinion(self,a,b):
        zs = self.board[a]
        self.board[a] = self.board[b]
        self.board[b] = zs

    def removeMinion(self,i):
        self.board[i] = ""
        self.boardI = 0

    def getAttacker(self):
        return self.board[self.attackI]

    def getDefender(self):
        return getRandom(self.board)

#minions

class Minion:
    def __init__(self,name,attack,hp,*args):
        if name == '':
            self.name = "default"
        else:
            self.name = name
        if hp == '':
            self.hp = -1
        else:
            self.hp = hp
        if attack == '':
            self.attack = -1
        else:
            self.attack = attack
        self.keywords = []
        for a in args:
            if a not in allowedKeywords:
                sys.exit(a + " is not an allowed keyword")
            else:
                self.keywords.append(str(a))
        self.loadMinion(name)
        
            
    def loadMinion(self,name):
        if name != "default":
            index = -1
            for i,l in enumerate(lines):
                if name in l[0]:
                    if index != -1:
                        sys.exit(name + " is found multiple times in the list of minions")
                    else:
                        index = i

            if index == -1:
                sys.exit(name + " is not found in the list of minions")
            else:
                self.name = lines[index][0]
                if self.attack == -1:
                    self.attack = lines[index][1]
                if self.hp == -1:
                    self.hp = lines[index][2]
                if len(lines[index])>2:
                    for l in lines[index][3:]:
                        if l not in self.keywords:
                            self.keywords.append(l)
#initialize

file = open('units.txt','r')
l = file.readlines()
lines = [a.strip().split(", ") for a in l]

allowedKeywords = ["taunt", "reborn", "divine", "poison", "windfury", "golden"]


p1 = Player(0)
p2 = Player(1)

#fill board
#TODO

#gui

# playere top

board_creator_column = [
    [sg.Text("Board creator")],
]
player_top_row = [
    [sg.Text("Top Player")],
    [sg.Text('Name', size=(15, 1)), sg.InputText(size=(15, 1),key="name")],
    [sg.Text('Attack', size=(15, 1)), sg.InputText(size=(5, 1),key="attack")],
    [sg.Text('HP', size=(15, 1)), sg.InputText(size=(5, 1),key="hp")],
    [sg.Checkbox('Golden', default=False,key="golden"), sg.Checkbox('Taunt', default=False,key="taunt"),sg.Checkbox('Reborn', default=False,key="reborn")],
    [sg.Checkbox('Windfury', default=False,key="windfury"),sg.Checkbox('Poison',default=False,key="poison"),sg.Checkbox('Divine', default=False,key="divine")],
    [sg.Radio('Top Player', "RADIO1", default=False,key="top"),sg.Radio('Bottom Player', "RADIO1", default=True,key="bot")],
    [sg.Button('Add', size=(5, 1)), sg.Button('Cancel')],
]


# For now will only show the name of the file that was chosen
board_viewer_column = [
    [sg.Text("Board",size=(10,6))],
]

temp = [[],[],[],[],[]]
temp[2].append(sg.Text("",size=(10,9)),)
for i,m in enumerate(p1.board):
    k = '1MINION' + str(i) #name
    kw = 'k1MINION' + str(i) #keywords
    ka = 'a1MINION' + str(i) #attack
    kh = 'h1MINION' + str(i) #hp      
    p = sg.Frame("",[[sg.Text("",key=k,size=(10,2),background_color='#9FB8AD')],[sg.Text("",key=kw,size=(10,3),background_color='#9FB8AD')],[sg.Text("",key=ka,size=(5,1),background_color='#9FB8AD'),sg.Text("",key=kh,size=(5,1),justification='right',background_color='#9FB8AD')]],background_color='#9FB8AD',pad=(8,0))
    temp[0].append(p)
    temp[1] += [sg.Button('<', size=(3, 1),key="1<"+str(i)),sg.Button('X', size=(4, 1),pad=(2,2),key="1X"+str(i)),sg.Button('>', size=(3, 1),key="1>"+str(i))]   
for i,m in enumerate(p2.board):
    k = '2MINION' + str(i) #name
    kw = 'k2MINION' + str(i) #keywords
    ka = 'a2MINION' + str(i) #attack
    kh = 'h2MINION' + str(i) #hp      
    temp[3].append(sg.Frame("",[[sg.Text("",key=k,size=(10,2),background_color='#9FB8AD')],[sg.Text("",key=kw,size=(10,3),background_color='#9FB8AD')],[sg.Text("",key=ka,size=(5,1),background_color='#9FB8AD'),sg.Text("",key=kh,size=(5,1),justification='right',background_color='#9FB8AD')]],background_color='#9FB8AD',pad=(8,0)))
    temp[4] += [sg.Button('<', size=(3, 1),key="2<"+str(i)),sg.Button('X', size=(4, 1),pad=(2,2),key="2X"+str(i)),sg.Button('>', size=(3, 1),key="2>"+str(i))] 
board_viewer_column+= temp

# ----- Full layout -----
layout = [
    [   

        sg.Column(board_creator_column+player_top_row),
        sg.VSeperator(),
        sg.Column(board_viewer_column,size=(1000, 600)),

    ]
]
# Create the window
window = sg.Window("Board Analyzer", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    

    print(event)
    if event=="Add":
        print('You entered ', values)
        #0->name;1->att;2->hp;3->gol;4->taunt;5->reb;6->wind;7->poi;8->div;9->top;10->bot
        #generate keyword list
        keywords = []
        for i in allowedKeywords:
            if values[i] == True:
                keywords.append(i)
        print(keywords)
        m = Minion(values["name"],values["attack"],values["hp"],*keywords)
        if values["top"] == True:
            p1.addMinion(m)
        else:
            p2.addMinion(m)        
    elif "X" in event:
        if event[0] == "1":
            p1.removeMinion(int(event[2]))
        if event[0] == "2":
            p2.removeMinion(int(event[2]))
    elif "<" in event:
        if event[2] != "0":
            if event[0] == "1":
                p1.swapMinion(int(event[2]),int(event[2])-1)
            if event[0] == "2":
                p2.swapMinion(int(event[2]),int(event[2])-1)
    elif ">" in event:
        if event[2] != "6":
            if event[0] == "1":
                p1.swapMinion(int(event[2]),int(event[2])+1)
            if event[0] == "2":
                p2.swapMinion(int(event[2]),int(event[2])+1)








    #update minions

    for i in range(7):
        k = '1MINION' + str(i) #name
        kw = 'k1MINION' + str(i) #keywords
        ka = 'a1MINION' + str(i) #attack
        kh = 'h1MINION' + str(i) #hp  
            
        if p1.board[i] != "":
            kws = " ".join(p1.board[i].keywords)
            window.Element(k).Update(p1.board[i].name)
            window.Element(kw).Update(kws)
            window.Element(ka).Update(p1.board[i].attack)
            window.Element(kh).Update(p1.board[i].hp)
        else:
            window.Element(k).Update("")
            window.Element(kw).Update("")
            window.Element(ka).Update("")
            window.Element(kh).Update("")
        
    for i in range(7):
        k = '2MINION' + str(i) #name
        kw = 'k2MINION' + str(i) #keywords
        ka = 'a2MINION' + str(i) #attack
        kh = 'h2MINION' + str(i) #hp  
            
        if p2.board[i] != "":
            kws = " ".join(p2.board[i].keywords)
            window.Element(k).Update(p2.board[i].name)
            window.Element(kw).Update(kws)
            window.Element(ka).Update(p2.board[i].attack)
            window.Element(kh).Update(p2.board[i].hp)  
        else:
            window.Element(k).Update("")
            window.Element(kw).Update("")
            window.Element(ka).Update("")
            window.Element(kh).Update("")       

 
window.close()



#start





    







    