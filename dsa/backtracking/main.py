
"""
An algorithmic technique for solving problems by exploring all
possible solutions incrementally.
It builds solutions step-by-step and abandons (”backtracks”) a
solution as soon as it is determined to be invalid.
Useful for solving constraint satisfaction problems,
combinatorial problems and optimization problems
where the goal is to build a valid solution step-by-step.
Real-world relevance
 Puzzle Solving
: Think of Sudoku or crosswords, where you systematically guess and checkpossibilities.
Route Planning
: Finding paths that meet certain conditions (like traveling through specificpoints).
Resource Allocation
: Assigning limited resources in a system under various constraints.


Backtracking explores the solution space using a state space
tree, where
Each node represents a partial solution.
The root represents the initial state.
The leaves represent complete solutions.
At each step, the algorithm:
Chooses a candidate to extend the current partial solution.
Checks constraints to determine if the candidate is valid.
Recurses to extend the solution if the candidate is valid.
Backtracks (undoes the last choice) if the candidate is invalid
or no further extension is possible.

Q
: If a solution is found, do we stop the whole backtracking immediately or continue searching?
A
: It depends on the problem requirement. If we only need
one
valid solution, we can stop. If weneed
all
solutions, we continue until all possibilities are exhausted.
2.2




def backtrakin(sol,candidates):
    if sol is complete:
        process solution
        return
    for cand in candidates:
        if cand is valid:
            sol.add(cand)
            backtrakin(sol,next_candidates)
            sol.remove(cand)
"""

def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    def backtrack(board, col):
        if col == N:
            result.append([''.join(row) for row in board])
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'

    backtrack(board, 0)
    return result


# Example 1
N1 = 4
result1 = solve_n_queens(N1)
print(f"Solution for Example 1 with N = {N1}:")
for solution in result1:
    print(solution)
print()

# Example 2
N2 = 1
result2 = solve_n_queens(N2)
print(f"Solution for Example 2 with N = {N2}:")
for solution in result2:
    print(solution)

"""
#backtracking_template.py-------------------
#<script src="https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6.js"></script>
def is_valid_state(state):
    # check if it is a valid solution
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
    
    
    
    
#leetcode_nqueens.py----------------------------------------
class Solution:
    """
    example on the left: [1, 3, 0, 2]
    example on the right: [2, 0, 3, 1]
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret
        
        
        
        
#leetcode_sudoku.py-------------------------
class Solution:
    from itertools import product
    
    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.search(board)
    
    def is_valid_state(self, board):
        # check if it is a valid solution
        # validate all the rows
        for row in self.get_rows(board):
            if not set(row) == self.DIGITS:
                return False
        # validate columns
        for col in self.get_cols(board):
            if not set(col) == self.DIGITS:
                return False
        # validate sub-boxes
        for grid in self.get_grids(board):
            if not set(grid) == self.DIGITS:
                return False
        return True

    def get_candidates(self, board, row, col):
        used_digits = set()
        # remove digits used by the same row
        used_digits.update(self.get_kth_row(board, row))
        # remove digits used by the same column
        used_digits.update(self.get_kth_col(board, col))
        # remove digits used by the 3x3 sub-box
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= set([self.EMPTY])
        candidates = self.DIGITS - used_digits
        return candidates

    def search(self, board):
        if self.is_valid_state(board):
            return True # found solution
        
        # find the next empty spot and take a guess
        for row_idx, row in enumerate(board):
            for col_idx, elm in enumerate(row):
                if elm == self.EMPTY:
                    # find candidates to construct the next state
                    for candidate in self.get_candidates(board, row_idx, col_idx):
                        board[row_idx][col_idx] = candidate
                        # recurse on the modified board
                        is_solved = self.search(board)
                        if is_solved:
                            return True
                        else:
                            # undo the wrong guess and start anew
                            board[row_idx][col_idx] = self.EMPTY
                    # exhausted all candidates
                    # but none solves the problem
                    return False
        # no empty spot
        return True

    # helper functions for retrieving rows, cols, and grids
    def get_kth_row(self, board, k):
        return board[k]

    def get_rows(self, board):
        for i in range(self.SHAPE):
            yield board[i]
    
    def get_kth_col(self, board, k):
        return [
            board[row][k] for row in range(self.SHAPE)
        ]

    def get_cols(self, board):
        for col in range(self.SHAPE):
            ret = [
                    board[row][col] for row in range(self.SHAPE)
            ]
            yield ret

    def get_grid_at_row_col(self, board, row, col):
        row = row // self.GRID * self.GRID
        col = col // self.GRID * self.GRID
        return [
            board[r][c] for r, c in 
            product(range(row, row + self.GRID), range(col, col + self.GRID))
        ]

    def get_grids(self, board):
        for row in range(0, self.SHAPE, self.GRID):
            for col in range(0, self.SHAPE, self.GRID):
                grid = [
                    board[r][c] for r, c in 
                    product(range(row, row + self.GRID), range(col, col + self.GRID))
                ]
                yield grid
"""













