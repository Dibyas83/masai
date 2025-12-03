
# return lements in spiral from top left

# boundry keep shrinking, using twopointer, l,r col, t,b rows
"""
         l                   r
      t  1   2   3   4   5
         6   7   8   9   10
         11  12  13  14  15
      b

"""
# shift top row boundry to below, and right col to left,then move bot row to up when
# they are finished then move left bound to right


class Solu:
    def spiral(self,matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0]) # right is 1 higher than matrix boundary
        top, bot = 0, len(matrix)   # bot is 1 higher than matrix boundary

        while left < right and top < bot:
            for i in range(left, right): # get every i in the top row
                res.append(matrix[top][i])
            top += 1  # this will bring the top to down
            # got every i in the right col
            for i in range(top, bot): # get every i in the right col
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bot):
                break

            for i in range(right - 1, left-1, -1): # get every i in the bot row
                res.append(matrix[bot-1][i])
            bot -= 1  # this will bring the top to down
            # got every i in the right col
            for i in range(bot-1,top-1, -1): # top has incremented before.get every i in the left col
                res.append(matrix[i][left])
            left += 1

        return res









