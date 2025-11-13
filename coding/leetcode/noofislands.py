# graph problem
#
"""
1  1  1  0  0
1  1  0  0  0
1  1  0  0  0
0  0  0  1  1

island are connected to neighbors horizontally or vertical .
"""
import collections


# island made of 1 and ocean of 0.so there are 2 islands


class Sole:
    def no_of_ones(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c): # it is not recursive it is iterative

            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))

            while q:  # not empty
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr,dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visit):

                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands










