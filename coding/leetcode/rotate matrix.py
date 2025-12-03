
# WHEN WE ARE MOVING we have to shift the prev ele instantly or store it in temp place
#left col becomes the  top row in rev order, top row becomes theright col,
# right col becomes the bot row in rev order, bot row to teft col
"""
         l            r
      t  1   2   3   4
         5   6   7   8               11   9   5   1
         9   10  11  12              14   10  6   2
      b  13  14  15  16              15   11  7   3
                                     16   12  8   4

"""
# move from 1st col of top row  to   1st row of right col
# move from 2nd col of top row  to   2nd row of right col

# after rotatng outermost layer,the square will shrink
# we need one temp var, we move 1 to temp  , 13 to 1  and 16 to 13 and  4 to 16  then 1 to 4 in rev order

class Solu:
    def spiral(self,matrix: list[list[int]]) -> None:
        res = []
        left, right = 0, len(matrix[0]) -1 # right is 1 higher than matrix boundary

        while left < right:
            for i in range(right-left):
                top, bot = left, right
                topleft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bot-i][left]
                matrix[bot-i][left] = matrix[bot][right-i]
                matrix[bot][right-i] = matrix[top+i][right]
                matrix[top +i][right] = topleft
            right -= 1  # shrinking
            left += 1
