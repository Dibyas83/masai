
"""
9*9 board. only the filled cell needs to be validated
no repetition in row and col from 1-9,and in 9 boxes of 3*3

solution for row , col, box  then combine
using hash set to compare

search or traversing  inside boxes
(0,1,2) / 3 = 0
(3,4,5) / 3 = 1
(6,7,8) / 3 = 2

finding hash set or box no
row/3 + 3+ col/3
"""
def isValid_Sudoku(board):
    N = 9

    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            val = board[r][c]

            if val == '.':
                continue

            if val in rows[r]:  # duplicate found
                return False
            rows[r].add(val)

            if val in cols[c]:
                return False
            cols[c].add(val)

            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)

    return True









