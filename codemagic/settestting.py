import random
import copy

new_moves = [[0,0,0,122],[0,0,0,3],[0,0,0,31],[0,0,0,12]]

new_moves.sort(key=lambda x: x[3])
# get the top half of the new_moves
new_moves = new_moves[:10]

print(new_moves)