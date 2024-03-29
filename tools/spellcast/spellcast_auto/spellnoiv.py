import nltk
#from PyDictionary import PyDictionary
import json
import random

class Grid:
    def __init__(self, grid, wordtree, dl=None, tl=None, dw=None):
        self.grid = grid
        self.visited = [[False] * 5 for _ in range(5)]
        self.strings = []
        self.string_count = 0
        self.total_strings = 0
        self.wordtree = wordtree
        self.letter_scores = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4, 'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8}
        self.dl = dl
        self.tl = tl
        self.dw = dw

    def is_valid_word(self, word):
        di = self.wordtree
        while len(word) > 0:
            if word[0] in di:
                di = di[word[0]]
                word = word[1:]
            else:
                return False
        return 'end' in di

    def no_words_start_with(self, prefix):
        if len(prefix) == 0:
            return False
        di = self.wordtree
        while len(prefix) > 0:
            if prefix[0] in di:
                di = di[prefix[0]]
                prefix = prefix[1:]
            else:
                return True
        return False

    def generate_strings(self):
        for i in range(5):
            for j in range(5):
                self.dfs(i, j, '', [])

    def dfs(self, row, col, current_string, current_path, current_score=0, current_multiplier=1):
        if row < 0 or row >= 5 or col < 0 or col >= 5:
            return
        if self.visited[row][col]:
            return
        current_string += self.grid[row][col]
        current_path.append((row, col))
        l_score = self.letter_scores[self.grid[row][col].lower()]
        if self.dw and (row == self.dw[1] and col == self.dw[0]):
            current_multiplier = 2
        if self.tl and (row == self.tl[1] and col == self.tl[0]):
            l_score *= 3
        if self.dl and (row == self.dl[1] and col == self.dl[0]):
            l_score *= 2
        current_score += l_score
        if self.is_valid_word(current_string):
            add = 0
            if len(current_string) > 5:
                add = 10
            self.strings.append((current_string, current_score*current_multiplier + add, current_multiplier, tuple(current_path)))
        if self.no_words_start_with(current_string):
            return
        self.visited[row][col] = True
        self.string_count += 1

        self.dfs(row - 1, col, current_string, current_path, current_score, current_multiplier)  # Up
        self.dfs(row + 1, col, current_string, current_path, current_score, current_multiplier)  # Down
        self.dfs(row, col - 1, current_string, current_path, current_score, current_multiplier)  # Left
        self.dfs(row, col + 1, current_string, current_path, current_score, current_multiplier)  # Right
        self.dfs(row - 1, col - 1, current_string, current_path, current_score, current_multiplier)  # Diagonal: Up-Left
        self.dfs(row - 1, col + 1, current_string, current_path, current_score, current_multiplier)  # Diagonal: Up-Right
        self.dfs(row + 1, col - 1, current_string, current_path, current_score, current_multiplier)  # Diagonal: Down-Left
        self.dfs(row + 1, col + 1, current_string, current_path, current_score, current_multiplier)  # Diagonal: Down-Right
        self.visited[row][col] = False

    def print_progress(self):
        if self.string_count % 50000 == 0:
            print(f"Progress: {self.string_count}")

def randomize_grid(grid):
    for i in range(5):
        for j in range(5):
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            grid[i][j], grid[row][col] = grid[row][col], grid[i][j]
    return grid

def average_score(grid, wordtree):
    my_grid = Grid(grid, wordtree)
    my_grid.generate_strings()
    my_grid.strings = list(set(my_grid.strings))
    my_grid.strings.sort(key=lambda x: x[1], reverse=True)
    return sum([x[1] for x in my_grid.strings[:10]]) / 10

def split_code(letters, dw, tl, dl):


    grid = letters
    # make grid lowercase
    for i in range(5):
        for j in range(5):
            grid[i][j] = grid[i][j].lower()
    
    with open('dict.json', 'r') as fp:
        wordtree = json.load(fp)

    my_grid = Grid(grid, wordtree, dl, tl, dw)
    my_grid.generate_strings()
    my_grid.strings = list(set(my_grid.strings))
    my_grid.strings.sort(key=lambda x: x[1], reverse=True)

    return my_grid.strings[:10]

def split_code_swap(letters, dw, tl, dl):
    grid = letters
    # make grid lowercase
    for i in range(5):
        for j in range(5):
            grid[i][j] = grid[i][j].lower()
    
    with open('dict.json', 'r') as fp:
        wordtree = json.load(fp)

    scores = []
    # for every letter in the grid swap it with every other letter in the alphabet and get the highest score
    for i in range(5):
        for j in range(5):
            for k in range(26):
                if grid[i][j] == chr(ord('a') + k):
                    continue
                grid[i][j] = chr(ord('a') + k)
                my_grid = Grid(grid, wordtree, dl, tl, dw)
                my_grid.generate_strings()
                my_grid.strings = list(set(my_grid.strings))
                my_grid.strings.sort(key=lambda x: x[1], reverse=True)

                scores.append((i,j, chr(ord('a') +k), my_grid.strings[0]))

                # swap back
                grid[i][j] = chr(ord('a') - k)

    scores.sort(key=lambda x: x[3][1], reverse=True)

    return scores[:10]


    