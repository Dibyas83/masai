
def solve(p,k,arr,curr,ans,res,idx):
    if curr > p:
        return
    if curr == p and len(ans) == k:
        res.append(ans[:]) # record the curr combination
        return
    for i in range(idx,9):
        ans.append(arr[i])
        solve(p,k,arr, curr + arr[i], ans, res, i+1)# solve at every i ,updating index,until cur>p or ==p and len(ans) = k) we pop and bring new element
        print(ans)
        ans.pop()

if __name__=="__main__":
    p,k = map(int,input().split(" "))
    arr = [1,2,3,4,5,6,7,8,9]
    ans = []
    res = []
    solve(p,k,arr,0,ans,res,0)
    if not res:
        print(-1)
    else:
        res = sorted(res)
        for combi in res:
            print(" ".join(map(str,combi)))











