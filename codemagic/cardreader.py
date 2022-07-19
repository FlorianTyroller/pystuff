from csv import reader
import keyboard
import time
# open file in read mode
cards = []
with open('cardlist.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # split row by ;
        cards.append(row[0].split(';'))

iss = [0,3,4,5,7,8,9]
new_cards = []
for c in cards:
    new_cards.append([int(x.replace(' ', '')) if i in iss else x for i,x in enumerate(c)])

# sort new_cards by 3rd index
new_cards.sort(key=lambda x: x[3])

# if space key is pressed print next entry of list
while True:
    if keyboard.is_pressed('space'):
        print(new_cards[0])
        new_cards.pop(0)
        time.sleep(0.5)
        if len(new_cards) == 0:
            break  