import numpy as np


board = np.array([[8,1,2,1],
        [1,0,4,1],
        [0,0,2,2],
        [4,4,8,16]])


def push(board, direction):
    def push_left(board):
        def push_left_once(board):
            new_b = []
            for i,row in enumerate(board):
                nr = [x for x in row if x > 0]
                if len(nr) > 1:
                    
                        for j in range(len(nr)-1, 0, -1):
                            if nr[j] == nr[j-1]:
                                nr[j] = 0
                                nr[j-1] *= 2
                while len(nr) < 4:
                    nr.append(0)
                new_b.append(nr)
            return new_b
        
        return push_left_once(push_left_once(push_left_once(board)))

    if direction == "left":
        return push_left(board)
    if direction == "right":
        return np.flip(push_left(np.flip(board, axis=1)), axis=1)
    if direction == "down":
        return np.rot90(push_left(np.rot90(board, k=-1)), k=1)
    if direction == "up":
        return np.rot90(push_left(np.rot90(board, k=1)), k=-1)
def printb(board):
    print("-"*10)
    for row in board:
        for num in row:
            print(num," ",end="")
        print()
    print("-"*10)

if __name__ == "__main__":
    printb(board)
    board = push(board, "up")
    printb(board)


