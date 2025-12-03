
# in the m * n matrix convert the row and col to 0 where there is 0

# make changes to a copy and compare if not overtaking or repeatetive conversion
# instead of copy we can use teo arrays of cols and rows

# and keep record which col and rows are to be set to 0 ,when traversing

"""
                    -      -      -

                -   1       0       1
                -   1       0       1
                -   0       1       1
------------------------------------------------
                     -      -      -

                -0  0       0       1  rowzero
                -0  1       0       1
                -0  0       1       1
"""

class Solut:
    def setzeroes(self,matrix: list[list[int]]) -> None:
        rows, cols  = len(matrix), len(matrix[0])
        rowzero = False

        # determine which row/col need to be 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r >0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        for r in range(1, rows):  # skip 1st row
            for c in range(1, cols): # skip 1st col
                if matrix[0][r] == 0 or matrix[r][0] == 0: # except 1st row/col
                    matrix[r][c] = 0 # set curr pos to 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0 #  zeroth col of every row be 0

        if rowzero:
             for c in range(cols):
                 matrix[0][c] = 0   #  zeroth row of every col be 0

