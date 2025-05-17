


def sudoku(mat ,row ,col ,k):
    for i in range(9):
        if mat[i][col] == k: # check for duplicates of k
            return False
        if mat[row][i] == k:
            return False

    start_r, start_c = 3 * (row // 3) , 3 *(col // 3  ) # determine the 3*3 subgrid starting indices for that no duplicates
    # in 3*3 subgrid if k is in 5th  col =3*1=3 ,if 2nd col 2//3=0 gives 3*0=0
    for  i in range(start_r ,start_r + 3):
        for j in range(start_c ,start_c +3):
            print(mat[i][j],end=" \n")
            if mat[i][j] == k:
                return False
    return True

def solve(mat ,row ,col):
    if row == 9:
        return True
    if col == 9:
        return solve(mat ,row +1 ,0)
    if mat[row][col] != 0:
        return solve(mat ,row ,col +1)
    for num in range(1 ,10):
        if sudoku(mat ,row ,col ,num):
            mat[row][col] = num
            if solve(mat, row, col+1):
                return True
            mat[row][col] = 0 # backtrack
    return False

def inpt():
    n = 9
    m = 9
    mat = []
    for i in range(n):
        mat.append(list(map(int ,input().strip().split(" "))))
    if solve(mat ,0 ,0):
        for i in range(len(mat)):
            print(*mat[i])
    else:
        print(-1)
inpt()






















