
def is_safe(i,j,n,m):
    return 0 <= i < n and 0 <= j < m
def maccandy(curx,cury, curcost, dis, mat):
    if curx == edx and cury == edy: # reached the shop
        return curcost
    if mat[stx][sty] ==0  or mat[edx][edy] == 0: # if obstruction then -1
        return -1
    dx = [-1,1,0,0] # possible coordinates x,y
    dy = [0,0,-1,1]
    ans = -1

    for i in range(4):
        nx = curx + dx[i] # next coordinate
        ny = curx + dy[i] # next coordinate
        if is_safe(nx,ny,nxx,mxx): # row and col value
            if mat[nx][ny] == 1 and dis[nx][ny] == 0: # same mat or copy
                dis[nx][ny] = 1
                ans = max(ans,maccandy(nx,ny,curcost+1, dis, mat))
                dis[nx][ny] = 0 # make it 0 again
    print(ans)
    print(curcost)
    return ans

def solve(n,m,matx,bob_i,bob_j,shi,shj):
    global nxx,mxx,stx,sty,edx,edy
    mat = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j] = matx[i][j] # matx took input row by row
    nxx,mxx = n, m
    stx,sty,edx,edy = bob_i,bob_j,shi,shj

    dis = [[0 for _ in range(m)] for _ in range(n)]
    dis[sty][sty] = 1
    return maccandy(stx,sty,0,dis,mat)

n,m = map(int,input().split(" "))
matx = []
for _ in range(n):
    row = list(map(int,input().split(" ")))
    matx.append(row)
stx1,sty1 = map(int,input().split(" "))
edx1,edy1 = map(int,input().split(" "))
result = solve(n,m,matx,stx1,sty1,edx1,edy1)
print(result)












