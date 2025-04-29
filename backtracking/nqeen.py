

def solv(n):
    sol = []
    board= [-1] * n # board[i] = col of queen at row i

    def isvalid(row,col):
        for r in range(row): # check if same col or diagonal
            if board[r] == col or abs(board[r] - col) == abs(r-row):
                return False
        return True
    def backtrack(row):
        if row == n:
            solution = [] # convert board position to visual representation
            for r in range(n):
                row_rep = ["."] * n
                row_rep[board[r]] = "q"
                solution.append("".join(row_rep))
            sol.append(solution)
            return
        for col in range(n):
            if isvalid(row,col):
                board[row] = col
                backtrack(row+1)
                board[row] = -1 # backtrack

    backtrack(0)
    return sol
n= 4
al4sol = solv(n)
for s in al4sol:
    for r in s:
        print(r)
    print()

"""
N-Queen must place exactly one queen in each row.
Diagonal checks are crucial: difference in row index = difference in column index
"""
#-----------
"""
Step 1: Place a Queen
Start by placing a queen in the first row at any valid position (any column in that row).
Step 2: Check for Attacks
After placing a queen, check if it attacks any previously placed queens. A queen can attack if:
Two queens share the same column.
Two queens share the same diagonal (either left or right diagonal).
Step 3: Move to the Next Row
Move to the next row and attempt to place another queen. Repeat the process, checking for attacksafter each placement.
Step 4: Backtrack if Necessary
If you reach a point where no valid column exists in the current row (due to attacks from previouslyplaced queens), backtrack. This means you undo the last queen placement, move it to a differentcolumn, and proceed again.
Step 5: Continue Until All Queens Are Placed or No Solution is Found
Repeat the process for all rows. If you successfully place all queens, the problem is solved. If youreach the end of the board and cannot find a valid configuration, backtrack to the previous steps andattempt new placements.

"""

print("--------------------------")
# check queen can be safely placed at position(row,col)
def is_safe(board,row,col,n):
    for i in range(row): #check col for any queen already placed
        if board[i][col] == 1:
            return False
# check left diagonal for any queen
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):

        if board[i][j] == 1:
            return False

# check right diagonal for any queen
    for i, j in zip(range(row - 1, -1, -1), range(col+1,n)):

        if board[i][j] == 1:
            return False
# if no queens attacking return true
    return True
def solve_queen(board,row,n):
    if row >= n: # if all queens are placed
        return True
    for col in range(n): # try placing a queen in every col of the current row
        if is_safe(board, row, col, n):
            board[row][col] = 1 # placing queen
            if solve_queen(board, row +1, n): # recursively place queens in next row
                return  True
            board[row][col] = 0 # backtrack if no valid placement

    return False # if no placement is possible in this row
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

# driver code to solve n queen problem for  n= 4
n = 4
board = [[0 for _ in range(n)] for _ in range(n)]
if solve_queen(board,0,n): # start backtracking process
    print_board(board) # print solution board
else:
    print("no sol")











