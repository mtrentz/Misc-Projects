import numpy as np

# Solves sudoku boards. Main idea is to keep finding new algorithms and compare time.

board = [[0,5,7,0,6,1,9,0,0],
         [0,0,8,0,0,0,1,4,7],
         [2,1,0,0,0,0,0,0,0],
         [9,0,0,7,1,0,0,6,8],
         [0,4,5,3,0,0,0,1,0],
         [0,8,0,0,0,0,4,7,0],
         [0,0,0,2,0,7,0,0,0],
         [5,2,0,0,0,0,0,9,0],
         [8,0,0,0,4,5,0,0,1]]

board = np.array(board)
col_len = board.shape[0]
row_len = board.shape[1]
full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(board)


def find_empty(bo):
    for y in range(col_len):
        for x in range(row_len):
            if bo[y][x] == 0:
                return y, x
    return None


def check_ok(bo, num, pos):
    sub_pos = (pos[0]//3, pos[1]//3)
    for y in range(col_len):
        for x in range(row_len):
            if bo[pos[0]][x] == num or bo[y][pos[1]] == num:
                return False
            if (y//3, x//3) == sub_pos and bo[y][x] == num:
                return False
    return True


def solver(bo):
    pos = find_empty(bo)
    if not pos:
        return True
    y, x = pos
    for i in full_set:
        if check_ok(bo, i, (y, x)):
            bo[y][x] = i
            if solver(bo):
                return True
            bo[y][x] = 0
    return False
            

print("---------")
solver(board)
print(board)

