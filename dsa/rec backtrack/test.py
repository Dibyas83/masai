

print(2//3)
print(5//3)
m,n = 9,9
dis = [[0 for _ in range(m)] for _ in range(n)]
dis[5][5] = 1
print(dis)
#------------
board = [[0]*7 for _ in range(7)]
for i in range(7):
    for j in range(7):
        board [i][j] = 0
print(board)
res = [[0]*7 for _ in range(7)]
#-----------------
def is_safe(row,col,n,board):
    for i in range(row-1):
        if board[i][col] == 1:
            return False # or -1
    # check upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 1 and j >= 1:
        if board[i][j] == 1:
            return False
        i = i -1
        j = j - 1
    # check upper rigt diagonal
    i = row - 1
    j = col +1
    while i >= 1 and j <= n:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True # if passes no 1 in wrong position

def solve(row,n,board):
    if row>n: # queens placed in board terminating condition
        print(board,n)
        return True
    for col in range(1,n):
        if is_safe(row,col,n,board):
            board[row][col] = 1 # place queen
            if solve(row+1,n,board):
                return True
            else:
                board[row][col] = 0 # backtrack as row +1 will not give sol so goes to next col
    return False
"""
class Solution: 

int res = 0 ;

void helper(vector<vector<int>> &mat,int i,int j,int r,int c,int ans){
    
    if(i<0 || j<0 || i>=mat.size() || j>= mat[0].size()){
        return;
    }
    
    
    if mat[i][j] == -1 || mat[i][j] == 0: # visited and hurdle
        return
    
    
    if(i == r && j == c){
        res = max(res,ans);
    }
    
    mat[i][j] = -1;
    
    helper(mat,i+1,j,r,c,ans+1); # updating length value if any of these apply
    helper(mat,i-1,j,r,c,ans+1);
    helper(mat,i,j+1,r,c,ans+1);
    helper(mat,i,j-1,r,c,ans+1);
    
    mat[i][j] = 1; after processing make -1 as 1 again
    
    
}
    int longestPath(vector<vector<int>> matrix, int xs, int ys, int xd, int yd)
    {
        // code here
        
        if(matrix[xs][ys] == 0 || matrix[xd][yd] == 0) 
        return -1;
        
        int ans = 0;
       
        
        helper(matrix,xs,ys,xd,yd,ans); # ans stores length of path and res stores max path
        return res;
    }
};
"""






"""
def sudoku(mat ,row ,col ,k):
    for i in range(9):
        if mat[i][col] == k: # check for duplicates of k
            return False
        if mat[row][i] == k:
            return True

    start_r, start_c = 3 * (row // 3) , 3 *(col // 3  )# determine the 3*3 subgrid starting indices
    for  i in range(start_r ,start_r + 3):
        for j in range(start_c ,start_c +3):
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
            if solve(mat, row, col):
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

"""













