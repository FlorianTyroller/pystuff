import nltk
from collections import defaultdict


"""nltk.download('words')
words = nltk.corpus.words.words()"""

# read the words from the file in wordlists/gh3/wl.txt
with open('wordlists/gh3/wl.txt', 'r') as f:
    words = f.readlines()
    words = [w.strip() for w in words]

def didic(d, w):
    if len(w) == 0:
        d['end'] == True
        return d
    if w[0] in d:
        didic(d[w[0]], w[1:])
    else:
        d[w[0]] = didic(defaultdict(dict), w[1:])
    return d


mdict = defaultdict(dict)

for word in words:
    mdict = didic(mdict, word.lower())


# save the dictionary to a json file
import json

with open('dict.json', 'w') as fp:
    json.dump(mdict, fp)




