
count = 0
def is_safe(r,c,mat):
    for i in range(r): # it is checking from 0 to curr row to end row
        if mat[i][c] == 1:
            return False

    for i,j in zip(range(r-1,-1,-1),range(c+1,len(mat[0]))):
        if mat[i][j] == 1:
            return False
    for i,j in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
        if mat[i][j] == 1:
            return False
    return True

def n_queens(r,mat):
    global count
    if r == len(mat): # succes
        count += 1
        return
    for j in range(len(mat[0])):
        if is_safe(r,j,mat): # checks in every col of row
            mat[r][j] = 1 # if true put 1

            n_queens(r + 1,mat) # then goes to next row
            mat[r][j] = 0 # if r+1 fails is safe backtrack
    print(mat)
    print(count)
def main(n):
    global count
    mat = [[0 for _ in range(n)] for _ in range(n)]
    n_queens(0,mat)

    print(count)

if __name__ == "__main__":
    n = int(input().strip())
    main(n)


















