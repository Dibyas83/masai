from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        ans = []

        i, j = 0, 0

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        direction = RIGHT

        UP_WALL = 0

        RIGHT_WALL = n

        DOWN_WALL = m

        LEFT_WALL = -1

        while len(ans) != m * n:

            if direction == RIGHT:

                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])

                    j += 1

                i, j = i + 1, j - 1

                RIGHT_WALL -= 1

                direction = DOWN

            elif direction == DOWN:

                while i < DOWN_WALL:
                    ans.append(matrix[i][j])

                    i += 1

                i, j = i - 1, j - 1

                DOWN_WALL -= 1

                direction = LEFT

            elif direction == LEFT:

                while j > LEFT_WALL:
                    ans.append(matrix[i][j])

                    j -= 1

                i, j = i - 1, j + 1

                LEFT_WALL += 1

                direction = UP

            else:

                while i > UP_WALL:
                    ans.append(matrix[i][j])

                    i -= 1

                i, j = i + 1, j + 1

                UP_WALL += 1

                direction = RIGHT

        return ans

        # Time: O(m*n)

        # Space: O(1)



class Solutio:
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        m, n = len(matrix), len(matrix[0])
        startrow, startcol = 0, 0
        endrow = m - 1
        endcol = n - 1
        while startrow <= endrow and startcol <= endcol:
            # Traverse from left to right along the top row
            for i in range(startcol, endcol + 1):
                result.append(matrix[startrow][i])
            startrow += 1
            # Traverse from top to bottom along the right column
            for i in range(startrow, endrow + 1):
                result.append(matrix[i][endcol])
            endcol -= 1
            # Traverse from right to left along the bottom row (if applicable)
            if startrow <= endrow:
                for i in range(endcol, startcol - 1, -1):
                    result.append(matrix[endrow][i])
                endrow -= 1
            # Traverse from bottom to top along the left column (if applicable)
            if startcol <= endcol:
                for i in range(endrow, startrow - 1, -1):
                    result.append(matrix[i][startcol])
                startcol += 1
        return result





