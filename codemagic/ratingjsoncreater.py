from csv import reader
import keyboard
import time
import json
# open file in read mode
cards = {}
with open('cardratings.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for i,row in enumerate(csv_reader):
        if i != 0:
            # row variable is a list that represents a row in csv
            # split row by ;
            entries = row[0].split('\t')
            cards[int(entries[0])] = tuple((float(e) for e in entries[1:]))


print(json.dumps(cards))