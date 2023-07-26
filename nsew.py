#!/usr/bin/env python3
# Mission: Coding a classic `Nsew`
# (pronounced NessEwwh   ;-)

'''
The Game of Nsew
================
Objective is to see how many "risks"
(moves into unknown regions) we can
endure before being "zeroed," or
scoring less than zero.
'''


debug = False
from random import randrange

def move(w, pos, board_size):
    hpos = list(pos)
    if w == 'n':
        pos[1] -= 1
    elif w == 's':
        pos[1] += 1
    elif w == 'e':
        pos[0] += 1
    elif w == 'w':
        pos[0] -= 1
    else:
        return False

    for ipos in 0, 1:
        if pos[ipos] < 0:
            pos[ipos] = 0
        if pos[ipos] >= board_size:
            pos[ipos] = board_size -1
    if pos == hpos:
        print("bump..")
        return False
    return True


def show(board, pos):
    for yy, row in enumerate(board):
        for xx, col in enumerate(row):
            if xx == pos[0] and yy == pos[1]:
                print('[$]\t', end='')
            elif col == 0:
                print(f'{col}\t', end='')
            else:
                if debug:
                    print(f'{col}\t', end='')
                else:
                    print('?\t', end='')
        print()

score = 10
board_size = 8
board = [[int(randrange(-3,3)) for _ in range(board_size)] for _ in range(board_size)]
risks = hi = lo = 0
for row in board:
    for col in row:
        if col < 0:
            lo += col
            risks += 1
        elif col > 0:
            hi += col
            risks += 1
    
print("Welcome to Nsew!")
print(__doc__)
print(f"High: {hi} Low: {lo} Risks: {risks}\n")

moved = 0
pos = [int(board_size/2), int(board_size/2)]
show(board, pos) # Jump
while True:
    print(f"Your Score: {score}, Risks: {moved}")
    where = input("NSEW? ").strip().lower()
    if not where:
        break     
    if move(where[0], pos, board_size):
        if board[pos[1]][pos[0]] != 0:
            moved +=1
        score += board[pos[1]][pos[0]]
        board[pos[1]][pos[0]] = 0
        if score < 0:
            debug = True
        show(board, pos)
        if score < 0:
            print(f"Zeroed in {moved} risks. [{hi}:{lo}]")
            break
    else:
        print('Please enter either N,S,E or W')
