
def exist(board,woed):
    def dfs(x,y,index):
        if index == len(woed): # index has incremented to len of word
            return True
        if x<0 or x >= n or y < 0 or y >= m or board[x][y] != woed[index] or visited[x][y]:
            return False
        visited[x][y] = True
        print(visited) # if true 2 times
        if dfs(x+1,y,index + 1) or dfs(x-1,y,index + 1) or dfs(x,y+1,index + 1) or dfs(x,y-1,index + 1):

            return True # found word

        visited[x][y] = False
        return  False
    n = len(board)
    m = len(board[0])
    visited = [[False]*m for _ in range(n)]
    for i  in range(n):
        for j  in range(n):
            if board[i][j] == woed[0] and dfs(i,j,0):
                return "Yes" # found  2 times
    return "No"
n,m = map(int,input().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(input().strip().split(" ")))
woed = input().strip()
result = exist(board,woed)
print(result)












