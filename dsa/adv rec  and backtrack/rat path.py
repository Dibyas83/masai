
def possible_paths(n,maze,row,col,path,ans):
    if row < 0 or row >= n or col <0 or col >= n or maze[row][col] == 0:
        return
    if row == n-1 and col == n-1: # reached dstination
        ans.append(path)
        return
    maze[row][col] = 0 # mark the cell a visited
    possible_paths(n, maze, row+1, col, path+"d", ans) # if sucess path is added to ans which stores each step
    possible_paths(n, maze, row, col-1, path+"l", ans) # all possible direction is tried
    possible_paths(n, maze, row, col+1, path+ "r", ans)
    possible_paths(n, maze, row-1, col, path+"u", ans)
    print(maze)
    print("-----------")
    maze[row][col] = 1  # unmark the cell
    print(maze,"after")
n= int(input())
maze = [list(map(int,input().strip().split(" "))) for _ in range(n)]
ans = []
if maze[0][0] == 1: # not 0 but allowed
    possible_paths(n,maze,0,0,"",ans)
if ans: # not 0
    ans.sort()
    for path in ans:
        print(path,end=" ")
else:
    print(-1)








