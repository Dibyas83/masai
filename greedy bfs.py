"""
search algorithm that expands the node  that is closest to the goal ,as estimated by a heuristic functon h(n) - a estimate taking h as input when coordinates are there of points
it is not always optimal

A* Search(a modification to greedy bfs)

search algorithm that expands node with lowest value of g(n) + h(n)
g(n) = cost to reach node
h(n) = estimated cost to goal
optimal if
- h(n) is admissible and consistent


-------------
Adversal search  -  in tic tac
find optimal + leading to future multi optimal sol + instead of finding optimal sol it will try to block anather to getting to optimal

1-minimax -three out comes x win -1,draw 0,y win 1
somebody trying to win somebody trying to draw

game functions

So init
player() whose turn one by one[xyxyxyxyx]
actions()  set of legal moves
result(s,a) returns state after action a taken
terminal() if draw or win, it has set of sol
utility(s)  1 0 or -1 output val

each player calculating own optimal and other pleyers next optimal move
will be like a tree and depth unlimited minmax

recursive process

func max-val(state): max player
  if terminal(state):
   return utility(state)

  v = -infinity
  for action in actions(state):
    v = max(v,min-value(result(state,action)))
  return v

func min-val(state): min player
  if terminal(state):
   return utility(state)

  v = infinity
  for action in actions(state):
    v = max(v,max-value(result(state,action)))
  return v

this gies huge result
                         u
possible-move    pm       pm   pm   pm   pm   pm   pm   pm
pm pm pm pm    pm pm pm
depth-limited minmax(optimized)
after certain amt of move i will stop
                         u
        pm          pm          pm
  pm  pm  pm     pm pm pm









"""

"""
A Breadth-First Search (BFS) maze solver in Python utilizes the BFS algorithm to find the shortest path from a starting point to an end point in a maze. The maze is typically represented as a 2D grid or array, where cells can be either walls or open paths.
Here's a breakdown of how a BFS maze solver in Python generally works:
Maze Representation:
The maze is commonly represented as a list of lists (a 2D array) where each element represents a cell.
Values like 0 or . can represent open paths, and 1 or # can represent walls.
Specific characters like S and E can mark the start and end points.
BFS Algorithm Implementation:
Queue: A collections.deque is used as a queue to store the cells to be explored. This ensures First-In, First-Out (FIFO) behavior, which is essential for BFS.
Visited Set/Array: A set or a 2D array is used to keep track of visited cells to prevent infinite loops and redundant exploration.
Parent Tracking (for path reconstruction): A dictionary or a similar structure can be used to store the "parent" of each cell, allowing reconstruction of the path from the end point back to the start.
Steps:
Initialization:
Find the starting coordinates in the maze.
Add the starting cell to the queue and mark it as visited.
Exploration Loop:
While the queue is not empty:
Dequeue the current cell.
If the current cell is the end point, reconstruct and return the path.
Explore Neighbors: For each valid neighbor (up, down, left, right) of the current cell:
Check if the neighbor is within maze bounds, is an open path, and has not been visited.
If valid, mark the neighbor as visited, add it to the queue, and record its parent (the current cell).
No Path Found: If the queue becomes empty and the end point has not been reached, it means no path exists.
Path Reconstruction:
If the end point is reached, trace back from the end cell to the start cell using the parent information to reconstruct the shortest path.
Example (Conceptual):
Python



"""

from collections import deque

def solve_maze_bfs(maze):
    start = None
    end = None
    # Find start and end points
    for r_idx, row in enumerate(maze):
        for c_idx, cell in enumerate(row):
            if cell == 'S':
                start = (r_idx, c_idx)
            elif cell == 'E':
                end = (r_idx, c_idx)

    if not start or not end:
        return "Start or End not found!"

    queue = deque([(start, [start])])  # (current_cell, path_to_current_cell)
    visited = set([start])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
                    maze[nr][nc] != '#' and (nr, nc) not in visited):
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), new_path))

    return "No path found."


maze = [
        ['S', '.', '#', '.'],
        ['.', '.', '.', '.'],
        ['#', '.', '#', '.'],
        ['.', '#', '.', 'E']
 ]
solution_path = solve_maze_bfs(maze)
print(solution_path)





