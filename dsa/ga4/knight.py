
def solve(i,j,n,board):
    if i < 0 or j < 0 or i >= 10 or j >= 10:
        return
    if n == 0:
        board[i][j] = 1
        return
    solve(i - 2,j - 1,n-1,board)
    solve(i - 2,j + 1,n-1,board)
    solve(i + 2,j - 1,n-1,board)
    solve(i + 2,j + 1,n-1,board)
    solve(i - 1,j - 2,n-1,board)
    solve(i + 1,j - 2,n-1,board)
    solve(i - 1,j + 2,n-1,board)
    solve(i + 1,j + 2,n-1,board)

def main():
    r, c, n = map(int,input().split(" "))
    board = [[0] * 10  for _ in range(10)]   # 0*10  10 times
    solve(r-1,c-1,n,board)
    count = sum(board[i][j] == 1 for i in range(10) for j in range(10))
    print(count)

#if __name__== "__main __":
main()











