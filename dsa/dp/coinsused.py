
def solve(price,no_of,arr,cur_sum,ans,res,idx):
    print(cur_sum,len(ans))

    if cur_sum > price:
        return
    if cur_sum == price and len(ans) == no_of:
        print(ans)
        res.append(ans[:])
        return
    for i in range(idx,9):
        ans.append(arr[i])
        solve(price, no_of, arr, cur_sum + arr[i], ans, res, i + 1)
        ans.pop()

if __name__== "__main__":
    price, no_of =map(int,input().split(" "))
    arr = [1,2,3,4,5,6,7,8,9]
    ans = []
    res = []
    solve(price,no_of,arr,0,ans,res,0)
    if not res:
        print(-1)
    else:
        res = sorted(res)
        for combination in res:
            print(" ".join(map(str,combination)))



















































