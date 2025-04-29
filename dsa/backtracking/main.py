
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

















